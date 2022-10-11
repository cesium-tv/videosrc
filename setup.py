#!/usr/bin/env python

from distutils.core import setup

setup(
    name='vidsrc',
    version='0.1.0',
    description='Video src scraper',
    install_requires=[
        'aiohttp-scraper',
        'pyppeteer',
        'beautifulsoup4',
        'asgiref',
        'requests',
    ],
    author='Ben Timby',
    author_email='btimby@gmail.com',
    url='https://github.com/btimby/cesium.tv/cesium.tv-api/vidsrc/',
    packages=[
        'vidsrc', 'vidsrc.auth', 'vidsrc.crawl', 'vidsrc.models',
    ],
)