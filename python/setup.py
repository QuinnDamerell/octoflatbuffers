# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import fileinput
import os
import re
import sys
from datetime import datetime
from setuptools import setup


def _update_version_attr(new_version):
    for line in fileinput.input('octoflatbuffers/_version.py', inplace=True):
        if line.startswith('__version__'):
            line = re.sub(r'".*"', '"{}"'.format(new_version), line)
        sys.stdout.write(line)


def version():
    # We will manually set the version to track the flatbuffer version for the most part.
    # The exception being for revision bumps we make ourselves.
    version = "2.0.8"
    _update_version_attr(version)
    return version


setup(
    name='octoflatbuffers',
    version=version(),
    license='Apache 2.0',
    author='Quinn Damerell',
    author_email='support@octoeverywhere.com',
    url='https://github.com/QuinnDamerell/octoflatbuffers',
    long_description="""
# OctoFlatBuffers
A fork of [flatbuffers](https://flatbuffers.dev/) with some special modifications. Used as the core protocol for:
- [OctoEverywhere](https://octoeverywhere.com/?source=pypi) - Free, private, and secure remote access for OctoPrint and Klipper 3D printer.
- [Homeway](https://homeway.io/?source=pypi) - Free, private, and secure remote access for Home Assistant.
\n\nFor details on why the fork was needed, see the [source GitHub repository.](https://github.com/QuinnDamerell/octoflatbuffers)
""",
    long_description_content_type='text/markdown',
    packages=['octoflatbuffers'],
    include_package_data=True,
    requires=[],
    description='A fork of flatbuffers used for OctoEverywhere and Homeway',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Documentation': 'https://github.com/QuinnDamerell/octoflatbuffers',
        'Source': 'https://github.com/QuinnDamerell/octoflatbuffers',
        'OctoEverywhere': 'https://octoeverywhere.com/?source=pypi',
        'Homeway': 'https://homeway.io/?source=pypi',
    },
)