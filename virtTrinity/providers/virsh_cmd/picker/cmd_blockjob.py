from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdBlockjobChecker
from virtTrinity.providers.virsh_cmd import data


class CmdBlockjobDomainPicker(picker.Picker):
    depends_on = CmdBlockjobChecker
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


class CmdBlockjobBandwidthPicker(picker.Picker):
    depends_on = CmdBlockjobChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'bandwidth' in self.test.options

    def apply(self, res):
        self.test.options['bandwidth'] = res


class CmdBlockjobPathPicker(picker.Picker):
    depends_on = CmdBlockjobChecker
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
