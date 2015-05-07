from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdBlkdeviotuneChecker
from virtTrinity.providers.virsh_cmd import data


class CmdBlkdeviotuneDomainPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
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


class CmdBlkdeviotuneReadBytesSecMaxPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'read-bytes-sec-max' in self.test.options

    def apply(self, res):
        self.test.options['read-bytes-sec-max'] = res


class CmdBlkdeviotuneTotalIopsSecPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'total-iops-sec' in self.test.options

    def apply(self, res):
        self.test.options['total-iops-sec'] = res


class CmdBlkdeviotuneWriteIopsSecPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'write-iops-sec' in self.test.options

    def apply(self, res):
        self.test.options['write-iops-sec'] = res


class CmdBlkdeviotuneReadBytesSecPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'read-bytes-sec' in self.test.options

    def apply(self, res):
        self.test.options['read-bytes-sec'] = res


class CmdBlkdeviotuneReadIopsSecMaxPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'read-iops-sec-max' in self.test.options

    def apply(self, res):
        self.test.options['read-iops-sec-max'] = res


class CmdBlkdeviotuneTotalIopsSecMaxPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'total-iops-sec-max' in self.test.options

    def apply(self, res):
        self.test.options['total-iops-sec-max'] = res


class CmdBlkdeviotuneWriteBytesSecMaxPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'write-bytes-sec-max' in self.test.options

    def apply(self, res):
        self.test.options['write-bytes-sec-max'] = res


class CmdBlkdeviotuneWriteIopsSecMaxPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'write-iops-sec-max' in self.test.options

    def apply(self, res):
        self.test.options['write-iops-sec-max'] = res


class CmdBlkdeviotuneReadIopsSecPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'read-iops-sec' in self.test.options

    def apply(self, res):
        self.test.options['read-iops-sec'] = res


class CmdBlkdeviotuneWriteBytesSecPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'write-bytes-sec' in self.test.options

    def apply(self, res):
        self.test.options['write-bytes-sec'] = res


class CmdBlkdeviotuneTotalBytesSecMaxPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'total-bytes-sec-max' in self.test.options

    def apply(self, res):
        self.test.options['total-bytes-sec-max'] = res


class CmdBlkdeviotuneTotalBytesSecPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'total-bytes-sec' in self.test.options

    def apply(self, res):
        self.test.options['total-bytes-sec'] = res


class CmdBlkdeviotuneSizeIopsSecPicker(picker.Picker):
    depends_on = CmdBlkdeviotuneChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'size-iops-sec' in self.test.options

    def apply(self, res):
        self.test.options['size-iops-sec'] = res