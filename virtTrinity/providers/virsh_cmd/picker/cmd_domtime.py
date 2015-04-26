from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDomtimeChecker
from virtTrinity.providers.virsh_cmd import data


class CmdDomtimeDomainPicker(picker.Picker):
    depends_on = CmdDomtimeChecker
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


class CmdDomtimeTimePicker(picker.Picker):
    depends_on = CmdDomtimeChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'time' in self.test.options

    def apply(self, res):
        self.test.options['time'] = res
