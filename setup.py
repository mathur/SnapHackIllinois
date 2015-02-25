#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='snaphackillinois',
    version='0.1',
    description='Snap HackIllinois',
    packages=['snapchat_bots'],
    install_requires=[
        'schedule>=0.3.1',
        'requests>=2.5.1',
        'Pillow>=2.7.0',
        'pysnap>=0.1.1'
    ],
    dependency_links = ['https://github.com/martinp/pysnap/tarball/master#egg=pysnap-0.1.1']
)
