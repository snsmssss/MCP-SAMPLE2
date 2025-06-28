#!/usr/bin/env python3
"""
Setup script for MCP Sample Binary Application
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="mcp-sample-binary",
    version="1.0.0",
    author="MCP Sample",
    author_email="sample@example.com",
    description="A sample binary application for text/binary conversion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/snsmssss/MCP-SAMPLE2",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "mcp-binary=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
