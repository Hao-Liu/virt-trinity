from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDomfsthawChecker
from virtTrinity.providers.virsh_cmd import data


class CmdDomfsthawDomainPicker(picker.Picker):
    depends_on = CmdDomfsthawChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Domain(),
        },
    }

    def prerequisite(self):
        return 'domain' in self.test.options

    def apply(self, res):
        self.test.options['domain'] = res


class CmdDomfsthawMountpointPicker(picker.Picker):
    depends_on = CmdDomfsthawChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'mountpoint' in self.test.options

    def apply(self, res):
        self.test.options['mountpoint'] = res
