from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdVolCreateAsChecker
from virtTrinity.providers.virsh_cmd import data


class CmdVolCreateAsPoolPicker(picker.Picker):
    depends_on = CmdVolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Pool(),
        },
    }

    def prerequisite(self):
        return 'vol' in self.test.options

    def apply(self, res):
        self.test.options['vol'] = res


class CmdVolCreateAsBackingVolPicker(picker.Picker):
    depends_on = CmdVolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'backing-vol' in self.test.options

    def apply(self, res):
        self.test.options['backing-vol'] = res


class CmdVolCreateAsCapacityPicker(picker.Picker):
    depends_on = CmdVolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'capacity' in self.test.options

    def apply(self, res):
        self.test.options['capacity'] = res


class CmdVolCreateAsNamePicker(picker.Picker):
    depends_on = CmdVolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'name' in self.test.options

    def apply(self, res):
        self.test.options['name'] = res


class CmdVolCreateAsFormatPicker(picker.Picker):
    depends_on = CmdVolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'format' in self.test.options

    def apply(self, res):
        self.test.options['format'] = res


class CmdVolCreateAsBackingVolFormatPicker(picker.Picker):
    depends_on = CmdVolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'backing-vol-format' in self.test.options

    def apply(self, res):
        self.test.options['backing-vol-format'] = res


class CmdVolCreateAsAllocationPicker(picker.Picker):
    depends_on = CmdVolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'allocation' in self.test.options

    def apply(self, res):
        self.test.options['allocation'] = res
