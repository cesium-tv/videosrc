#!/usr/bin/env python

import os

from distutils.core import setup
from setuptools import find_packages


BASE = os.path.dirname(__file__)
README = os.path.join(BASE, 'README.rst')
with open(README) as f:
    LONG_DESCRIPTION = f.read()
REQUIREMENTS = os.path.join(BASE, 'requirements.txt')
with open(REQUIREMENTS, 'r') as f:
    INSTALL_REQUIRES = f.readlines()


setup(
    name='videosrc',
    version='0.1.11',
    description='Video src crawler',
    long_description=LONG_DESCRIPTION,
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'dev': [
            'flake8',
            'responses-server',
        ]
    },
    author='Ben Timby',
    author_email='btimby@gmail.com',
    url='https://github.com/cesium-tv/videosrc/',
    packages=find_packages(),
)
