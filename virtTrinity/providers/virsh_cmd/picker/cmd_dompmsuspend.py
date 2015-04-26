from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDompmsuspendChecker
from virtTrinity.providers.virsh_cmd import data


class CmdDompmsuspendDomainPicker(picker.Picker):
    depends_on = CmdDompmsuspendChecker
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


class CmdDompmsuspendDurationPicker(picker.Picker):
    depends_on = CmdDompmsuspendChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'duration' in self.test.options

    def apply(self, res):
        self.test.options['duration'] = res


class CmdDompmsuspendTargetPicker(picker.Picker):
    depends_on = CmdDompmsuspendChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'target' in self.test.options

    def apply(self, res):
        self.test.options['target'] = res
