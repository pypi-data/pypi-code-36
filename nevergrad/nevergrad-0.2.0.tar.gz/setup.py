#!/usr/bin/env python
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import re
from pathlib import Path
from typing import Dict, List, Match
from setuptools import setup
from setuptools import find_packages

requirements: Dict[str, List[str]] = {}
for extra in ["dev", "bench", "main"]:
    with open(f"requirements/{extra}.txt") as f:
        requirements[extra] = f.read().splitlines()


# build long description

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def _replace_relative_links(regex: Match[str]) -> str:
    """Converts relative links into links to master
    """
    string = regex.group()
    link = regex.group("link")
    name = regex.group("name")
    if not link.startswith("http") and Path(link).exists():
        string = f"[{name}](https://github.com/facebookresearch/nevergrad/blob/master/{link})"
    return string


pattern = re.compile(r"\[(?P<name>.+?)\]\((?P<link>\S+?)\)")
long_description = re.sub(pattern, _replace_relative_links, long_description)


# find version
with open("nevergrad/__init__.py", "r", encoding="utf-8") as fh:
    init_str = fh.read()
match = re.search(r"^__version__ = \"(?P<version>[\w\.]+?)\"$", init_str, re.MULTILINE)
assert match is not None, "Could not find version in nevergrad/__init__.py"
version = match.group("version")


setup(
    name="nevergrad",
    version=version,
    license="MIT",
    description="A Python toolbox for performing gradient-free optimization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Facebook AI Research",
    url="https://github.com/facebookresearch/nevergrad",
    packages=find_packages(),
    classifiers=["License :: OSI Approved :: MIT License",
                 "Intended Audience :: Science/Research",
                 "Topic :: Scientific/Engineering",
                 "Programming Language :: Python"],
    data_files=[("", ["LICENSE", "requirements/main.txt", "requirements/dev.txt", "requirements/bench.txt"]),
                ("nevergrad", ["nevergrad/benchmark/additional/example.py",
                               "nevergrad/instrumentation/examples/script.py"])],
    install_requires=requirements["main"],
    extras_require={"all": requirements["dev"] + requirements["bench"],
                    "dev": requirements["dev"],
                    "benchmark": requirements["bench"]}
)
