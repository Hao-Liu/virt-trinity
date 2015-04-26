from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdVolNameChecker
from virtTrinity.providers.virsh_cmd import data


class CmdVolNameVolPicker(picker.Picker):
    depends_on = CmdVolNameChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.VolumePath(),
        },
    }

    def prerequisite(self):
        return 'vol' in self.test.options

    def apply(self, res):
        self.test.options['vol'] = res
