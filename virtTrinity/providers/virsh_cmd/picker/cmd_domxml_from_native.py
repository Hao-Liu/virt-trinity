from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDomxmlFromNativeChecker


class CmdDomxmlFromNativeConfigPicker(picker.Picker):
    depends_on = CmdDomxmlFromNativeChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'config' in self.test.options

    def apply(self, res):
        self.test.options['config'] = res


class CmdDomxmlFromNativeFormatPicker(picker.Picker):
    depends_on = CmdDomxmlFromNativeChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'format' in self.test.options

    def apply(self, res):
        self.test.options['format'] = res
