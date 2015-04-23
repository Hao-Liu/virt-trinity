import re
import os
import json
import logging
import subprocess

from virtTrinity import data_dir


def option_from_line(line):
    option = {'required': False, 'argv': False}
    name, type_name, _ = [i.strip() for i in line.split(' ', 2)]

    if name.startswith('[') and name.endswith(']'):
        name = name[1:-1]
        option['required'] = True

    if name.startswith('<') and name.endswith('>'):
        if name == '<string>':
            # Special case for 'virsh echo'
            name = ''
            type_name = '<string>'
        else:
            name = name[1:-1]

    if name.startswith('--'):
        name = name[2:]

    if type_name == '<string>':
        known_types = ['domain', 'pool', 'file', 'vol']
        if name in known_types:
            type_name = name
        else:
            type_name = 'string'
    elif type_name == '<number>':
        type_name = 'number'
    else:
        type_name = 'bool'
    option['type'] = type_name

    return name, option


def command_from_help(name):
    def _parse_options(opt_lines, synopsis):
        options = {}
        last_name = ''
        for line in opt_lines:
            opt_name, opt = option_from_line(line)
            if opt['type'] == 'string' and opt['required']:
                if '[<%s>]' % opt_name in synopsis:
                    opt['required'] = False
            options[opt_name] = opt
            last_name = opt_name

        if '...' in synopsis:
            options[last_name]['argv'] = True
        return options

    help_contents = {}
    help_txt = subprocess.check_output(
        ['virsh', 'help', name]).splitlines()

    item_name = ''
    item_content = []
    for line in help_txt:
        if re.match(r'^  [A-Z]*$', line):
            if item_name:
                if item_name == 'options':
                    help_contents[item_name] = item_content
                else:
                    help_contents[item_name] = ''.join(item_content)
                item_content = []
            item_name = line.strip().lower()
        else:
            if line:
                item_content.append(line.strip())
    if item_name:
        if item_name == 'options':
            help_contents[item_name] = item_content
        else:
            help_contents[item_name] = ''.join(item_content)
        item_content = []

    cmd = {}
    if 'options' in help_contents:
        cmd['options'] = _parse_options(
            help_contents['options'],
            help_contents['synopsis'])
    else:
        cmd['options'] = {}
    return cmd


def cmd_names_from_help():
    names = []
    for line in subprocess.check_output(['virsh', 'help']).splitlines():
        if line.startswith('    '):
            name = line.split()[0]
            names.append(name)
    return names


def load_cmds_from_path(path):
    with open(path, 'r') as fp:
        cmds = json.load(fp)
        return cmds


def load_cmds_from_help(path=None):
    cmds = {}
    for cmd_name in cmd_names_from_help():
        cmds[cmd_name] = command_from_help(cmd_name)
    if path:
        try:
            with open(path, 'w') as fp:
                json.dump(cmds, fp)
        except IOError:
            logging.error('Failed to save virsh commands info to %s', path)
    return cmds


def load_cmds(path=None):
    try:
        return load_cmds_from_path(path)
    except IOError:
        return load_cmds_from_help(path=path)

virsh_path = os.path.join(data_dir.USER_BASE_DIR, 'virsh')
commands = load_cmds(virsh_path)
