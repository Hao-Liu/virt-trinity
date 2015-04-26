from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdAttachInterfaceChecker
from virtTrinity.providers.virsh_cmd import data


class CmdAttachInterfaceDomainPicker(picker.Picker):
    depends_on = CmdAttachInterfaceChecker
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


class CmdAttachInterfaceMacPicker(picker.Picker):
    depends_on = CmdAttachInterfaceChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'mac' in self.test.options

    def apply(self, res):
        self.test.options['mac'] = res


class CmdAttachInterfaceOutboundPicker(picker.Picker):
    depends_on = CmdAttachInterfaceChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'outbound' in self.test.options

    def apply(self, res):
        self.test.options['outbound'] = res


class CmdAttachInterfaceTargetPicker(picker.Picker):
    depends_on = CmdAttachInterfaceChecker
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


class CmdAttachInterfaceScriptPicker(picker.Picker):
    depends_on = CmdAttachInterfaceChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'script' in self.test.options

    def apply(self, res):
        self.test.options['script'] = res


class CmdAttachInterfaceInboundPicker(picker.Picker):
    depends_on = CmdAttachInterfaceChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'inbound' in self.test.options

    def apply(self, res):
        self.test.options['inbound'] = res


class CmdAttachInterfaceTypePicker(picker.Picker):
    depends_on = CmdAttachInterfaceChecker
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


class CmdAttachInterfaceSourcePicker(picker.Picker):
    depends_on = CmdAttachInterfaceChecker
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


class CmdAttachInterfaceModelPicker(picker.Picker):
    depends_on = CmdAttachInterfaceChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'model' in self.test.options

    def apply(self, res):
        self.test.options['model'] = res
