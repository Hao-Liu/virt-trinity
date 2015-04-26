from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDetachInterfaceChecker
from virtTrinity.providers.virsh_cmd import data


class CmdDetachInterfaceDomainPicker(picker.Picker):
    depends_on = CmdDetachInterfaceChecker
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


class CmdDetachInterfaceMacPicker(picker.Picker):
    depends_on = CmdDetachInterfaceChecker
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


class CmdDetachInterfaceTypePicker(picker.Picker):
    depends_on = CmdDetachInterfaceChecker
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
