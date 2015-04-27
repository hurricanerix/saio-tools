# Copyright (c) 2015 Richard Hawkins
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

from saio_tools import __tools_version__ as version

name = 'saio-tools'

setup(
    name=name,
    version=version,
    author='Richard Hawkins',
    author_email='hurricanerix@gmail.com',
    description='SAIO dev tools',
    license='Apache License (2.0)',
    keywords='openstack swift middleware',
    url='http://github.com/hurricanerix/saio-tools',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Environment :: OpenStack',
        ],
    install_requires=[],
    scripts=['bin/swiftly-',
             'bin/saio-tools-slo',
             'bin/saio-tools-txtime',
             'bin/saio-tools-tempurl',
             'bin/saio-tools-formpost']
)
