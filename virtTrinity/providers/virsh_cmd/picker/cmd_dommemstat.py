from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDommemstatChecker
from virtTrinity.providers.virsh_cmd import data


class CmdDommemstatDomainPicker(picker.Picker):
    depends_on = CmdDommemstatChecker
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


class CmdDommemstatPeriodPicker(picker.Picker):
    depends_on = CmdDommemstatChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'period' in self.test.options

    def apply(self, res):
        self.test.options['period'] = res
