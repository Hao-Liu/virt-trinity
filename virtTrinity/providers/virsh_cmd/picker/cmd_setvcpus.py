from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdSetvcpusChecker
from virtTrinity.providers.virsh_cmd import data


class CmdSetvcpusDomainPicker(picker.Picker):
    depends_on = CmdSetvcpusChecker
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


class CmdSetvcpusCountPicker(picker.Picker):
    depends_on = CmdSetvcpusChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'count' in self.test.options

    def apply(self, res):
        self.test.options['count'] = res
