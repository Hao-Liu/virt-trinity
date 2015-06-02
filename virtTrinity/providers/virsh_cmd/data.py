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
        set(['qemu-monitor-event', 'event', 'nodesuspend', 'undefine',
             'pool-undefine', 'net-undefine',
             'iface-bridge', 'iface-unbridge', 'iface-undefine',
             'vol-delete', 'vol-resize', 'vol-upload', 'vol-wipe',
             'nodedev-destroy', 'nodedev-detach', 'nodedev-reset',
             'secret-undefine', 'nwfilter-undefine',
             ]))


class OptSet(data.Data):
    def validate(self, obj):
        return (isinstance(obj, set) and
                all([re.match(r'\w.*', i) for i in obj]))

    def generate(self):
        res = {}
        for _ in xrange(rnd.int_exp()):
            key = random.choice(
                string.ascii_letters + string.digits) + rnd.text()
            value = random.choice([rnd.text(), True])
            res[key] = value
        return res


class ValidOptSet(OptSet):
    def validate(self, obj):
        cmd_name = self._params['test'].cmd
        opts = virsh.commands[cmd_name]['options']
        excs = virsh.commands[cmd_name]['exclusives']
        for opt_name in obj:
            if opt_name not in opts:
                return False

        for opt_name, opt in opts.items():
            if opt['required'] and opt_name not in obj:
                return False
        for exc_a, exc_b in excs:
            if exc_a in obj and exc_b in obj:
                return True
        return True

    def generate(self):
        cmd_name = self._params['test'].cmd
        opts = virsh.commands[cmd_name]['options']
        excs = virsh.commands[cmd_name]['exclusives']
        res = {}
        for name, opt in opts.items():
            if opt['required'] or random.random() < 0.3:
                if opt['type'] == 'bool':
                    res[name] = True
                elif opt['type'] == 'number':
                    res[name] = str(rnd.int_exp())
                else:
                    res[name] = rnd.text()
        for exc_a, exc_b in excs:
            if exc_a in res and exc_b in res:
                chosen_opt = random.choice([exc_a, exc_b])
                del res[chosen_opt]
        return res


class MissingRequiredOptSet(OptSet):
    def generate(self):
        cmd_name = self._params['test'].cmd
        opts = virsh.commands[cmd_name]['options']
        requires = [opt_name
                    for opt_name, opt in opts.items()
                    if opt['required']]
        if not requires:
            raise ValueError(
                'Impossible generate missing dependence option set '
                'for command %s' % cmd_name)

        res = {}
        for name, opt in opts.items():
            if opt['required'] or random.random() < 0.3:
                if opt['type'] == 'bool':
                    res[name] = True
                elif opt['type'] == 'number':
                    res[name] = str(rnd.int_exp())
                else:
                    res[name] = rnd.text()

        cnt = rnd.count(min_inc=1, max_inc=len(requires))
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


class ExclusiveOptSet(OptSet):
    def generate(self):
        cmd_name = self._params['test'].cmd
        opts = virsh.commands[cmd_name]['options']
        excs = virsh.commands[cmd_name]['exclusives']
        if not excs:
            raise ValueError('Impossible generate exclusive '
                             'option set for command %s' % cmd_name)
        res = {}
        for name, opt in opts.items():
            if opt['required'] or random.random() < 0.3:
                if opt['type'] == 'bool':
                    res[name] = True
                elif opt['type'] == 'number':
                    res[name] = str(rnd.int_exp())
                else:
                    res[name] = rnd.text()

        exc = random.choice(excs)
        for opt_name in exc:
            if opt_name not in res:
                opt = opts[opt_name]
                if opt['type'] == 'bool':
                    res[opt_name] = True
                elif opt['type'] == 'number':
                    res[opt_name] = str(rnd.int_exp())
                else:
                    res[opt_name] = rnd.text()
        return res

    def validate(self, obj):
        cmd_name = self._params['test'].cmd
        opts = virsh.commands[cmd_name]['options']
        excs = virsh.commands[cmd_name]['exclusives']
        for opt_name in obj:
            if opt_name not in opts:
                return False

        for exc_a, exc_b in excs:
            if exc_a in obj and exc_b in obj:
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


