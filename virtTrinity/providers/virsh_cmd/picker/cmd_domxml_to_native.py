from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDomxmlToNativeChecker


class CmdDomxmlToNativeXmlPicker(picker.Picker):
    depends_on = CmdDomxmlToNativeChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'xml' in self.test.options

    def apply(self, res):
        self.test.options['xml'] = res


class CmdDomxmlToNativeFormatPicker(picker.Picker):
    depends_on = CmdDomxmlToNativeChecker
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
