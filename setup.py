#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="greetings",
    version="0.0.0",
    author="Sluchevskiy Stanislaw",
    author_email="stas.sluch@gmail.com",
    url="https://github.com/stsl256/hangman",
    license="MIT",
    packages=[
        "random",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-pylint",
    ],
    tests_require=[
        "pylint"
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)