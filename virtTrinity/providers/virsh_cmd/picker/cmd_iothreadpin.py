from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdIothreadpinChecker
from virtTrinity.providers.virsh_cmd import data


class CmdIothreadpinDomainPicker(picker.Picker):
    depends_on = CmdIothreadpinChecker
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


class CmdIothreadpinCpulistPicker(picker.Picker):
    depends_on = CmdIothreadpinChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'cpulist' in self.test.options

    def apply(self, res):
        self.test.options['cpulist'] = res


class CmdIothreadpinIothreadPicker(picker.Picker):
    depends_on = CmdIothreadpinChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'iothread' in self.test.options

    def apply(self, res):
        self.test.options['iothread'] = res
