from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdNetDhcpLeasesChecker
from virtTrinity.providers.virsh_cmd import data


class CmdNetDhcpLeasesMacPicker(picker.Picker):
    depends_on = CmdNetDhcpLeasesChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'mac' in self.test.options

    def apply(self, res):
        self.test.options['mac'] = res


class CmdNetDhcpLeasesNetworkPicker(picker.Picker):
    depends_on = CmdNetDhcpLeasesChecker
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
