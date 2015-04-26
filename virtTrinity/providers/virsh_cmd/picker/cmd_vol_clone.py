from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdVolCloneChecker
from virtTrinity.providers.virsh_cmd import data


class CmdVolClonePoolVolumePairPicker(picker.Picker):
    depends_on = CmdVolCloneChecker
    data_type = common_data.Pair()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.PoolVolumePair(),
        },
    }

    def prerequisite(self):
        return 'vol' in self.test.options and 'pool' in self.test.options

    def apply(self, res):
        self.test.options['vol'], self.test.options['pool'] = res


class CmdVolCloneVolPicker(picker.Picker):
    depends_on = CmdVolCloneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.VolumePath(),
        },
    }

    def prerequisite(self):
        return 'vol' in self.test.options and 'pool' not in self.test.options

    def apply(self, res):
        self.test.options['vol'] = res


class CmdVolClonePoolPicker(picker.Picker):
    depends_on = CmdVolCloneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Pool(),
        },
    }

    def prerequisite(self):
        return 'vol' not in self.test.options and 'pool' in self.test.options

    def apply(self, res):
        self.test.options['pool'] = res


class CmdVolCloneNewnamePicker(picker.Picker):
    depends_on = CmdVolCloneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'newname' in self.test.options

    def apply(self, res):
        self.test.options['newname'] = res
