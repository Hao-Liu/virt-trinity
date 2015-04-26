from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdSnapshotCreateAsChecker
from virtTrinity.providers.virsh_cmd import data


class CmdSnapshotCreateAsDomainPicker(picker.Picker):
    depends_on = CmdSnapshotCreateAsChecker
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


class CmdSnapshotCreateAsMemspecPicker(picker.Picker):
    depends_on = CmdSnapshotCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'memspec' in self.test.options

    def apply(self, res):
        self.test.options['memspec'] = res


class CmdSnapshotCreateAsNamePicker(picker.Picker):
    depends_on = CmdSnapshotCreateAsChecker
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


class CmdSnapshotCreateAsDiskspecPicker(picker.Picker):
    depends_on = CmdSnapshotCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'diskspec' in self.test.options

    def apply(self, res):
        self.test.options['diskspec'] = res


class CmdSnapshotCreateAsDescriptionPicker(picker.Picker):
    depends_on = CmdSnapshotCreateAsChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'description' in self.test.options

    def apply(self, res):
        self.test.options['description'] = res
