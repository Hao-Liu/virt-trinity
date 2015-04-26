from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdSnapshotDumpxmlChecker
from virtTrinity.providers.virsh_cmd import data


class CmdSnapshotDumpxmlDomainSnapshotPairPicker(picker.Picker):
    depends_on = CmdSnapshotDumpxmlChecker
    data_type = common_data.Pair()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.DomainSnapshotPair(),
        },
    }

    def prerequisite(self):
        return 'domain' in self.test.options and 'snapshotname' in self.test.options

    def apply(self, res):
        self.test.options['domain'], self.test.options['snapshotname'] = res


class CmdSnapshotDumpxmlDomainPicker(picker.Picker):
    depends_on = CmdSnapshotDumpxmlChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Domain(),
        },
    }

    def prerequisite(self):
        return 'domain' in self.test.options and 'snapshotname' not in self.test.options

    def apply(self, res):
        self.test.options['domain'] = res


class CmdSnapshotDumpxmlSnapshotPicker(picker.Picker):
    depends_on = CmdSnapshotDumpxmlChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Snapshot(),
        },
    }

    def prerequisite(self):
        return 'domain' not in self.test.options and 'snapshotname' in self.test.options

    def apply(self, res):
        self.test.options['snapshotname'] = res
