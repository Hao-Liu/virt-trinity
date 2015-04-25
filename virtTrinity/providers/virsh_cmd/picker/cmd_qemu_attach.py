from virtTrinity import picker
from virtTrinity import data as common_data

from virtTrinity.providers.virsh_cmd.picker.cmds import CmdQemuAttachChecker


class CmdQemuAttachPidPicker(picker.Picker):
    depends_on = CmdQemuAttachChecker
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
