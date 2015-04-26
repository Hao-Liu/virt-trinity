from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdSendKeyChecker
from virtTrinity.providers.virsh_cmd import data


class CmdSendKeyDomainPicker(picker.Picker):
    depends_on = CmdSendKeyChecker
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


class CmdSendKeyHoldtimePicker(picker.Picker):
    depends_on = CmdSendKeyChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'holdtime' in self.test.options

    def apply(self, res):
        self.test.options['holdtime'] = res


class CmdSendKeyKeycodePicker(picker.Picker):
    depends_on = CmdSendKeyChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'keycode' in self.test.options

    def apply(self, res):
        self.test.options['keycode'] = res


class CmdSendKeyCodesetPicker(picker.Picker):
    depends_on = CmdSendKeyChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'codeset' in self.test.options

    def apply(self, res):
        self.test.options['codeset'] = res
