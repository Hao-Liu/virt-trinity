from virtTrinity import picker
from virtTrinity.providers.virsh_cmd import data
from virtTrinity.providers.virsh_cmd.utils import virsh
from virtTrinity.providers.virsh_cmd.picker.command import CmdPicker


class OptSetPicker(picker.PickerBase):
    depends_on = CmdPicker
    data_type = data.VirshOptSet()

    types = {
        "positive": {
            "patterns": None,
            "data_type": data.OptSet(),
        },
        "miss_dep": {
            "patterns": r"command '.*' requires .* option",
            "data_type": data.MissingDepOptSet(),
        },
        "other": {
            "patterns": [
                r"command '.*' doesn't support option --.*",
                # r"command or command group '.*' doesn't exist",
            ]
        },
    }

    def prerequisite(self):
        return self.test.cmd in virsh.commands

    def apply(self, result):
        self.test.options = result
