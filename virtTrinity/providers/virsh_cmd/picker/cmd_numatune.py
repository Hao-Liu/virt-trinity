from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdNumatuneChecker
from virtTrinity.providers.virsh_cmd import data


class CmdNumatuneDomainPicker(picker.Picker):
    depends_on = CmdNumatuneChecker
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


class CmdNumatuneModePicker(picker.Picker):
    depends_on = CmdNumatuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'mode' in self.test.options

    def apply(self, res):
        self.test.options['mode'] = res


class CmdNumatuneNodesetPicker(picker.Picker):
    depends_on = CmdNumatuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'nodeset' in self.test.options

    def apply(self, res):
        self.test.options['nodeset'] = res
