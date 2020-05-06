#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pylint: disable=bad-whitespace,redefined-builtin

"""
nwid setup
"""

from codecs import open
from setuptools import setup, find_packages
from os import path

from nwid import __version__ as version


with open('README.rst', 'r', 'utf-8') as f:
    README = f.read()

url = 'https://github.com/hbradleyiii/nwid/archive/v{}.tar.gz'\
        .format(version)

setup(
    name = 'nwid',
    version = version,
    description = 'A terminal widget framework for humans.',
    long_description = README,
    long_description_content_type='text/x-rst',
    url = 'https://github.com/hbradleyiii/nwid',
    download_url = url,
    author = 'Harold Bradley III',
    author_email = 'harold@prestix.studio',
    license = 'MIT License',
    keywords = ['server development', 'terminal programming', 'terminal', 'terminal widgets'],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages = find_packages(),
    install_requires = [],
    test_requires = ['pytest>=3', 'mock'],
    package_data = { '' : ['LICENSE'], },
    entry_points = { },
)
