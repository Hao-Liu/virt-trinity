import os

from virtTrinity import picker
from virtTrinity import data as common_data

from virtTrinity.providers.virsh_cmd import data
from virtTrinity.providers.virsh_cmd.picker.optset import OptSetPicker


class CmdCdPicker(picker.PickerBase):
    depends_on = OptSetPicker
    types = {
        "non_interactive": {
            "patterns": "cd: command valid only in interactive mode",
            "data_type": None,
        }
    }

    def prerequisite(self):
        return self.test.cmd == 'cd'

    def apply(self, res):
        pass


class CmdDefineFilePicker(picker.PickerBase):
    depends_on = OptSetPicker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": common_data.RegularFile(),
        },
        "other": {
            "patterns": "No such file or directory",
        }
    }

    def prerequisite(self):
        return self.test.cmd == 'define' and 'file' in self.test.options

    def apply(self, res):
        if os.path.isfile(res):
            self.test.path = res
        self.test.options['file'] = res


class CmdQemuAttachPidPicker(picker.PickerBase):
    depends_on = OptSetPicker
    data_type = common_data.String()
    types = {
        "no_cmdline_pid": {
            "patterns": "no emulator path found",
            "data_type": common_data.ActiveKernelPID(),
        },
        "cmdline_pid": {
            "patterns": "No monitor connection for pid .*",
            "data_type": ~common_data.ActiveKernelPID(),
        },
        "non_exist_pid": {
            "patterns": "Failed to open file '/proc/.*/cmdline': No such file or directory",
            "data_type": ~common_data.ActivePID(),
        },
        "other": {
            "patterns": "missing pid value"
        },
    }

    def prerequisite(self):
        return self.test.cmd == 'qemu-attach' and 'pid' in self.test.options

    def apply(self, res):
        self.test.options['pid'] = res


class CmdDefineXMLPicker(picker.PickerBase):
    depends_on = OptSetPicker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.DomainXML(),
        },
        "other": {
            "patterns": "Failed to define domain from .*",
        }
    }

    def prerequisite(self):
        return self.test.cmd == 'define' and 'file' in self.test.options

    def apply(self, res):
        self.test.xml = res
