import os
import re
import types
import xml.etree.ElementTree as etree
import random
import logging

from virtTrinity.utils import rnd
from xml.sax import saxutils


class XMLError(Exception):
    pass


SCHEMAS_PATH = '/usr/share/libvirt/schemas'
MAX_DEEPTH = 100
OVERIDE_MAP = {
    "element": [
    ],
    "define": [
    ],
    "optional": [
    ],
    "attribute": [
        ("/domain/type", None, "domain_type"),
        ("/domain/os/type", r'/define[@name="archList"]/attribute', "arch_type"),
    ],
    "zeroOrMore": [
    ],
    "oneOrMore": [
    ],
    "data": [
    ],
    "choice": [
    ],
    "ref": [
    ],
    "empty": [
    ],
    "group": [
    ],
    "value": [
    ],
    "interleave": [
    ],
    "text": [
    ],
    "start": [
    ],
    "anyName": [
    ],
    "anyURI": [
    ],
}


class ProcessBase(object):

    def __init__(self):
        self.xml = None
        self.node = None
        self.cont = False
        self.name = ''
        self.parent = None
        self.nodetree = None
        self.node_path = None
        self.xml_path = None
        self.params = None
        self.cur_xml = None
        self.xml_stack = None
        self.choices = []

    def process(self, func_name, node, xml_path, node_path, params):
        self.xml_path = xml_path
        self.node_path = node_path
        self.params = params
        self.xml_stack = params['xml_stack']
        self.xml = self.xml_stack[0]
        self.cur_xml = self.xml_stack[-1]
        if len(self.xml_stack) > 1:
            self.parent = self.xml_stack[-2]
        self.node = node
        self.nodetree = params['nodetree']
        self.name = node.get('name')

        result = getattr(self, func_name)()

        return self.cont, result

    def go_on(self):
        self.cont = True


class ProcessAttribute(ProcessBase):

    def process(self, func_name, node, xml_path, node_path, params):
        _, result = super(ProcessAttribute, self).process(
            func_name, node, xml_path, node_path, params)

        if isinstance(result, types.StringType):
            self.cur_xml.set(self.name, result)
        elif result is not None:
            logging.error("Attribute should be a string, but %s found",
                          type(result))
        return self.cont, None

    def domain_type(self):
        if 'dom_types' in self.params:
            dom_types = self.params['dom_types']
        else:
            dom_types = ["qemu", "kvm", "xen"]
        return random.choice(dom_types)

    def arch_type(self):
        if 'archs' in self.params:
            arch_types = self.params['archs']
        else:
            arch_types = ["x86_64", "i686", "ppc64"]
        return random.choice(arch_types)


class ProcessChoice(ProcessBase):

    def process(self, func_name, node, xml_path, node_path, params):
        self.choices = []
        super(ProcessChoice, self).process(
            func_name, node, xml_path, node_path, params)

        if not self.choices:
            return self.cont, None

        choice = random.choice(self.choices)
        return self.cont, parse_node(choice, params=self.params)

    def os_type(self):
        if 'os_types' in self.params:
            os_types = self.params['os_types']
        else:
            os_types = ['hvm']
        return random.choice(os_types)


class ProcessValue(ProcessBase):

    def process(self, func_name, node, xml_path, node_path, params):
        _, result = super(ProcessValue, self).process(
            func_name, node, xml_path, node_path, params)
        if isinstance(result, types.StringType):
            self.cur_xml.text = result
        elif result is not None:
            logging.error("Attribute should be a string, but %s found",
                          type(result))
        return self.cont, None


def load_rng(file_name, is_root=True):
    xml_str = open(file_name).read()
    xml_str = re.sub(' xmlns="[^"]+"', '', xml_str, count=1)
    nodetree = etree.fromstring(xml_str)
    for node in nodetree.findall('./include'):
        rng_name = os.path.join(SCHEMAS_PATH, node.attrib['href'])
        nodetree.remove(node)
        for element in load_rng(rng_name, is_root=False):
            nodetree.insert(0, element)
    return nodetree if is_root else nodetree.getchildren()


def gen_node(nodename=None, xml_type='domain', params=None):
    nodetree = load_rng(os.path.join(SCHEMAS_PATH, xml_type + '.rng'))

    if nodename is None:
        node = nodetree.find("./start")
    else:
        node = nodetree.find("./define[@name='%s']" % nodename)

    if params is None:
        params = {}

    params.update({
        'xml_stack': [],
        'node_stack': [],
        'nodetree': nodetree,
    })
    return parse_node(node, params=params)


def process_overide(tag, xml_path, node_path, node, params):
    logging.debug('%s %s %s', tag, xml_path, node_path)
    if tag not in OVERIDE_MAP:
        raise XMLError('Unknown tag %s' % tag)

    cont = True
    result = None
    for xml_patt, node_patt, func_name in OVERIDE_MAP[tag]:
        if xml_patt is None or re.match('^' + xml_patt + '$', xml_path):
            if node_patt is None or re.match('^' + node_patt + '$', node_path):
                cls_name = 'Process' + tag.capitalize()
                process_instance = globals()[cls_name]()
                cont, result = process_instance.process(
                    func_name, node, xml_path, node_path, params)

    return cont, result


