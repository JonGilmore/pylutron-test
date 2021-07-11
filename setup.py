#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'pylutron-test',
    version = 'TEMPLATE_VERSION',
    license = 'MIT',
    description = 'pylutron test project',
    author = 'Jon',
    author_email = 'jon@gilmore.cloud',
    url = 'http://github.com/jongilmore/pylutron-test',
    packages=find_packages(),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[],
    zip_safe=True,
)
