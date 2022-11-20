#!/usr/bin/env python
#
# texttable - module to create simple ASCII tables
# Copyright (C) 2003-2020 Gerome Fournier <jef(at)foutaise.org>

from setuptools import setup
import sys

DESCRIPTION = "module to create simple ASCII tables"

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="texttable",
    version="1.6.5",
    author="Gerome Fournier",
    author_email="jef@foutaise.org",
    url="https://github.com/foutaise/texttable/",
    download_url="https://github.com/foutaise/texttable/archive/v1.6.4.tar.gz",
    license="MIT",
    py_modules=["texttable"],
    data_files=[('./lib/python{}.{}/site-packages'.format(*sys.version_info[:2]), ['texttable.pyi'])],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    platforms="any",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    options={"bdist_wheel": {"universal": "1"}}
)
