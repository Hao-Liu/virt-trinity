from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdSecretGetValueChecker
from virtTrinity.providers.virsh_cmd import data


class CmdSecretGetValueSecretPicker(picker.Picker):
    depends_on = CmdSecretGetValueChecker
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
