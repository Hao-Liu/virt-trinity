from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdQemuAgentCommandChecker
from virtTrinity.providers.virsh_cmd import data


class CmdQemuAgentCommandDomainPicker(picker.Picker):
    depends_on = CmdQemuAgentCommandChecker
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


class CmdQemuAgentCommandTimeoutPicker(picker.Picker):
    depends_on = CmdQemuAgentCommandChecker
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


class CmdQemuAgentCommandCmdPicker(picker.Picker):
    depends_on = CmdQemuAgentCommandChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'cmd' in self.test.options

    def apply(self, res):
        self.test.options['cmd'] = res
