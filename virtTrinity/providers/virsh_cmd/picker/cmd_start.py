from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdStartChecker
from virtTrinity.providers.virsh_cmd import data


class CmdStartDomainPicker(picker.Picker):
    depends_on = CmdStartChecker
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


class CmdStartPassFdsPicker(picker.Picker):
    depends_on = CmdStartChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'pass-fds' in self.test.options

    def apply(self, res):
        self.test.options['pass-fds'] = res
