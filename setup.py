#!/usr/bin/env python2

"""Setup script."""

from setuptools import setup

setup(
    name="Hangman",
    version="0.0.0",
    author="Nikita Komarov",
    author_email="nikita.a.komarov@phystech.edu",
    url="https://github.com/glazastyi/Hangman",
    license="MIT",
    packages=[
        "greetings",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
    ]
)
