from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdBlockcopyChecker
from virtTrinity.providers.virsh_cmd import data


class CmdBlockcopyDomainPicker(picker.Picker):
    depends_on = CmdBlockcopyChecker
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


class CmdBlockcopyXmlPicker(picker.Picker):
    depends_on = CmdBlockcopyChecker
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


class CmdBlockcopyFormatPicker(picker.Picker):
    depends_on = CmdBlockcopyChecker
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


class CmdBlockcopyDestPicker(picker.Picker):
    depends_on = CmdBlockcopyChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'dest' in self.test.options

    def apply(self, res):
        self.test.options['dest'] = res


class CmdBlockcopyBandwidthPicker(picker.Picker):
    depends_on = CmdBlockcopyChecker
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


class CmdBlockcopyBufSizePicker(picker.Picker):
    depends_on = CmdBlockcopyChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'buf-size' in self.test.options

    def apply(self, res):
        self.test.options['buf-size'] = res


class CmdBlockcopyTimeoutPicker(picker.Picker):
    depends_on = CmdBlockcopyChecker
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


class CmdBlockcopyPathPicker(picker.Picker):
    depends_on = CmdBlockcopyChecker
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


class CmdBlockcopyGranularityPicker(picker.Picker):
    depends_on = CmdBlockcopyChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.Integer(),
        },
    }

    def prerequisite(self):
        return 'granularity' in self.test.options

    def apply(self, res):
        self.test.options['granularity'] = res
