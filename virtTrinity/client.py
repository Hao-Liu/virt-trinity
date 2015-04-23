import re
import os
import sys
import json
import random
import logging
import requests
import argparse
import threading

from collections import Counter

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

    def _stat_result(self, item, counters, err_stat):
        """
        Categorizes and keep the count of a result of a test item depends on
        the expected failure patterns.
        """
        res = item.res
        fail_patts = item.fail_patts

        test_pattern = '#Failed to parse'
        if res:
            if res.exit_status == 'timeout':
                counters['timeout_cnt'] += 1
                print 'TIMEOUT:'
                res.pprint()

            if fail_patts:
                if res.exit_status == 'success':
                    counters['unexpected_pass_cnt'] += 1
                    print 'UNEXPECTED PASS: (Expect %s)' % fail_patts
                    res.pprint()
                elif res.exit_status == 'failure':
                    if any([re.search(p, res.stderr) for p in fail_patts]):
                        counters['expected_neg_cnt'] += 1
                    else:
                        counters['unexpected_neg_cnt'] += 1
                        print 'UNEXPECTED FAIL: (Expect %s)' % fail_patts
                        res.pprint()
            else:
                if res.exit_status == 'success':
                    counters['success_cnt'] += 1
                elif res.exit_status == 'failure':
                    err_stat[res.stderr] += 1
                    counters['failure_cnt'] += 1
                    if test_pattern in res.stderr:
                        item.pprint()
                        exit(0)
        else:
            counters['skip_cnt'] += 1

    def _report(self, counters, err_stat):
        """
        Print a simple statistics on results depends on the expected failure
        patterns.
        """
        cnt = counters["cnt"]
        skip_cnt = counters["skip_cnt"]
        failure_cnt = counters["failure_cnt"]
        success_cnt = counters["success_cnt"]
        timeout_cnt = counters["timeout_cnt"]
        expected_neg_cnt = counters["expected_neg_cnt"]
        unexpected_neg_cnt = counters["unexpected_neg_cnt"]
        unexpected_pass_cnt = counters["unexpected_pass_cnt"]
        print '\r' + "STATISTICS".center(80, '_')
        print "Success  : %.2f%% (%d/%d)" % (
            float(success_cnt) / cnt * 100,
            success_cnt, cnt)
        print "Failure  : %.2f%% (%d/%d)" % (
            float(failure_cnt) / cnt * 100,
            failure_cnt, cnt)
        print "Skipped  : %.2f%% (%d/%d)" % (
            float(skip_cnt) / cnt * 100,
            skip_cnt, cnt)
        print "ExpFail  : %.2f%% (%d/%d)" % (
            float(expected_neg_cnt) / cnt * 100,
            expected_neg_cnt, cnt)
        print "UnexpFail: %.2f%% (%d/%d)" % (
            float(unexpected_neg_cnt) / cnt * 100,
            unexpected_neg_cnt, cnt)
        print "UnexpPass: %.2f%% (%d/%d)" % (
            float(unexpected_pass_cnt) / cnt * 100,
            unexpected_pass_cnt, cnt)
        print "Timeout  : %.2f%% (%d/%d)" % (
            float(timeout_cnt) / cnt * 100,
            timeout_cnt, cnt)
        print "FREQUENT FAILS".center(80, '_')
        print "%6s%6s%68s" % ('COUNT', 'RATIO', 'STDERR'.center(68))
        for err, c in err_stat.most_common(30):
            print "%5d %6.2f" % (c, float(c) * 100 / failure_cnt),
            for idx, l in enumerate(err.splitlines()):
                if idx == 0:
                    print "\t" + l
                else:
                    print "\t\t" + l

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
        response = requests.post(
            url,
            data=data,
            headers=headers,
            auth=(self.args.username, self.args.password),
        )
        if response.status_code != 201:
            logging.error('Failed to send result (HTTP%s):',
                          response.status_code)
            if 'DOCTYPE' in response.text:
                html_path = 'debug_%s.html' % rnd.regex('[a-z]{4}')
                with open(html_path, 'w') as fp:
                    fp.write(response.text)
                logging.error('Html response saved to %s',
                              os.path.abspath(html_path))
            else:
                logging.error(response.text)

    def run(self):
        """
        Main loop to run tests and send/report tests results.
        """
        providers = self._process_providers()

        err_stat = Counter()
        counters = {
            "cnt": 0,
            "skip_cnt": 0,
            "failure_cnt": 0,
            "success_cnt": 0,
            "timeout_cnt": 0,
            "expected_neg_cnt": 0,
            "unexpected_neg_cnt": 0,
            "unexpected_pass_cnt": 0,
        }
        send_queue = []
        last_thread = None
        try:
            while True:
                item = random.choice(providers.values()).run_once()
                send_queue.append(item)

                self._stat_result(item, counters, err_stat)

                counters['cnt'] += 1
                cnt = counters['cnt']
                if cnt % 200 == 0 and cnt != 0:
                    self._report(counters, err_stat)
                    if last_thread:
                        last_thread.join()
                    send_thread = threading.Thread(
                        target=self.send,
                        args=(send_queue,)
                    )
                    send_thread.start()
                    last_thread = send_thread
                    send_queue = []
                else:
                    sys.stdout.write('\r%s\r' % cnt)
                    sys.stdout.flush()
        except KeyboardInterrupt:
            self._report(counters, err_stat)
            sys.exit(0)
