from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdPoolStartChecker
from virtTrinity.providers.virsh_cmd import data


class CmdPoolStartPoolPicker(picker.Picker):
    depends_on = CmdPoolStartChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Pool(),
        },
    }

    def prerequisite(self):
        return 'vol' in self.test.options

    def apply(self, res):
        self.test.options['vol'] = res
