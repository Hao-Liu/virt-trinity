from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdFindStoragePoolSourcesChecker


class CmdFindStoragePoolSourcesTypePicker(picker.Picker):
    depends_on = CmdFindStoragePoolSourcesChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'type' in self.test.options

    def apply(self, res):
        self.test.options['type'] = res


class CmdFindStoragePoolSourcesSrcspecPicker(picker.Picker):
    depends_on = CmdFindStoragePoolSourcesChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'srcSpec' in self.test.options

    def apply(self, res):
        self.test.options['srcSpec'] = res