def parse_node(node, params=None):
    xml_stack = params['xml_stack']
    node_stack = params['node_stack']
    nodetree = params['nodetree']

    if len(xml_stack) > MAX_DEEPTH:
        return

    name = node.get('name')
    logging.debug('parsing %s', node.tag)

    xml_tags = [xml.tag for xml in xml_stack]
    if name is None:
        path_seg = node.tag
    else:
        path_seg = '%s[@name="%s"]' % (node.tag, name)
        xml_tags.append(name)

    if node.tag in ["start", "define"]:
        params['node_stack'] = [path_seg]
    else:
        params['node_stack'].append(path_seg)

    xml_path = '/' + '/'.join(xml_tags)
    node_path = '/' + '/'.join([tag for tag in node_stack])

    cont, result = process_overide(
        node.tag, xml_path, node_path, node, params)
    if cont is not True:
        return result

    subnodes = list(node)

    if node.tag in ["start", "define"]:
        if len(subnodes) == 1:
            return parse_node(subnodes[0], params)
        elif len(subnodes) > 1:
            result = None
            for subnode in subnodes:
                sgl_res = parse_node(subnode, params)
                if sgl_res is not None:
                    if result is not None:
                        logging.info("Duplicated result in <define>")
                    result = sgl_res
            return result
    elif node.tag == "ref":
        def_nodes = nodetree.findall('./define[@name="%s"]' % name)
        choices = []
        for def_node in def_nodes:
            if not len(def_node.findall('./notAllowed')):
                choices.append(def_node)
        if choices:
            return parse_node(random.choice(choices), params)
    elif node.tag == "element":
        if node.find('./anyName') is not None:
            name = rnd.text()
        if name is None:
            raise XMLError('Cannot find element name: %s' %
                           etree.tostring(node))
        element = etree.Element(name)
        if len(xml_stack):
            xml_stack[-1].append(element)
        xml_stack.append(element)
        for subnode in subnodes:
            sgl_res = parse_node(subnode, params)
            if isinstance(sgl_res, types.StringType):
                element.text = sgl_res
        if len(xml_stack) > 1:
            xml_stack.pop()
        return element
    elif node.tag == "attribute":
        if subnodes is not None:
            if subnodes:
                value = parse_node(subnodes[0], params)
            else:
                value = saxutils.escape(
                    rnd.text(),
                    entities={"'": "&apos;", "\"": "&quot;"}
                )
        else:
            value = 'anystring'
        if value is not None:
            xml_stack[-1].set(name, value)
    elif node.tag == "empty":
        pass
    elif node.tag == "optional":
        # TODO
        is_optional = random.random() < 1
        if is_optional:
            for subnode in subnodes:
                parse_node(subnode, params)
    elif node.tag == "interleave":
        if False:
            # TODO
            random.shuffle(subnodes)
        for subnode in subnodes:
            parse_node(subnode, params)
    elif node.tag == "data":
        return get_data(node)
    elif node.tag == "choice":
        choice = random.choice(node.getchildren())
        return parse_node(choice, params)
    elif node.tag == "group":
        for subnode in subnodes:
            parse_node(subnode, params)
    elif node.tag in ["zeroOrMore", "oneOrMore"]:
        if len(subnodes) > 1:
            logging.error("More than one subnodes when xOrMore")

        subnode = subnodes[0]
        min_cnt = 1 if node.tag == "oneOrMore" else 0
        cnt = int(random.expovariate(0.5)) + min_cnt
        for _ in xrange(cnt):
            parse_node(subnode, params)
    elif node.tag == "value":
        return node.text
    elif node.tag in ["text", 'anyName']:
        return saxutils.escape(
            rnd.text(),
            entities={"'": "&apos;", '"': "&quot;"}
        )
    elif node.tag == 'anyURI':
        return "qemu:///system"
    else:
        logging.error("Unhandled %s", node.tag)
        exit(1)


def get_data(node):
    data_type = node.get('type')
    if data_type in ['short', 'integer', 'int', 'long', 'unsignedShort',
                     'unsignedInt', 'unsignedLong', 'positiveInteger']:
        data_max = 100
        data_min = -100
        if data_type.startswith('unsigned'):
            data_min = 0
        elif data_type == 'positiveInteger':
            data_min = 1

        xml_min = node.findall("./param[@name='minInclusive']")
        xml_max = node.findall("./param[@name='maxInclusive']")
        if xml_min:
            data_min = int(xml_min[0].text)
        if xml_max:
            data_max = int(xml_max[0].text)
        return str(random.randint(data_min, data_max))
    elif data_type == 'double':
        return str(random.expovariate(0.1))
    elif data_type == 'dateTime':
        return "2014-12-25T00:00:01"
    elif data_type == 'NCName':
        return "NCName"
    elif data_type == 'string':
        pattern = node.findall("./param[@name='pattern']")
        pattern = pattern[0].text if pattern else None

        if data_type == 'string' and pattern is None:
            logging.info('None string found')
            return "NoneString"

        return rnd.regex(pattern)
    else:
        logging.error("Unhandled data type %s", data_type)


def rnd_xml(name='domain', params=None):
    xml = gen_node(xml_type=name, params=params)
    if name == 'domain':
        for elem in xml:
            if elem.tag in ['metadata', 'commandline']:
                xml.remove(elem)
    return xml
