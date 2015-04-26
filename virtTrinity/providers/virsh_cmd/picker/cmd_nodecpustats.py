from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdNodecpustatsChecker


class CmdNodecpustatsCpuPicker(picker.Picker):
    depends_on = CmdNodecpustatsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'cpu' in self.test.options

    def apply(self, res):
        self.test.options['cpu'] = res
