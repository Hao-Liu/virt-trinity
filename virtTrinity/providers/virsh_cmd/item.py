import os
from virtTrinity.utils import base
from xml.dom import minidom
from xml.etree import ElementTree


class Item(object):
    def __init__(self):
        self.cmd = ''
        self.xml = None
        self.options = {}
        self.path = None
        self.fail_patts = set()
        self.res = None

    def serialize(self):
        serial = {}
        serial['cmd'] = self.cmd
        serial['options'] = self.options
        serial['fail_patts'] = list(self.fail_patts)
        if self.xml is not None:
            if isinstance(self.xml, ElementTree.Element):
                serial['xml'] = ElementTree.tostring(self.xml)
            else:
                serial['xml'] = str(self.xml)
        if self.res:
            serial['cmdline'] = self.res.cmdline
            serial['stdout'] = self.res.stdout
            serial['stderr'] = self.res.stderr
            serial['exit_code'] = self.res.exit_code
            serial['exit_status'] = self.res.exit_status
            serial['call_time'] = self.res.call_time
        return serial

    def pre_process(self):
        if self.path:
            try:
                with open(self.path, 'w') as fp:
                    if isinstance(self.xml, ElementTree.Element):
                        fp.write(ElementTree.tostring(self.xml))
                    else:
                        fp.write(str(self.xml))
            except IOError:
                pass

    def post_process(self):
        if self.path:
            try:
                os.remove(self.path)
            except OSError:
                pass

    def run(self):
        self.pre_process()
        try:
            cmdline = 'virsh'
            cmdline += ' %s' % base.escape(self.cmd)
            for name, opt in self.options.items():
                name = base.escape(name)
                if opt is True:
                    cmdline += ' --%s' % name
                elif opt is False:
                    pass
                else:
                    opt = base.escape(opt)
                    cmdline += ' --%s' % name
                    cmdline += ' %s' % opt

            self.res = base.run(cmdline)
            return self.res
        finally:
            self.post_process()

    def pprint(self):
        if self.xml is not None:
            mxml = minidom.parseString(ElementTree.tostring(self.xml))
            mxml = minidom.parseString(
                ElementTree.tostring(self.xml.find('./cputune')))
            print mxml.toprettyxml()
        self.res.pprint()
