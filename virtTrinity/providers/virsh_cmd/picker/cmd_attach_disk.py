from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdAttachDiskChecker
from virtTrinity.providers.virsh_cmd import data


class CmdAttachDiskDomainPicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
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


class CmdAttachDiskTargetPicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'target' in self.test.options

    def apply(self, res):
        self.test.options['target'] = res


class CmdAttachDiskTargetbusPicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'targetbus' in self.test.options

    def apply(self, res):
        self.test.options['targetbus'] = res


class CmdAttachDiskTypePicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
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


class CmdAttachDiskCachePicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'cache' in self.test.options

    def apply(self, res):
        self.test.options['cache'] = res


class CmdAttachDiskDriverPicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'driver' in self.test.options

    def apply(self, res):
        self.test.options['driver'] = res


class CmdAttachDiskSubdriverPicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'subdriver' in self.test.options

    def apply(self, res):
        self.test.options['subdriver'] = res


class CmdAttachDiskSourcePicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'source' in self.test.options

    def apply(self, res):
        self.test.options['source'] = res


class CmdAttachDiskIothreadPicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'iothread' in self.test.options

    def apply(self, res):
        self.test.options['iothread'] = res


class CmdAttachDiskModePicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'mode' in self.test.options

    def apply(self, res):
        self.test.options['mode'] = res


class CmdAttachDiskSerialPicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'serial' in self.test.options

    def apply(self, res):
        self.test.options['serial'] = res


class CmdAttachDiskWwnPicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'wwn' in self.test.options

    def apply(self, res):
        self.test.options['wwn'] = res


class CmdAttachDiskAddressPicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'address' in self.test.options

    def apply(self, res):
        self.test.options['address'] = res


class CmdAttachDiskSourcetypePicker(picker.Picker):
    depends_on = CmdAttachDiskChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'sourcetype' in self.test.options

    def apply(self, res):
        self.test.options['sourcetype'] = res
