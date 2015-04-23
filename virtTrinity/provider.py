import os
import sys
import imp
import fnmatch
import inspect
import importlib

from virtTrinity import picker
from virtTrinity import providers


class Provider(object):
    def __init__(self, path):
        if not os.path.isdir(path):
            raise ValueError("%s is not a directory." % path)

        self.name = os.path.basename(path)
        self.path = path

        file_names = os.listdir(path)
        if '__init__.py' not in file_names:
            raise ValueError('__init__.py should exist in provider directory')

        file_names.remove('__init__.py')
        file_names.insert(0, '__init__.py')

        self.modules = {}
        for root, _, files in os.walk(path):
            relative_path = os.path.relpath(root, path)
            folders = os.path.split(relative_path)
            root_ns = '.'.join(
                [folder for folder in folders if folder not in ['', '.']])
            files.remove('__init__.py')
            files.insert(0, '__init__.py')
            for file_name in fnmatch.filter(files, '*.py'):
                mod_name, _ = os.path.splitext(file_name)
                if mod_name == '__init__':
                    mod_name = ''
                ns_list = [ns for ns in [self.name, root_ns, mod_name] if ns]
                mod_ns = '.'.join(ns_list)
                imp.load_source(mod_ns, os.path.join(root, file_name))
                self.modules[mod_ns] = importlib.import_module(mod_ns)

        mod_cls_map = {}

        for mod_name, cls_name in mod_cls_map.items():
            if mod_name not in self.modules:
                raise ValueError("Module %s doesn't exists in %s" %
                                 (mod_name, path))

            mod = self.modules[mod_name]

            if (not hasattr(mod, cls_name) or
                    not inspect.isclass(getattr(mod, cls_name))):
                raise ValueError("Module %s doesn't has class %s" %
                                 (mod_name, cls_name))

        self.Item = self.modules['%s.item' % self.name].Item
        self.picker_mod = self.modules['%s.picker' % self.name]
        self.picker_root = picker.setup_picker_tree(self.picker_mod)

    def run_once(self):
        item = self.Item()
        try:
            picker.pick(item, root=self.picker_root)
        except (picker.PickImpossibleError, picker.PickSkippedError), detail:
            try:
                return self.run_once()
            except RuntimeError:
                raise detail
        item.run()
        return item


def get_providers():
    providers_path = os.path.dirname(providers.__file__)
    sys.path.insert(0, providers_path)
    providers_dict = {}
    for subdir in os.listdir(providers_path):
        path = os.path.join(providers_path, subdir)
        if os.path.isdir(path):
            try:
                provider = Provider(path)
                providers_dict[provider.name] = provider
            except ValueError, detail:
                print "Skipped %s: %s" % (subdir, detail)
                continue
    return providers_dict
