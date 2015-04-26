from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdNetEventChecker
from virtTrinity.providers.virsh_cmd import data


class CmdNetEventEventPicker(picker.Picker):
    depends_on = CmdNetEventChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'event' in self.test.options

    def apply(self, res):
        self.test.options['event'] = res


class CmdNetEventNetworkPicker(picker.Picker):
    depends_on = CmdNetEventChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Network(),
        },
    }

    def prerequisite(self):
        return 'network' in self.test.options

    def apply(self, res):
        self.test.options['network'] = res


class CmdNetEventTimeoutPicker(picker.Picker):
    depends_on = CmdNetEventChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'timeout' in self.test.options

    def apply(self, res):
        self.test.options['timeout'] = res
