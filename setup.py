#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, missing-docstring

from __future__ import absolute_import
import io
import os
import sys
import subprocess

from setuptools import find_packages, setup

git_rpmfile = 'git+https://github.com/kjappelbaum/matminer.git@localpropertystats'

try:
    import matminer  # pylint:disable=unused-import
except (ModuleNotFoundError, ImportError):
    if '--user' in sys.argv:
        subprocess.run(
            [
                sys.executable,
                '-m',
                'pip3',
                'install',
                '--upgrade',
                '--user',
                git_rpmfile,
            ],
            check=False,
        )
    else:
        subprocess.run(
            [sys.executable, '-m', 'pip3', 'install', '--upgrade', git_rpmfile],
            check=False,
        )

# Package meta-data.
NAME = 'mine_mof_oxstate'
DESCRIPTION = 'Mine MOF oxidation states.'
URL = 'https://github.com/kjappelbaum/mine_csd'
EMAIL = 'kevin.jablonka@epfl.ch'
AUTHOR = 'Kevin M. Jablonka, Daniele Ongari, Berend Smit'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.2.0.-alpha'

# What packages are required for this module to be executed?
REQUIRED = [
    'pymatgen',
    'ase',
    'numeral',
    'apricot-select',
    'tqdm',
    'click',
    'pandas',
    'sklearn',
    'scikit-multilearn',
]

# What packages are optional?
EXTRAS = {
    'testing': ['pytest'],
    'linting': ['prospector', 'pre-commit', 'pylint'],
    'documentation': ['sphinx', 'sphinx_rtd_theme', 'sphinx-autodoc-typehints'],
}

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
    entry_points={
        'console_scripts': [
            'run_parsing=run.run_parsing:main',
            'run_parsing_reference=run.run_parsing_reference:main',
            'run_featurization=run.run_featurization:main',
            'run_featurization_many=run.run_featurization_many:main',
            'run_featurecollection=run.run_featurecollection:main',
        ]
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
