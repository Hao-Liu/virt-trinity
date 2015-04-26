from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdDomiftuneChecker
from virtTrinity.providers.virsh_cmd import data


class CmdDomiftuneDomainPicker(picker.Picker):
    depends_on = CmdDomiftuneChecker
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


class CmdDomiftuneOutboundPicker(picker.Picker):
    depends_on = CmdDomiftuneChecker
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


class CmdDomiftuneInboundPicker(picker.Picker):
    depends_on = CmdDomiftuneChecker
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
