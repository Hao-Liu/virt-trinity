from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdMemtuneChecker
from virtTrinity.providers.virsh_cmd import data


class CmdMemtuneDomainPicker(picker.Picker):
    depends_on = CmdMemtuneChecker
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


class CmdMemtuneMinGuaranteePicker(picker.Picker):
    depends_on = CmdMemtuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'min-guarantee' in self.test.options

    def apply(self, res):
        self.test.options['min-guarantee'] = res


class CmdMemtuneSwapHardLimitPicker(picker.Picker):
    depends_on = CmdMemtuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'swap-hard-limit' in self.test.options

    def apply(self, res):
        self.test.options['swap-hard-limit'] = res


class CmdMemtuneSoftLimitPicker(picker.Picker):
    depends_on = CmdMemtuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'soft-limit' in self.test.options

    def apply(self, res):
        self.test.options['soft-limit'] = res


class CmdMemtuneHardLimitPicker(picker.Picker):
    depends_on = CmdMemtuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'hard-limit' in self.test.options

    def apply(self, res):
        self.test.options['hard-limit'] = res
