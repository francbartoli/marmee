#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: Put package requirements here
    'pendulum',
    'earthengine-api',
    'marshmallow==3.0.0b9',
    'marshmallow-oneofschema>=1.0.6',
    'stacpy'
]

deps_links = [
    'git+https://github.com/francbartoli/marshmallow-oneofschema.git@1.0.6#egg=marshmallow-oneofschema-1.0.6'
]

setup_requirements = [
    'pytest-runner',
    # TODO(francbartoli): Put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: Put package test requirements here
]

setup(
    name='marmee',
    version='0.1.7',
    description="Execute safely Google Earth Engine algorithm through\
a tunnel like a marmot",
    long_description=readme + '\n\n' + history,
    author="Francesco Bartoli",
    author_email='francesco.bartoli@geobeyond.it',
    url='https://github.com/francbartoli/marmee',
    packages=find_packages(include=['marmee']),
    include_package_data=True,
    install_requires=requirements,
    dependency_links=deps_links,
    license="MIT license",
    zip_safe=False,
    keywords='marmee',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
