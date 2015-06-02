import re
import os
import sys
import time
import json
import curses
import random
import logging
import requests
import argparse
import threading

from collections import Counter
from xml.dom import minidom
from xml.etree import ElementTree

from virtTrinity import provider
from virtTrinity.utils import rnd


class VirtTrinityApp(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            '--server',
            action='store',
            help='Server address',
            dest='server',
            default='127.0.0.1',
        )
        self.parser.add_argument(
            '--port',
            action='store',
            help='Server port',
            dest='port',
            default='8067',
        )
        self.parser.add_argument(
            '--username',
            action='store',
            help='Server authentication user name',
            dest='username',
        )
        self.parser.add_argument(
            '--password',
            action='store',
            help='Server authentication password',
            dest='password',
        )
        self.parser.add_argument(
            '--providers',
            action='store',
            help="List of test providers separated by ','",
            dest='providers',
            default='virsh_cmd',
        )
        self.parser.add_argument(
            '--list-providers',
            action='store_true',
            help='List all available test providers',
            dest='list_providers',
        )
        self.args, _ = self.parser.parse_known_args()

        self.providers = self._process_providers()

        self.stats = {
            "skip": Counter(),
            "failure": Counter(),
            "success": Counter(),
            "timeout": Counter(),
            "expected_neg": Counter(),
            "unexpected_neg": Counter(),
            "unexpected_pass": Counter(),
        }
        self.counters = {
            "cnt": 0,
            "skip": 0,
            "failure": 0,
            "success": 0,
            "timeout": 0,
            "expected_neg": 0,
            "unexpected_neg": 0,
            "unexpected_pass": 0,
        }
        self.exiting = False
        self.pause = False
        self.test_thread = threading.Thread(
            target=self.run_tests,
        )
        self.send_queue = []
        self.last_item = None
        self.cur_counter = 'failure'
        self.screen = curses.initscr()

    def _stat_result(self, item):
        """
        Categorizes and keep the count of a result of a test item depends on
        the expected failure patterns.
        """
        res = item.res
        fail_patts = item.fail_patts

        test_pattern = 'PATTERNS.TO.TEST.ON'

        self.counters['cnt'] += 1
        if res:
            if res.exit_status == 'timeout':
                self.counters['timeout'] += 1

            if fail_patts:
                if res.exit_status == 'success':
                    self.counters['unexpected_pass'] += 1
                    self.stats['unexpected_pass'][res.stderr] += 1
                elif res.exit_status == 'failure':
                    if any([re.search(p, res.stderr) for p in fail_patts]):
                        self.counters['expected_neg'] += 1
                        self.stats['expected_neg'][res.stderr] += 1
                    else:
                        self.counters['unexpected_neg'] += 1
                        self.stats['unexpected_neg'][res.stderr] += 1
            else:
                if res.exit_status == 'success':
                    self.counters['success'] += 1
                    self.stats['success'][res.stderr] += 1
                elif res.exit_status == 'failure':
                    self.stats['failure'][res.stderr] += 1
                    self.counters['failure'] += 1
                    if test_pattern in res.stderr:
                        item.pprint()
                        exit(0)
        else:
            self.counters['skip'] += 1

    def _show_report(self):
        """
        Show the most frequent pattern of a specified result type depends on
        the expected failure patterns.
        """
        maxy, maxx = self.screen.getmaxyx()
        width, height = maxx / 2, maxy

        cnt = self.counters["cnt"]

        cur_y = 1
        item_id = 0
        pad = curses.newpad(height, width)
        stat_cnt = self.counters[self.cur_counter]
        for err, c in self.stats[self.cur_counter].most_common(30):
            pad.addstr(cur_y, 1, str(c))
            pad.addstr(cur_y, 6, "%6.2f" % (float(c) * 100 / stat_cnt))

            style = curses.A_BOLD if bool(item_id % 2) else curses.A_DIM
            for line in err.splitlines():
                if len(line) > (width - 17):
                    line = line[:(width - 17)]
                pad.addstr(cur_y, 15, line, style)
                cur_y += 1
                if cur_y == height:
                    break
            if cur_y == height:
                break
            item_id += 1
        pad.box()
        title = self.cur_counter.replace('_', ' ').upper()
        pad.addstr(0, 10, ' MOST FREQUENT %s ' % title)
        if cnt:
            pad.addstr(0, 2, '%.2f%%' % (float(stat_cnt) / cnt * 100))
        pad.refresh(0, 0, 0, 0, height, width)

    def _show_last_result(self):
        """
        Show last result of tested items
        """
        maxy, maxx = self.screen.getmaxyx()
        width, height = maxx / 2, maxy

        pad = curses.newpad(height, width)
        item = self.last_item
        if item:
            lines = ''
            lines = str(item.res)
            if item.xml is not None:
                if isinstance(item.xml, ElementTree.Element):
                    xml = minidom.parseString(
                        ElementTree.tostring(item.xml)).toprettyxml()
                else:
                    xml = str(item.xml)
                lines += xml
            cur_y = 1
            for line in lines.splitlines():
                line = line.replace('\t', '  ')
                if len(line) > (width - 2):
                    line = line[:(width - 2)]
                pad.addstr(cur_y, 1, line)
                cur_y += 1
                if cur_y == height:
                    break
        pad.box()
        pad.addstr(0, 10, ' LAST RESULT ')
        pad.refresh(0, 0, 0, maxx / 2, maxy, maxx)

    def _show_exit(self):
        """
        Show existing pad in the center of screen
        """
        maxy, maxx = self.screen.getmaxyx()
        width, height = 30, 5

        pad = curses.newpad(height, width)
        pad.box()
        pad.addstr(2, 10, ' EXISTING... ')
        pad.refresh(0, 0, maxy / 2 - 3, maxx / 2 - 15,
                    maxy / 2 + 3, maxx / 2 + 15)

    def _process_providers(self):
        """
        Print a list of available providers if --list-providers is set
        or return a dict of specified providers.
        """
        all_providers = provider.get_providers()
        if self.args.list_providers:
            print ' '.join(all_providers.keys())
            sys.exit(0)

        providers = {}
        if self.args.providers:
            for name in self.args.providers.split(','):
                try:
                    providers[name] = all_providers[name]
                except KeyError:
                    sys.stderr.write(
                        'Unknowns provider %s.\n'
                        'Available providers are: %s.' %
                        (name, ' '.join(all_providers.keys())))
                    sys.exit(1)
        return providers

    def send(self, queue):
        """
        Serialize a list of test results and send them to remote server.
        """
        content = []
        for item in queue:
            content.append(item.serialize())
        data = json.dumps(content)
        headers = {}
        headers['content-type'] = 'application/json'
        url = 'http://%s:%s/api/tests/' % (self.args.server, self.args.port)
        try:
            response = requests.post(
                url,
                data=data,
                headers=headers,
                auth=(self.args.username, self.args.password),
            )
            if response.status_code != 201:
                logging.debug('Failed to send result (HTTP%s):',
                              response.status_code)
                if 'DOCTYPE' in response.text:
                    html_path = 'debug_%s.html' % rnd.regex('[a-z]{4}')
                    with open(html_path, 'w') as fp:
                        fp.write(response.text)
                    logging.debug('Html response saved to %s',
                                  os.path.abspath(html_path))
                else:
                    logging.debug(response.text)
        except requests.ConnectionError, detail:
            logging.debug('Failed to send result to server: %s', detail)

    def run_tests(self):
        while not self.exiting:
            item = random.choice(self.providers.values()).run_once()
            self.last_item = item
            self.send_queue.append(item)
            self._stat_result(item)
            if self.pause:
                while self.pause and not self.exiting:
                    time.sleep(0.5)

    def run(self):
        """
        Main loop to run tests and send/report tests results.
        """
        os.environ["EDITOR"] = "echo"
        last_thread = None
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.screen.keypad(1)
        self.screen.timeout(100)
        self.screen.refresh()

        self.last_item = None
        self.test_thread.start()

        try:
            while True:
                self._show_report()
                self._show_last_result()
                if last_thread:
                    last_thread.join()

                # Monitor key press
                ch = self.screen.getch()
                if ch == ord('q'):
                    break
                elif ch == ord('p'):
                    self.pause = not self.pause
                elif ch == ord('n'):
                    idx = self.stats.keys().index(self.cur_counter)
                    new_idx = (idx + 1) % len(self.stats)
                    self.cur_counter = self.stats.keys()[new_idx]
                elif ch == ord('N'):
                    idx = self.stats.keys().index(self.cur_counter)
                    new_idx = (idx - 1) % len(self.stats)
                    self.cur_counter = self.stats.keys()[new_idx]

                if len(self.send_queue) > 200:
                    send_thread = threading.Thread(
                        target=self.send,
                        args=(self.send_queue,)
                    )
                    send_thread.start()
                    last_thread = send_thread
                    self.send_queue = []
        except KeyboardInterrupt:
            pass
        finally:
            self.exiting = True
            self._show_exit()
            self.test_thread.join()
            curses.nocbreak()
            self.screen.keypad(0)
            curses.curs_set(1)
            curses.echo()
            curses.endwin()
