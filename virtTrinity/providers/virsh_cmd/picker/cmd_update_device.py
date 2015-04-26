from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdUpdateDeviceChecker
from virtTrinity.providers.virsh_cmd import data


class CmdUpdateDeviceDomainPicker(picker.Picker):
    depends_on = CmdUpdateDeviceChecker
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


class CmdUpdateDeviceFilePicker(picker.Picker):
    depends_on = CmdUpdateDeviceChecker
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
