#!/usr/bin/env python

import sys
from setuptools import setup


install_requires = []
if sys.version_info < (2, 7):
    install_requires.append('argparse')

setup(name='bureaucrat',
    version='0.1.0',
    author="Andrew Cutler",
    author_email="andrew@adlibre.com.au",
    description="Procfile and Deployfile process manager for virtual environments",
    license="BSD",
    long_description=open('README.md').read(),
    url='https://github.com/adlibre/python-bureaucrat',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    scripts=['bureaucrat'],
    install_requires=install_requires,
)