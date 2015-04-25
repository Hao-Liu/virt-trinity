from virtTrinity import picker
from virtTrinity.providers.virsh_cmd import data
from virtTrinity.providers.virsh_cmd.utils import virsh
from virtTrinity.providers.virsh_cmd.picker.command import CmdPicker


class OptSetPicker(picker.Picker):
    depends_on = CmdPicker
    data_type = data.OptSet()

    types = {
        "positive": {
            "patterns": None,
            "data_type": data.ValidOptSet(),
        },
        "miss_required": {
            "patterns": r"command '.*' requires .* option",
            "data_type": data.MissingRequiredOptSet(),
        },
        "exclusive": {
            "patterns": [
                r"Options .* and .* are mutually exclusive",
            ],
            "data_type": data.ExclusiveOptSet(),
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
