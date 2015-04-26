from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdMigrateSetspeedChecker
from virtTrinity.providers.virsh_cmd import data


class CmdMigrateSetspeedDomainPicker(picker.Picker):
    depends_on = CmdMigrateSetspeedChecker
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


class CmdMigrateSetspeedBandwidthPicker(picker.Picker):
    depends_on = CmdMigrateSetspeedChecker
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
