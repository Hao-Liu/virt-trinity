from virtTrinity import picker
from virtTrinity import data as common_data

from virtTrinity.providers.virsh_cmd import data
# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdNodesuspendChecker


class CmdNodesuspendTargetPicker(picker.Picker):
    depends_on = CmdNodesuspendChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.SuspendTarget(),
        },
        "other": {
            "patterns": "Invalid target",
        }
    }

    def prerequisite(self):
        return 'target' in self.test.options

    def apply(self, res):
        self.test.options['target'] = res
