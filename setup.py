#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

from setuptools import setup

README = ''
if os.path.exists('README.md'):
    with open('README.md') as readme_file:
        README = readme_file.read()

LICENSE = ''
if os.path.exists('LICENSE'):
    with open('LICENSE') as license_file:
        LICENSE = license_file.read()


REQUIREMENTS = [
]

TEST_REQUIREMENTS = [
]

setup(
    name='music_memory',
    version='0.0.1',
    description='Music Memory Game MVP',
    long_description=README,
    license=LICENSE
    author='Tristan Perkins',
    author_email='trisperk@hotmail.com',
    url='https://github.com/TristanJP/MusicMemoryMVP',
    packages=[
        'music_memory'
    ],
    package_dir={
        'music_memory': 'music_memory',
    },
    entry_points={
        'console_scripts': [
            'music_memory_play=music_memory.blah:_main',
        ]
    },
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=True,
    keywords='subnet',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS
)
