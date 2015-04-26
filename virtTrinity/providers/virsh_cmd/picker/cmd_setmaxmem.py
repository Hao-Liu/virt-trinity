from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdSetmaxmemChecker
from virtTrinity.providers.virsh_cmd import data


class CmdSetmaxmemDomainPicker(picker.Picker):
    depends_on = CmdSetmaxmemChecker
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


class CmdSetmaxmemSizePicker(picker.Picker):
    depends_on = CmdSetmaxmemChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'size' in self.test.options

    def apply(self, res):
        self.test.options['size'] = res
