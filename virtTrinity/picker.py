import sys
import random
import logging
import inspect


class PickerError(Exception):
    pass


class PickImpossibleError(PickerError):
    pass


class PickSkippedError(PickerError):
    pass


class PickerBase(object):
    picker_type = 'selector'
    types = {}
    data_type = None

    def __init__(self, test):
        self.test = test
        for tp in self.types.values():
            params = {'test': self.test}
            try:
                tp['data_type'].set_params(params)
            except (KeyError, AttributeError):
                pass

    def prerequisite(self):
        cls_name = self.__class__.__name__
        name = inspect.stack()[0][3]
        raise NotImplementedError(
            "Method '%s' should be implemented for class '%s'" %
            (name, cls_name))

    def apply(self, _):
        cls_name = self.__class__.__name__
        name = inspect.stack()[0][3]
        raise NotImplementedError(
            "Method '%s' should be implemented for class '%s'" %
            (name, cls_name))

    def apply_many(self, _):
        cls_name = self.__class__.__name__
        name = inspect.stack()[0][3]
        raise NotImplementedError(
            "Method '%s' should be implemented for class '%s'" %
            (name, cls_name))

    def checkpoint(self):
        cls_name = self.__class__.__name__
        name = inspect.stack()[0][3]
        raise NotImplementedError(
            "Method '%s' should be implemented for class '%s'" %
            (name, cls_name))

    def pick(self, positive_weight=0.999):
        types = self.types.keys()
        if not types:
            raise ValueError("Property 'types' is not set for %s" %
                             self.__class__.__name__)

        # Weighted pick to favor positive result
        if 'positive' in types and random.random() < positive_weight:
            chosen_type = 'positive'
        else:
            chosen_type = random.choice(types)

        logging.debug('Chosen type is %s', chosen_type)

        # Get chosen data type instance and failure patterns.
        if chosen_type == 'other':
            data_type = self.data_type
            for type_name, tp in self.types.items():
                if type_name != 'other':
                    data_type -= tp['data_type']
        else:
            try:
                data_type = self.types[chosen_type]['data_type']
            except KeyError:
                raise KeyError(
                    "Type '%s' don't have 'data_type' in class '%s'" %
                    (chosen_type, self.__class__.__name__))
        fail_patts = self.types[chosen_type]['patterns']

        # Apply result according to picker's type
        if self.picker_type == 'selector':
            try:
                if data_type:
                    res = data_type.generate()
                else:
                    res = None
            except ValueError, detail:
                raise PickImpossibleError(
                    "Can't generate data. Picking is impossible: %s" %
                    detail)
            try:
                self.apply(res)
            except NotImplementedError:
                pass
            try:
                self.apply_many(data_type)
            except NotImplementedError:
                pass
        elif self.picker_type == 'skipper':
            if not data_type.validate(self.checkpoint()):
                raise PickSkippedError("Picker skipped")
        return fail_patts


def pick(item, root=None):
    picker_classes = {root.__name__: root}
    logging.debug('Start picking')
    while True:
        logging.debug('Current %s pickers: %s', len(picker_classes), picker_classes)
        picked_count = 0
        for name, picker_class in picker_classes.items():
            picker = picker_class(item)
            match = picker.prerequisite()
            if match:
                picked_count += 1
                fail_patt = picker.pick()
                if fail_patt:
                    if type(fail_patt) == str:
                        item.fail_patts.add(fail_patt)
                    elif type(fail_patt) == list:
                        item.fail_patts |= set(fail_patt)
                del picker_classes[name]
                if hasattr(picker_class, 'children'):
                    for c_name, c_picker in picker_class.children.items():
                        picker_classes[c_name] = c_picker
        logging.debug('Picked %d from %d', picked_count, len(picker_classes))
        if picked_count == 0:
            break


def setup_picker_tree(module):
    def _picker_predicate(member):
        return inspect.isclass(member) and member.__name__.endswith('Picker')

    pickers = dict(
        inspect.getmembers(sys.modules[module.__name__],
                           predicate=_picker_predicate))

    logging.debug('Found %s pickers: %s', len(pickers), pickers)

    root = pickers[module.root_picker]

    for name, picker in pickers.items():
        parent = picker.depends_on
        if parent is None:
            if name != root.__name__:
                raise ValueError('Non-root picker %s has no parent' % name)
        else:
            if hasattr(parent, 'children'):
                parent.children[name] = picker
            else:
                setattr(parent, 'children', {name: picker})
    return root
