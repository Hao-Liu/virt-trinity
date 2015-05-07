from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdNodedevResetChecker
from virtTrinity.providers.virsh_cmd import data


class CmdNodedevResetDevicePicker(picker.Picker):
    depends_on = CmdNodedevResetChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.NodeDevice(),
        },
    }

    def prerequisite(self):
        return 'device' in self.test.options

    def apply(self, res):
        self.test.options['device'] = res