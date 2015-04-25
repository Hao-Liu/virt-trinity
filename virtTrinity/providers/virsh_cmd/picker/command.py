from virtTrinity import picker
from virtTrinity import data as common_data
from virtTrinity.providers.virsh_cmd import data


class CmdPicker(picker.Picker):
    depends_on = None
    # A command should never starts with a dash
    data_type = ~common_data.Option()

    types = {
        "positive": {
            "patterns": None,
            "data_type": data.VirshCmd(),
        },
        "other": {
            "patterns": [
                r"unknown command: '.*'",
                # These two errors are hard to classify and
                # are considered permeable.
                r"missing \"",
                r"dangling \\",
            ],
        }
    }

    def prerequisite(self):
        return True

    def apply(self, result):
        self.test.cmd = result
