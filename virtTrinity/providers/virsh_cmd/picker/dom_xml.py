from xml.etree import ElementTree

from virtTrinity import picker
from virtTrinity import data as common_data
from virtTrinity.providers.virsh_cmd import data
from virtTrinity.providers.virsh_cmd.picker.option import CmdDefineXMLPicker


class DomainXMLTypePicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    picker_type = 'skipper'
    data_type = data.DomainType()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.AvailDomainType(),
        },
        "other": {
            "patterns": "unexpected domain type .*, expecting one of these: .*",
        }
    }

    def prerequisite(self):
        if isinstance(self.test.xml, ElementTree.Element):
            return self.test.xml.tag == 'domain'

    def checkpoint(self):
        return self.test.xml.get('type')


class DomainXMLMemSizePicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    data_type = data.MemorySize()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.ValidMemorySize(),
        },
        "other": {
            "patterns": "numerical overflow: value too large: .*",
        }
    }

    def prerequisite(self):
        return (
            isinstance(self.test.xml, ElementTree.Element) and
            self.test.xml.tag == 'domain' and
            self.test.xml.find('./memory') is not None
        )

    def apply(self, res):
        size, unit = res
        mem_xml = self.test.xml.find('./memory')
        mem_xml.set('unit', unit)
        mem_xml.text = size


class DomainXMLMaxMemoryPicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    data_type = data.MemorySize()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.ValidMemorySize(),
        },
        "other": {
            "patterns": "numerical overflow: value too large: .*",
        }
    }

    def prerequisite(self):
        return (
            isinstance(self.test.xml, ElementTree.Element) and
            self.test.xml.tag == 'domain' and
            self.test.xml.find('./maxMemory') is not None
        )

    def apply(self, res):
        size, unit = res
        mem_xml = self.test.xml.find('./maxMemory')
        mem_xml.set('unit', unit)
        mem_xml.text = size


class DomainXMLCurrentMemSizePicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    data_type = data.MemorySize()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.ValidMemorySize(),
        },
        "other": {
            "patterns": "numerical overflow: value too large: .*",
        }
    }

    def prerequisite(self):
        return (
            isinstance(self.test.xml, ElementTree.Element) and
            self.test.xml.tag == 'domain' and
            self.test.xml.find('./currentMemory') is not None
        )

    def apply(self, res):
        size, unit = res
        mem_xml = self.test.xml.find('./currentMemory')
        mem_xml.set('unit', unit)
        mem_xml.text = size


class DomainXMLMemoryBackingHugepagesNodesetPicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Nodeset(),
        },
        "other": {
            "patterns": "Failed to parse bitmap '.*'",
        }
    }

    def prerequisite(self):
        return (
            isinstance(self.test.xml, ElementTree.Element) and
            self.test.xml.tag == 'domain' and
            self.test.xml.find('./memoryBacking/hugepages/page') is not None
        )

    def apply_many(self, tp):
        for page_xml in self.test.xml.findall(
                './memoryBacking/hugepages/page'):
            page_xml.set('nodeset', tp.generate())


class DomainXMLCputuneVcpupinCpusetPicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Nodeset(),
        },
        "other": {
            "patterns": "Failed to parse bitmap '.*'",
        }
    }

    def prerequisite(self):
        return (
            isinstance(self.test.xml, ElementTree.Element) and
            self.test.xml.tag == 'domain' and
            self.test.xml.find('./cputune/vcpupin') is not None
        )

    def apply_many(self, tp):
        for page_xml in self.test.xml.findall('./cputune/vcpupin'):
            page_xml.set('cpuset', tp.generate())


class DomainXMLCputuneEmulatorpinCpusetPicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Nodeset(),
        },
        "other": {
            "patterns": "Failed to parse bitmap '.*'",
        }
    }

    def prerequisite(self):
        return (
            isinstance(self.test.xml, ElementTree.Element) and
            self.test.xml.tag == 'domain' and
            self.test.xml.find('./cputune/emulatorpin') is not None
        )

    def apply_many(self, tp):
        for page_xml in self.test.xml.findall('./cputune/emulatorpin'):
            page_xml.set('cpuset', tp.generate())


