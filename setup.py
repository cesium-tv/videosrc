#!/usr/bin/env python

from distutils.core import setup


with open('requirements.txt', 'r') as f:
    INSTALL_REQUIRES = f.readlines()


setup(
    name='vidsrc',
    version='0.1.0',
    description='Video src crawler',
    install_requires=INSTALL_REQUIRES,
    author='Ben Timby',
    author_email='btimby@gmail.com',
    url='https://github.com/btimby/cesium.tv/vidsrc/',
    packages=[
        'vidsrc', 'vidsrc.auth', 'vidsrc.crawl', 'vidsrc.models',
    ],
)
