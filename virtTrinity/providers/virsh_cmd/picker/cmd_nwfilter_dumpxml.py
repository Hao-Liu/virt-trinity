from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdNwfilterDumpxmlChecker
from virtTrinity.providers.virsh_cmd import data


class CmdNwfilterDumpxmlNwfilterPicker(picker.Picker):
    depends_on = CmdNwfilterDumpxmlChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Nwfilter(),
        },
    }

    def prerequisite(self):
        return 'nwfilter' in self.test.options

    def apply(self, res):
        self.test.options['nwfilter'] = res
