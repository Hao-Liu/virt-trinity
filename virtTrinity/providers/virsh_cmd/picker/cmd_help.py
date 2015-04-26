from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdHelpChecker


class CmdHelpCommandPicker(picker.Picker):
    depends_on = CmdHelpChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'command' in self.test.options

    def apply(self, res):
        self.test.options['command'] = res
