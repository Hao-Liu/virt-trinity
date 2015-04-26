from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDomifaddrChecker
from virtTrinity.providers.virsh_cmd import data


class CmdDomifaddrDomainPicker(picker.Picker):
    depends_on = CmdDomifaddrChecker
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


class CmdDomifaddrSourcePicker(picker.Picker):
    depends_on = CmdDomifaddrChecker
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
