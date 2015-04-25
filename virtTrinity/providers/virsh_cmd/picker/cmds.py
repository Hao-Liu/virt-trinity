import os

from virtTrinity import picker

from virtTrinity.providers.virsh_cmd.utils import virsh
from virtTrinity.providers.virsh_cmd.picker.optset import OptSetPicker


class CmdCdChecker(picker.Checker):
    depends_on = OptSetPicker
    types = {
        "non_interactive": {
            "patterns": "cd: command valid only in interactive mode",
            "data_type": None,
        }
    }

    def prerequisite(self):
        return self.test.cmd == 'cd'

    def predict(self):
        return 'non_interactive'


class CmdIfaceBeginChecker(picker.Checker):
    depends_on = OptSetPicker
    types = {
        "positive": {
            "patterns": None,
        },
        "already-began": {
            "patterns": "There is already an open transaction",
        },
    }

    def prerequisite(self):
        return self.test.cmd == 'iface-begin'

    def predict(self):
        snapshot_path = '/var/lib/netcf/network-snapshot'
        if os.path.exists(snapshot_path):
            return 'already-began'
        else:
            return 'positive'


class CmdIfaceCommitChecker(picker.Checker):
    depends_on = OptSetPicker
    types = {
        "positive": {
            "patterns": None,
        },
        "not-began": {
            "patterns": "No pending transaction to commit",
        },
    }

    def prerequisite(self):
        return self.test.cmd == 'iface-commit'

    def predict(self):
        snapshot_path = '/var/lib/netcf/network-snapshot'
        if os.path.exists(snapshot_path):
            return 'positive'
        else:
            return 'not-began'


class CmdIfaceRollbackChecker(picker.Checker):
    depends_on = OptSetPicker
    types = {
        "positive": {
            "patterns": None,
        },
        "not-began": {
            "patterns": "No pending transaction to rollback",
        },
    }

    def prerequisite(self):
        return self.test.cmd == 'iface-rollback'

    def predict(self):
        snapshot_path = '/var/lib/netcf/network-snapshot'
        if os.path.exists(snapshot_path):
            return 'positive'
        else:
            return 'not-began'

# Generate command checker for every virsh commands
for cmd in virsh.commands:
    cls_name = 'Cmd%sChecker' % ''.join([s.capitalize() for s in cmd.split('-')]).encode()
    if cls_name not in globals():
        bases = (picker.Checker,)
        attrs = {
            'depends_on': OptSetPicker,
            'types': {
                "positive": {
                    "patterns": None,
                },
            },
            'prerequisite': lambda x, cmd=cmd: x.test.cmd == cmd,
            'predict': lambda x: 'positive',
            'test': cmd,
        }
        cls = type(cls_name, bases, attrs)
        globals()[cls_name] = cls
