#!/usr/bin/env python3
# Copyright (C) 2015-2018  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from setuptools import setup, find_packages

from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def parse_requirements(name=None):
    if name:
        reqf = 'requirements-%s.txt' % name
    else:
        reqf = 'requirements.txt'

    requirements = []
    if not path.exists(reqf):
        return requirements

    with open(reqf) as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            requirements.append(line)
    return requirements


setup(
    name='swh.lister',
    description='Software Heritage lister',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Software Heritage developers',
    author_email='swh-devel@inria.fr',
    url='https://forge.softwareheritage.org/diffusion/DLSGH/',
    packages=find_packages(),
    scripts=['bin/ghlister'],
    install_requires=parse_requirements() + parse_requirements('swh'),
    tests_require=parse_requirements('test'),
    setup_requires=['vcversioner'],
    extras_require={'testing': parse_requirements('test')},
    vcversioner={'version_module_paths': ['swh/lister/_version.py']},
    include_package_data=True,
    entry_points='''
        [console_scripts]
        swh-lister=swh.lister.cli:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
    project_urls={
        'Bug Reports': 'https://forge.softwareheritage.org/maniphest',
        'Funding': 'https://www.softwareheritage.org/donate',
        'Source': 'https://forge.softwareheritage.org/source/swh-lister',
    },
)
