from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdPoolListChecker


class CmdPoolListTypePicker(picker.Picker):
    depends_on = CmdPoolListChecker
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
