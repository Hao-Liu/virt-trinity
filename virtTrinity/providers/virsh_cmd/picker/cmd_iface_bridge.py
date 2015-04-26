from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdIfaceBridgeChecker
from virtTrinity.providers.virsh_cmd import data


class CmdIfaceBridgeInterfacePicker(picker.Picker):
    depends_on = CmdIfaceBridgeChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Interface(),
        },
    }

    def prerequisite(self):
        return 'interface' in self.test.options

    def apply(self, res):
        self.test.options['interface'] = res


class CmdIfaceBridgeBridgePicker(picker.Picker):
    depends_on = CmdIfaceBridgeChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'bridge' in self.test.options

    def apply(self, res):
        self.test.options['bridge'] = res


class CmdIfaceBridgeDelayPicker(picker.Picker):
    depends_on = CmdIfaceBridgeChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'delay' in self.test.options

    def apply(self, res):
        self.test.options['delay'] = res
