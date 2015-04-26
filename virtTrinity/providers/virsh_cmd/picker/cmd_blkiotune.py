from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdBlkiotuneChecker
from virtTrinity.providers.virsh_cmd import data


class CmdBlkiotuneDomainPicker(picker.Picker):
    depends_on = CmdBlkiotuneChecker
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


class CmdBlkiotuneDeviceReadIopsSecPicker(picker.Picker):
    depends_on = CmdBlkiotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'device-read-iops-sec' in self.test.options

    def apply(self, res):
        self.test.options['device-read-iops-sec'] = res


class CmdBlkiotuneDeviceWeightsPicker(picker.Picker):
    depends_on = CmdBlkiotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'device-weights' in self.test.options

    def apply(self, res):
        self.test.options['device-weights'] = res


class CmdBlkiotuneWeightPicker(picker.Picker):
    depends_on = CmdBlkiotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'weight' in self.test.options

    def apply(self, res):
        self.test.options['weight'] = res


class CmdBlkiotuneDeviceWriteIopsSecPicker(picker.Picker):
    depends_on = CmdBlkiotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'device-write-iops-sec' in self.test.options

    def apply(self, res):
        self.test.options['device-write-iops-sec'] = res


class CmdBlkiotuneDeviceReadBytesSecPicker(picker.Picker):
    depends_on = CmdBlkiotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'device-read-bytes-sec' in self.test.options

    def apply(self, res):
        self.test.options['device-read-bytes-sec'] = res


class CmdBlkiotuneDeviceWriteBytesSecPicker(picker.Picker):
    depends_on = CmdBlkiotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'device-write-bytes-sec' in self.test.options

    def apply(self, res):
        self.test.options['device-write-bytes-sec'] = res
