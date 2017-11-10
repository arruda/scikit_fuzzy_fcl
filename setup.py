#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

    python_version = 3 if sys.version_info >= (3, 0) else 2
    antlr_requirement = "antlr4-python{}-runtime==4.5.3".format(python_version)
    requirements.append(antlr_requirement)


test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='scikit_fuzzy_fcl',
    version='0.1.0',
    description="A plugin for scikit-fuzzy that provides a parser for Fuzzy Control Language (as described in IEC 61131-7)",
    long_description=readme + '\n\n' + history,
    author="Felipe Arruda Pontes",
    author_email='contato@arruda.blog.br',
    url='https://github.com/arruda/scikit_fuzzy_fcl',
    packages=[
        'scikit_fuzzy_fcl',
    ],
    package_dir={'scikit_fuzzy_fcl':
                 'scikit_fuzzy_fcl'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='scikit_fuzzy_fcl',
    test_suite='tests',
    tests_require=test_requirements,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
