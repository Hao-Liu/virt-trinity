from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdSendProcessSignalChecker
from virtTrinity.providers.virsh_cmd import data


class CmdSendProcessSignalDomainPicker(picker.Picker):
    depends_on = CmdSendProcessSignalChecker
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


class CmdSendProcessSignalPidPicker(picker.Picker):
    depends_on = CmdSendProcessSignalChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'pid' in self.test.options

    def apply(self, res):
        self.test.options['pid'] = res


class CmdSendProcessSignalSignamePicker(picker.Picker):
    depends_on = CmdSendProcessSignalChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'signame' in self.test.options

    def apply(self, res):
        self.test.options['signame'] = res
