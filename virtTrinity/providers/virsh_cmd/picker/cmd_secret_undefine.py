from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdSecretUndefineChecker
from virtTrinity.providers.virsh_cmd import data


class CmdSecretUndefineSecretPicker(picker.Picker):
    depends_on = CmdSecretUndefineChecker
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
