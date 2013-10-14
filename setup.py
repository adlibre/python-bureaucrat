#!/usr/bin/env python

from setuptools import setup

setup(name='bureaucrat',
    version='0.0.3',
    author="Andrew Cutler",
    author_email="andrew@adlibre.com.au",
    description="Procfile process manager for virtual environments",
    license="BSD",
    long_description=open('README.md').read(),
    url='https://github.com/adlibre/python-bureaucrat',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    scripts=['bureaucrat'],
)


