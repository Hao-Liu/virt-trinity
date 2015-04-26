from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdNetInfoChecker
from virtTrinity.providers.virsh_cmd import data


class CmdNetInfoNetworkPicker(picker.Picker):
    depends_on = CmdNetInfoChecker
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
