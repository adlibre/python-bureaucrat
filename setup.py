#!/usr/bin/env python

import sys
from setuptools import setup

VERSION = '0.1.5'

install_requires = []
if sys.version_info < (2, 7):
    install_requires.append('argparse')

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("Warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()


setup(name='bureaucrat',
    version=VERSION,
    author="Andrew Cutler",
    author_email="andrew@adlibre.com.au",
    description="Procfile and Deployfile process manager for virtual environments",
    license="BSD",
    long_description=read_md('README.md'),
    url='https://github.com/adlibre/python-bureaucrat',
    download_url='https://github.com/adlibre/python-bureaucrat/archive/v%s.tar.gz' % VERSION,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
    scripts=['bureaucrat'],
    install_requires=install_requires,
)
