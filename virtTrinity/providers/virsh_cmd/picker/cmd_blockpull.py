from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdBlockpullChecker
from virtTrinity.providers.virsh_cmd import data


class CmdBlockpullDomainPicker(picker.Picker):
    depends_on = CmdBlockpullChecker
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


class CmdBlockpullBandwidthPicker(picker.Picker):
    depends_on = CmdBlockpullChecker
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


class CmdBlockpullBasePicker(picker.Picker):
    depends_on = CmdBlockpullChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'base' in self.test.options

    def apply(self, res):
        self.test.options['base'] = res


class CmdBlockpullTimeoutPicker(picker.Picker):
    depends_on = CmdBlockpullChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'timeout' in self.test.options

    def apply(self, res):
        self.test.options['timeout'] = res


class CmdBlockpullPathPicker(picker.Picker):
    depends_on = CmdBlockpullChecker
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
