from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdPoolCreateAsChecker


class CmdPoolCreateAsSourceNamePicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'source-name' in self.test.options

    def apply(self, res):
        self.test.options['source-name'] = res


class CmdPoolCreateAsSourceFormatPicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'source-format' in self.test.options

    def apply(self, res):
        self.test.options['source-format'] = res


class CmdPoolCreateAsNamePicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
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


class CmdPoolCreateAsTypePicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
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


class CmdPoolCreateAsAuthUsernamePicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'auth-username' in self.test.options

    def apply(self, res):
        self.test.options['auth-username'] = res


class CmdPoolCreateAsSourcePathPicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'source-path' in self.test.options

    def apply(self, res):
        self.test.options['source-path'] = res


class CmdPoolCreateAsSourceDevPicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'source-dev' in self.test.options

    def apply(self, res):
        self.test.options['source-dev'] = res


class CmdPoolCreateAsAuthTypePicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'auth-type' in self.test.options

    def apply(self, res):
        self.test.options['auth-type'] = res


class CmdPoolCreateAsAdapterNamePicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'adapter-name' in self.test.options

    def apply(self, res):
        self.test.options['adapter-name'] = res


class CmdPoolCreateAsAdapterParentPicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'adapter-parent' in self.test.options

    def apply(self, res):
        self.test.options['adapter-parent'] = res


class CmdPoolCreateAsSourceHostPicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'source-host' in self.test.options

    def apply(self, res):
        self.test.options['source-host'] = res


class CmdPoolCreateAsAdapterWwnnPicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'adapter-wwnn' in self.test.options

    def apply(self, res):
        self.test.options['adapter-wwnn'] = res


class CmdPoolCreateAsSecretUsagePicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'secret-usage' in self.test.options

    def apply(self, res):
        self.test.options['secret-usage'] = res


class CmdPoolCreateAsAdapterWwpnPicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'adapter-wwpn' in self.test.options

    def apply(self, res):
        self.test.options['adapter-wwpn'] = res


class CmdPoolCreateAsTargetPicker(picker.Picker):
    depends_on = CmdPoolCreateAsChecker
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