class SuspendTarget(data.String):
    static_list = ['mem', 'disk', 'hybrid']


class Domain(data.String):
    dynamic_list = staticmethod(virsh.domains)


class BlkIO(data.String):
    def generate(self):
        dom = self._params['test'].options['domain']
        cnt = rnd.count(min_inc=1)
        parts = []
        for _ in xrange(cnt):
            try:
                parts.append('/dev/' + random.choice(virsh.blkdevs(dom)))
            except IndexError:
                raise data.CanNotGenerateError('No valid blkdev for domain %s' % dom)
            parts.append(str(rnd.int_exp()))
        return ','.join(parts)

    def validate(self, obj):
        return False


class ActiveDomain(Domain):
    dynamic_list = staticmethod(virsh.active_domains)


class VolumePath(data.String):
    dynamic_list = staticmethod(virsh.all_volume_paths)


class Pool(data.String):
    dynamic_list = staticmethod(virsh.pools)


class Interface(data.String):
    dynamic_list = staticmethod(virsh.interfaces)


class Network(data.String):
    dynamic_list = staticmethod(virsh.networks)


class Secret(data.String):
    dynamic_list = staticmethod(virsh.secrets)


class NodeDevice(data.String):
    dynamic_list = staticmethod(virsh.node_devices)


class Snapshot(data.String):
    dynamic_list = staticmethod(virsh.all_snapshots)


class Nwfilter(data.String):
    dynamic_list = staticmethod(virsh.nwfilters)


class PoolVolumePair(data.Pair):
    def generate(self):
        pairs = []
        for pool in virsh.active_pools():
            for vol in virsh.volumes(pool):
                pairs.append((pool, vol))
        return random.choice(pairs)

    def validate(self, obj):
        pool, vol = obj
        if pool not in virsh.active_pools():
            return False
        return vol in virsh.volumes(pool)


class DomainSnapshotPair(data.Pair):
    def generate(self):
        pairs = []
        for dom in virsh.domains():
            for snapshot in virsh.snapshots(dom):
                pairs.append((dom, snapshot))

        if pairs:
            return random.choice(pairs)
        else:
            raise data.CanNotGenerateError('No valid domain-snapshot pairs')

    def validate(self, obj):
        dom, snapshot = obj
        if dom not in virsh.domains():
            return False
        return snapshot in virsh.snapshots(dom)


class DomainDiskPair(data.Pair):
    def generate(self):
        pairs = []
        for dom in virsh.domains():
            for blkdev in virsh.blkdevs(dom):
                pairs.append((dom, blkdev))
        return random.choice(pairs)

    def validate(self, obj):
        dom, blkdev = obj
        if dom not in virsh.domains():
            return False
        return blkdev in virsh.blkdevs(dom)


class ActiveDomainDiskPair(DomainDiskPair):
    def generate(self):
        pairs = []
        for dom in virsh.active_domains():
            for blkdev in virsh.blkdevs(dom):
                pairs.append((dom, blkdev))
        return random.choice(pairs)

    def validate(self, obj):
        dom, blkdev = obj
        if dom not in virsh.active_domains():
            return False
        return blkdev in virsh.blkdevs(dom)


class ActiveDomainActiveDiskPair(ActiveDomainDiskPair):
    def generate(self):
        pairs = []
        for dom in virsh.active_domains():
            for blkdev in virsh.blkdevs(dom):
                if virsh.blk_active(dom, blkdev):
                    pairs.append((dom, blkdev))
        return random.choice(pairs)

    def validate(self, obj):
        dom, blkdev = obj
        if dom not in virsh.active_domains():
            return False
        return blkdev in virsh.blkdevs(dom)
