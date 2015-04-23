import re
import os
import string
import random

from virtTrinity import data
from virtTrinity.utils import rnd
from virtTrinity.utils import base

from virtTrinity.providers.virsh_cmd.utils import virsh
from virtTrinity.providers.virsh_cmd.utils import xml_gen


class VirshCmd(data.String):
    static_list = list(
        set(virsh.commands.keys()) -
        set(['qemu-monitor-event', 'event']))


class VirshOptSet(data.Data):
    def validate(self, obj):
        return (type(obj) is set and
                all([re.match(r'\w.*', i) for i in obj]))

    def generate(self):
        res = {}
        for _ in xrange(rnd.int_exp()):
            key = random.choice(
                string.ascii_letters + string.digits) + rnd.text()
            value = random.choice([rnd.text(), True])
            res[key] = value
        return res


class OptSet(VirshOptSet):
    def validate(self, obj):
        opts = virsh.commands[self._params['test'].cmd]['options']
        for opt_name in obj:
            if opt_name not in opts:
                return False

        for opt_name, opt in opts.items():
            if opt['required'] and opt_name not in obj:
                return False
        return True

    def generate(self):
        opts = virsh.commands[self._params['test'].cmd]['options']
        res = {}
        for name, opt in opts.items():
            if opt['required'] or random.random() < 0.3:
                if opt['type'] == 'bool':
                    res[name] = True
                elif opt['type'] == 'number':
                    res[name] = str(rnd.int_exp())
                else:
                    res[name] = rnd.text()
        return res


class MissingDepOptSet(VirshOptSet):
    def generate(self):
        cmd_name = self._params['test'].cmd
        opts = virsh.commands[cmd_name]['options']
        res = {}
        for name, opt in opts.items():
            if opt['required'] or random.random() < 0.3:
                if opt['type'] == 'bool':
                    res[name] = True
                elif opt['type'] == 'number':
                    res[name] = str(rnd.int_exp())
                else:
                    res[name] = rnd.text()

        requires = [opt_name
                    for opt_name, opt in opts.items()
                    if opt['required']]
        if not requires:
            raise ValueError(
                'Impossible generate missing dependence option set '
                'for command %s' % self._params['test'].cmd)
        else:
            cnt = rnd.int_exp(min_inc=1, max_inc=len(requires))
            choices = random.sample(requires, cnt)
            for choice in choices:
                del res[choice]
        return res

    def validate(self, obj):
        cmd_name = self._params['test'].cmd
        opts = virsh.commands[cmd_name]['options']
        for opt_name in obj:
            if opt_name not in opts:
                return False

        for opt_name, opt in opts.items():
            if opt['required'] and opt_name not in obj:
                return True
        return False


class XML(data.String):
    pass


class LibvirtXML(XML):
    def validate(self, obj):
        tmp_file = '/tmp/virt-trinity-validate.xml'
        with open(tmp_file, 'w') as fp:
            fp.write(obj)
        try:
            res = base.run('virt-xml-validate %s' % tmp_file)
            return not bool(res.exit_code)
        finally:
            try:
                os.remove(tmp_file)
            except IOError:
                pass


class DomainXML(LibvirtXML):
    def generate(self):
        return xml_gen.rnd_xml('domain')

    def validate(self, obj):
        tmp_file = '/tmp/virt-trinity-validate.xml'
        with open(tmp_file, 'w') as fp:
            fp.write(obj)
        try:
            res = base.run('virt-xml-validate %s domain' % tmp_file)
            return not bool(res.exit_code)
        finally:
            try:
                os.remove(tmp_file)
            except IOError:
                pass


class DomainType(data.String):
    static_list = [
        'qemu', 'kqemu', 'kvm', 'xen', 'lxc', 'uml',
        'openvz', 'test', 'vmware', 'hyperv', 'vbox',
        'phyp', 'parallels', 'bhyve']


class AvailDomainType(DomainType):
    static_list = ['qemu', 'kqemu', 'kvm', 'xen']


UNIT_MAP = {
    "b": 1,
    "byte": 1,
    "k": 1000**1,
    "m": 1000**2,
    "g": 1000**3,
    "t": 1000**4,
    "p": 1000**5,
    "e": 1000**6,
    "kb": 1000**1,
    "mb": 1000**2,
    "gb": 1000**3,
    "tb": 1000**4,
    "pb": 1000**5,
    "eb": 1000**6,
    "kib": 1024**1,
    "mib": 1024**2,
    "gib": 1024**3,
    "tib": 1024**4,
    "pib": 1024**5,
    "eib": 1024**6,
}


class MemorySize(data.Data):
    def generate(self):
        size = str(rnd.int_exp(min_inc=1, lambd=0.01))
        unit = random.choice(UNIT_MAP.keys())
        return size, unit

    def validate(self, obj):
        size, unit = obj
        return size.isdigit() and unit in UNIT_MAP


class ValidMemorySize(MemorySize):
    def generate(self):
        while True:
            size = str(rnd.int_exp(min_inc=1, lambd=0.01))
            unit = random.choice(UNIT_MAP.keys())
            if int(size) * UNIT_MAP[unit] < 0x8000000000:
                return size, unit

    def validate(self, obj):
        size, unit = obj
        return int(size) * UNIT_MAP[unit] < 0x8000000000


class Nodeset(data.String):
    def generate(self):
        return rnd.cpuset()

    def validate(self, obj):
        return False
