from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdVolDownloadChecker
from virtTrinity.providers.virsh_cmd import data


class CmdVolDownloadPoolVolumePairPicker(picker.Picker):
    depends_on = CmdVolDownloadChecker
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


class CmdVolDownloadVolPicker(picker.Picker):
    depends_on = CmdVolDownloadChecker
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


class CmdVolDownloadPoolPicker(picker.Picker):
    depends_on = CmdVolDownloadChecker
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


class CmdVolDownloadLengthPicker(picker.Picker):
    depends_on = CmdVolDownloadChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'length' in self.test.options

    def apply(self, res):
        self.test.options['length'] = res


class CmdVolDownloadFilePicker(picker.Picker):
    depends_on = CmdVolDownloadChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.RegularFile(),
        },
    }

    def prerequisite(self):
        return 'file' in self.test.options

    def apply(self, res):
        self.test.options['file'] = res


class CmdVolDownloadOffsetPicker(picker.Picker):
    depends_on = CmdVolDownloadChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'offset' in self.test.options

    def apply(self, res):
        self.test.options['offset'] = res
