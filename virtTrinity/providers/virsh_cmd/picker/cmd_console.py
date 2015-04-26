from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdConsoleChecker
from virtTrinity.providers.virsh_cmd import data


class CmdConsoleDomainPicker(picker.Picker):
    depends_on = CmdConsoleChecker
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


class CmdConsoleDevnamePicker(picker.Picker):
    depends_on = CmdConsoleChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'devname' in self.test.options

    def apply(self, res):
        self.test.options['devname'] = res
