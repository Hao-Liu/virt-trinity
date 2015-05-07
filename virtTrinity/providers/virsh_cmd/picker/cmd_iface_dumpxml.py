from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdIfaceDumpxmlChecker
from virtTrinity.providers.virsh_cmd import data


class CmdIfaceDumpxmlInterfacePicker(picker.Picker):
    depends_on = CmdIfaceDumpxmlChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Interface(),
        },
    }

    def prerequisite(self):
        return 'interface' in self.test.options

    def apply(self, res):
        self.test.options['interface'] = res