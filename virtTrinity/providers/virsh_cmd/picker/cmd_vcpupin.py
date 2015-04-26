from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdVcpupinChecker
from virtTrinity.providers.virsh_cmd import data


class CmdVcpupinDomainPicker(picker.Picker):
    depends_on = CmdVcpupinChecker
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


class CmdVcpupinCpulistPicker(picker.Picker):
    depends_on = CmdVcpupinChecker
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


class CmdVcpupinVcpuPicker(picker.Picker):
    depends_on = CmdVcpupinChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'vcpu' in self.test.options

    def apply(self, res):
        self.test.options['vcpu'] = res