class DomainXMLCputuneIothreadpinCpusetPicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Nodeset(),
        },
        "other": {
            "patterns": "Failed to parse bitmap '.*'",
        }
    }

    def prerequisite(self):
        return (
            isinstance(self.test.xml, ElementTree.Element) and
            self.test.xml.tag == 'domain' and
            self.test.xml.find('./cputune/iothreadpin') is not None
        )

    def apply_many(self, tp):
        for page_xml in self.test.xml.findall('./cputune/iothreadpin'):
            page_xml.set('cpuset', tp.generate())


class DomainXMLVcpuCpusetPicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    data_type = common_data.String()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.Nodeset(),
        },
        "other": {
            "patterns": "Failed to parse bitmap '.*'",
        }
    }

    def prerequisite(self):
        return (
            isinstance(self.test.xml, ElementTree.Element) and
            self.test.xml.tag == 'domain' and
            self.test.xml.find('./vcpu') is not None
        )

    def apply(self, res):
        vcpu_xml = self.test.xml.find('./vcpu')
        vcpu_xml.set('cpuset', res)


class DomainXMLMemtuneHardLimitPicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    data_type = data.MemorySize()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.ValidMemorySize(),
        },
        "other": {
            "patterns": "numerical overflow: value too large: .*",
        }
    }

    def prerequisite(self):
        return (
            isinstance(self.test.xml, ElementTree.Element) and
            self.test.xml.tag == 'domain' and
            self.test.xml.find('./memtune/hard_limit') is not None
        )

    def apply(self, res):
        size, unit = res
        mem_xml = self.test.xml.find('./memtune/hard_limit')
        mem_xml.set('unit', unit)
        mem_xml.text = size


class DomainXMLMemtuneSoftLimitPicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    data_type = data.MemorySize()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.ValidMemorySize(),
        },
        "other": {
            "patterns": "numerical overflow: value too large: .*",
        }
    }

    def prerequisite(self):
        return (
            isinstance(self.test.xml, ElementTree.Element) and
            self.test.xml.tag == 'domain' and
            self.test.xml.find('./memtune/soft_limit') is not None
        )

    def apply(self, res):
        size, unit = res
        mem_xml = self.test.xml.find('./memtune/soft_limit')
        mem_xml.set('unit', unit)
        mem_xml.text = size


class DomainXMLMemtuneMinGuaranteePicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    data_type = data.MemorySize()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.ValidMemorySize(),
        },
        "other": {
            "patterns": "numerical overflow: value too large: .*",
        }
    }

    def prerequisite(self):
        return (
            isinstance(self.test.xml, ElementTree.Element) and
            self.test.xml.tag == 'domain' and
            self.test.xml.find('./memtune/min_guarantee') is not None
        )

    def apply(self, res):
        size, unit = res
        mem_xml = self.test.xml.find('./memtune/min_guarantee')
        mem_xml.set('unit', unit)
        mem_xml.text = size


class DomainXMLMemtuneSwapHardLimitPicker(picker.PickerBase):
    depends_on = CmdDefineXMLPicker
    data_type = data.MemorySize()
    types = {
        "positive": {
            "patterns": None,
            "data_type": data.ValidMemorySize(),
        },
        "other": {
            "patterns": "numerical overflow: value too large: .*",
        }
    }

    def prerequisite(self):
        return (
            isinstance(self.test.xml, ElementTree.Element) and
            self.test.xml.tag == 'domain' and
            self.test.xml.find('./memtune/swap_hard_limit') is not None
        )

    def apply(self, res):
        size, unit = res
        mem_xml = self.test.xml.find('./memtune/swap_hard_limit')
        mem_xml.set('unit', unit)
        mem_xml.text = size
