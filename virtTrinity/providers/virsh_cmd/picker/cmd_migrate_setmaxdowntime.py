from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdMigrateSetmaxdowntimeChecker
from virtTrinity.providers.virsh_cmd import data


class CmdMigrateSetmaxdowntimeDomainPicker(picker.Picker):
    depends_on = CmdMigrateSetmaxdowntimeChecker
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


class CmdMigrateSetmaxdowntimeDowntimePicker(picker.Picker):
    depends_on = CmdMigrateSetmaxdowntimeChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'downtime' in self.test.options

    def apply(self, res):
        self.test.options['downtime'] = res
