from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdSecretSetValueChecker
from virtTrinity.providers.virsh_cmd import data


class CmdSecretSetValueSecretPicker(picker.Picker):
    depends_on = CmdSecretSetValueChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Secret(),
        },
    }

    def prerequisite(self):
        return 'secret' in self.test.options

    def apply(self, res):
        self.test.options['secret'] = res


class CmdSecretSetValueBase64Picker(picker.Picker):
    depends_on = CmdSecretSetValueChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'base64' in self.test.options

    def apply(self, res):
        self.test.options['base64'] = res
