from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdSnapshotCreateChecker
from virtTrinity.providers.virsh_cmd import data


class CmdSnapshotCreateDomainPicker(picker.Picker):
    depends_on = CmdSnapshotCreateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Domain(),
        },
    }

    def prerequisite(self):
        return 'domain' in self.test.options

    def apply(self, res):
        self.test.options['domain'] = res


class CmdSnapshotCreateXmlfilePicker(picker.Picker):
    depends_on = CmdSnapshotCreateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'xmlfile' in self.test.options

    def apply(self, res):
        self.test.options['xmlfile'] = res
