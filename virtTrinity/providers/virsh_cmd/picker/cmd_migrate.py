from virtTrinity import picker
from virtTrinity import data as common_data

# pylint: disable=no-name-in-module
from virtTrinity.providers.virsh_cmd.picker.cmds import CmdMigrateChecker
from virtTrinity.providers.virsh_cmd import data


class CmdMigrateDomainPicker(picker.Picker):
    depends_on = CmdMigrateChecker
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


class CmdMigrateXmlPicker(picker.Picker):
    depends_on = CmdMigrateChecker
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


class CmdMigrateDesturiPicker(picker.Picker):
    depends_on = CmdMigrateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'desturi' in self.test.options

    def apply(self, res):
        self.test.options['desturi'] = res


class CmdMigrateListenAddressPicker(picker.Picker):
    depends_on = CmdMigrateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'listen-address' in self.test.options

    def apply(self, res):
        self.test.options['listen-address'] = res


class CmdMigrateMigrateuriPicker(picker.Picker):
    depends_on = CmdMigrateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'migrateuri' in self.test.options

    def apply(self, res):
        self.test.options['migrateuri'] = res


class CmdMigrateTimeoutPicker(picker.Picker):
    depends_on = CmdMigrateChecker
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


class CmdMigrateDnamePicker(picker.Picker):
    depends_on = CmdMigrateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'dname' in self.test.options

    def apply(self, res):
        self.test.options['dname'] = res


class CmdMigrateGraphicsuriPicker(picker.Picker):
    depends_on = CmdMigrateChecker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.String(),
        },
    }

    def prerequisite(self):
        return 'graphicsuri' in self.test.options

    def apply(self, res):
        self.test.options['graphicsuri'] = res
