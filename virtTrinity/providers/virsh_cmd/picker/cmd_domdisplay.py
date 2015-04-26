from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDomdisplayChecker
from virtTrinity.providers.virsh_cmd import data


class CmdDomdisplayDomainPicker(picker.Picker):
    depends_on = CmdDomdisplayChecker
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


class CmdDomdisplayTypePicker(picker.Picker):
    depends_on = CmdDomdisplayChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'type' in self.test.options

    def apply(self, res):
        self.test.options['type'] = res
