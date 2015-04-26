from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdMetadataChecker
from virtTrinity.providers.virsh_cmd import data


class CmdMetadataDomainPicker(picker.Picker):
    depends_on = CmdMetadataChecker
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


class CmdMetadataSetPicker(picker.Picker):
    depends_on = CmdMetadataChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'set' in self.test.options

    def apply(self, res):
        self.test.options['set'] = res


class CmdMetadataUriPicker(picker.Picker):
    depends_on = CmdMetadataChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'uri' in self.test.options

    def apply(self, res):
        self.test.options['uri'] = res


class CmdMetadataKeyPicker(picker.Picker):
    depends_on = CmdMetadataChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'key' in self.test.options

    def apply(self, res):
        self.test.options['key'] = res
