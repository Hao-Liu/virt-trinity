from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDomcapabilitiesChecker


class CmdDomcapabilitiesMachinePicker(picker.Picker):
    depends_on = CmdDomcapabilitiesChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'machine' in self.test.options

    def apply(self, res):
        self.test.options['machine'] = res


class CmdDomcapabilitiesArchPicker(picker.Picker):
    depends_on = CmdDomcapabilitiesChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'arch' in self.test.options

    def apply(self, res):
        self.test.options['arch'] = res


class CmdDomcapabilitiesVirttypePicker(picker.Picker):
    depends_on = CmdDomcapabilitiesChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'virttype' in self.test.options

    def apply(self, res):
        self.test.options['virttype'] = res


class CmdDomcapabilitiesEmulatorbinPicker(picker.Picker):
    depends_on = CmdDomcapabilitiesChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'emulatorbin' in self.test.options

    def apply(self, res):
        self.test.options['emulatorbin'] = res
