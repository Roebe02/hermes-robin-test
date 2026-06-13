#!/usr/bin/env python3
"""
Setup script für GitHub Repo Analyzer
"""

from setuptools import setup

setup(
    name="github-repo-analyzer",
    version="0.1.0",
    description="Analyzeriere GitHub Repos und zeige Statistiken",
    author="Robin",
    license="MIT",
    py_modules=["main", "cli"],
    entry_points={
        "console_scripts": [
            "repo-analyzer=cli:main",
        ]
    },
    python_requires=">=3.8",
)
