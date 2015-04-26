from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdNodeMemoryTuneChecker


class CmdNodeMemoryTuneShmSleepMillisecsPicker(picker.Picker):
    depends_on = CmdNodeMemoryTuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'shm-sleep-millisecs' in self.test.options

    def apply(self, res):
        self.test.options['shm-sleep-millisecs'] = res


class CmdNodeMemoryTuneShmMergeAcrossNodesPicker(picker.Picker):
    depends_on = CmdNodeMemoryTuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'shm-merge-across-nodes' in self.test.options

    def apply(self, res):
        self.test.options['shm-merge-across-nodes'] = res


class CmdNodeMemoryTuneShmPagesToScanPicker(picker.Picker):
    depends_on = CmdNodeMemoryTuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'shm-pages-to-scan' in self.test.options

    def apply(self, res):
        self.test.options['shm-pages-to-scan'] = res
