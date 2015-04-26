from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdNetUpdateChecker
from virtTrinity.providers.virsh_cmd import data


class CmdNetUpdateXmlPicker(picker.Picker):
    depends_on = CmdNetUpdateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'xml' in self.test.options

    def apply(self, res):
        self.test.options['xml'] = res


class CmdNetUpdateParentIndexPicker(picker.Picker):
    depends_on = CmdNetUpdateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'parent-index' in self.test.options

    def apply(self, res):
        self.test.options['parent-index'] = res


class CmdNetUpdateNetworkPicker(picker.Picker):
    depends_on = CmdNetUpdateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Network(),
        },
    }

    def prerequisite(self):
        return 'network' in self.test.options

    def apply(self, res):
        self.test.options['network'] = res


class CmdNetUpdateSectionPicker(picker.Picker):
    depends_on = CmdNetUpdateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'section' in self.test.options

    def apply(self, res):
        self.test.options['section'] = res


class CmdNetUpdateCommandPicker(picker.Picker):
    depends_on = CmdNetUpdateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'command' in self.test.options

    def apply(self, res):
        self.test.options['command'] = res
