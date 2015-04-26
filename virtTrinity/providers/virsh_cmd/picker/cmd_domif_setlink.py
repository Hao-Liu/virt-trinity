from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDomifSetlinkChecker
from virtTrinity.providers.virsh_cmd import data


class CmdDomifSetlinkDomainPicker(picker.Picker):
    depends_on = CmdDomifSetlinkChecker
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


class CmdDomifSetlinkStatePicker(picker.Picker):
    depends_on = CmdDomifSetlinkChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'state' in self.test.options

    def apply(self, res):
        self.test.options['state'] = res
