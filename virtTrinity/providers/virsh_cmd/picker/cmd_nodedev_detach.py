from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdNodedevDetachChecker
from virtTrinity.providers.virsh_cmd import data


class CmdNodedevDetachDevicePicker(picker.Picker):
    depends_on = CmdNodedevDetachChecker
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


class CmdNodedevDetachDriverPicker(picker.Picker):
    depends_on = CmdNodedevDetachChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'driver' in self.test.options

    def apply(self, res):
        self.test.options['driver'] = res
