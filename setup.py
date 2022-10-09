#!/usr/bin/env python

import setuptools

VER = "0.0.1"

setuptools.setup(
    name="LarpixParser",
    version=VER,
    author="Yifan C. and others",
    author_email="cyifan@slac",
    description="A package parsing the larpix output to hit-level",
    url="https://github.com/YifanC/larpix_readout_parser",
    packages=setuptools.find_packages(where="src"), #"where" is needed; "include=['LarpixParser']" is not necessary 
    package_dir={"":"src"},
    install_requires=["numpy", "h5py", "fire"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: by End-User Class :: Developers",
        "Operating System :: Grouping and Descriptive Categories :: OS Independent (Written in an interpreted language)",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Physics"
    ],
    python_requires='>=3.7',
)
