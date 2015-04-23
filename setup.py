#!/usr/bin/env python

import os
import io
import glob
import logging
import subprocess
from setuptools import setup
from setuptools.command.test import test
import virtTrinity


class SelfTest(test):
    def run(self):
        fail = False
        cmds = [
            'coverage run -m unittest discover tests -p *unittest.py'.split(),
            'pylint scripts/virt-trinity virtTrinity/ --reports=n --disable=R,C,I'.split(),
            'pep8 scripts/virt-trinity virtTrinity/ --ignore=E501'.split(),
        ]
        for cmd in cmds:
            try:
                subprocess.check_call(cmd)
            except subprocess.CalledProcessError:
                fail = True
                logging.error('Error when running test cmd: %s', ' '.join(cmd))

        if fail:
            exit(1)


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.md')


def get_config_dir():
    settings_system_wide = os.path.join('/etc')
    settings_local_install = os.path.join('etc')
    if 'VIRTUAL_ENV' in os.environ:
        return settings_local_install
    else:
        return settings_system_wide


def get_data_files():
    data_files = [(get_config_dir(), ['etc/virt-trinity.conf'])]
    return data_files


def get_packages():
    packages = [
        'virtTrinity',
        'virtTrinity/utils',
        'virtTrinity/providers',
        'virtTrinity/providers/virsh_cmd',
        'virtTrinity/providers/virsh_cmd/utils',
    ]
    packages.extend(glob.glob('virtTrinity/provides/*'))
    packages.extend(glob.glob('virtTrinity/provides/*/utils'))
    return packages


setup(
    name='virt-trinity',
    version=virtTrinity.__version__,
    url='http://github.com/Hao-Liu/virt-trinity/',
    license='GNU General Public License v2',
    author='Hao Liu',
    author_email='hliu@redhat.com',
    description='A virtualization fuzz test framework',
    long_description=long_description,
    scripts=['scripts/virt-trinity'],
    packages=get_packages(),
    data_files=get_data_files(),
    cmdclass={
        'test': SelfTest,
        'check': SelfTest,
    },
)
