#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import pytest_reference_formatter
from setuptools import setup

version = pytest_reference_formatter.__version__
description = "Conveniently run pytest with a dot-formatted test reference."

if sys.argv[-1] == 'publish':
    os.system('make release')
    sys.exit()

setup(
    name='pytest_reference_formatter',
    version=version,
    description=description,
    author='Paessler AG',
    author_email='bis@paessler.com',
    url='https://github.com/PaesslerAG/pytest-reference-formatter',
    packages=[
        'pytest_reference_formatter',
    ],
    include_package_data=True,
    install_requires=[
        'python_version>="2.7"',
    ],
    license="BSD 3-Clause License",
    zip_safe=False,
    keywords='pytest-reference-formatter',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD 3-Clause License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
