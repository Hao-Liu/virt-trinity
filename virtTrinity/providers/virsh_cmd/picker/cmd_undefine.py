from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdUndefineChecker
from virtTrinity.providers.virsh_cmd import data


class CmdUndefineDomainPicker(picker.Picker):
    depends_on = CmdUndefineChecker
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


class CmdUndefineStoragePicker(picker.Picker):
    depends_on = CmdUndefineChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'storage' in self.test.options

    def apply(self, res):
        self.test.options['storage'] = res
