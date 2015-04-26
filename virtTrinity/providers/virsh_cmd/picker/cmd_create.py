from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdCreateChecker


class CmdCreateFilePicker(picker.Picker):
    depends_on = CmdCreateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.RegularFile(),
        },
    }

    def prerequisite(self):
        return 'file' in self.test.options

    def apply(self, res):
        self.test.options['file'] = res


class CmdCreatePassFdsPicker(picker.Picker):
    depends_on = CmdCreateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'pass-fds' in self.test.options

    def apply(self, res):
        self.test.options['pass-fds'] = res
