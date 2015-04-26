from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdChangeMediaChecker
from virtTrinity.providers.virsh_cmd import data


class CmdChangeMediaDomainPicker(picker.Picker):
    depends_on = CmdChangeMediaChecker
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


class CmdChangeMediaSourcePicker(picker.Picker):
    depends_on = CmdChangeMediaChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'source' in self.test.options

    def apply(self, res):
        self.test.options['source'] = res


class CmdChangeMediaPathPicker(picker.Picker):
    depends_on = CmdChangeMediaChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'path' in self.test.options

    def apply(self, res):
        self.test.options['path'] = res
