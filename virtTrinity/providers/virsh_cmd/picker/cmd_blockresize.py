from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdBlockresizeChecker
from virtTrinity.providers.virsh_cmd import data


class CmdBlockresizeDomainPicker(picker.Picker):
    depends_on = CmdBlockresizeChecker
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


class CmdBlockresizePathPicker(picker.Picker):
    depends_on = CmdBlockresizeChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'path' in self.test.options

    def apply(self, res):
        self.test.options['path'] = res


class CmdBlockresizeSizePicker(picker.Picker):
    depends_on = CmdBlockresizeChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'size' in self.test.options

    def apply(self, res):
        self.test.options['size'] = res
