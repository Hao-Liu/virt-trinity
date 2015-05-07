from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdSnapshotInfoChecker
from virtTrinity.providers.virsh_cmd import data


class CmdSnapshotInfoDomainSnapshotPairPicker(picker.Picker):
    depends_on = CmdSnapshotInfoChecker
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


class CmdSnapshotInfoDomainPicker(picker.Picker):
    depends_on = CmdSnapshotInfoChecker
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


class CmdSnapshotInfoSnapshotPicker(picker.Picker):
    depends_on = CmdSnapshotInfoChecker
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