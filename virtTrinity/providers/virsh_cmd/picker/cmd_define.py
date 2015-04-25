import os

from virtTrinity import picker
from virtTrinity import data as common_data

from virtTrinity.providers.virsh_cmd import data
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDefineChecker


class CmdDefineFilePicker(picker.Picker):
    depends_on = CmdDefineChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.RegularFile(),
        },
        "other": {
            "patterns": "No such file or directory",
        }
    }

    def prerequisite(self):
        return 'file' in self.test.options

    def apply(self, res):
        if os.path.isfile(res):
            self.test.path = res
        self.test.options['file'] = res


class CmdDefineXMLPicker(picker.Picker):
    depends_on = CmdDefineFilePicker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.DomainXML(),
        },
        "other": {
            "patterns": "Failed to define domain from .*",
        }
    }

    def prerequisite(self):
        return self.test.cmd == 'define' and 'file' in self.test.options

    def apply(self, res):
        self.test.xml = res
