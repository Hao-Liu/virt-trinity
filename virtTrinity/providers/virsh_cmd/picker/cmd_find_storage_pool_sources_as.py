from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdFindStoragePoolSourcesAsChecker


class CmdFindStoragePoolSourcesAsInitiatorPicker(picker.Picker):
    depends_on = CmdFindStoragePoolSourcesAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'initiator' in self.test.options

    def apply(self, res):
        self.test.options['initiator'] = res


class CmdFindStoragePoolSourcesAsTypePicker(picker.Picker):
    depends_on = CmdFindStoragePoolSourcesAsChecker
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


class CmdFindStoragePoolSourcesAsHostPicker(picker.Picker):
    depends_on = CmdFindStoragePoolSourcesAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'host' in self.test.options

    def apply(self, res):
        self.test.options['host'] = res


class CmdFindStoragePoolSourcesAsPortPicker(picker.Picker):
    depends_on = CmdFindStoragePoolSourcesAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'port' in self.test.options

    def apply(self, res):
        self.test.options['port'] = res
