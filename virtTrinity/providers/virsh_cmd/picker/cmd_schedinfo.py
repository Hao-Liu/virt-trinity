from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdSchedinfoChecker
from virtTrinity.providers.virsh_cmd import data


class CmdSchedinfoDomainPicker(picker.Picker):
    depends_on = CmdSchedinfoChecker
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


class CmdSchedinfoSetPicker(picker.Picker):
    depends_on = CmdSchedinfoChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'set' in self.test.options

    def apply(self, res):
        self.test.options['set'] = res


class CmdSchedinfoWeightPicker(picker.Picker):
    depends_on = CmdSchedinfoChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'weight' in self.test.options

    def apply(self, res):
        self.test.options['weight'] = res


class CmdSchedinfoCapPicker(picker.Picker):
    depends_on = CmdSchedinfoChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'cap' in self.test.options

    def apply(self, res):
        self.test.options['cap'] = res
