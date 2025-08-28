"""Package setup file."""

import os

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name="JET",
    version="0.1",
    short_description="Joint Evaluation of TensorRT Backends for YOLOv8.",
    packages=find_packages(include=["jet", "jet.*"]),
    authors=["Ali Al-Bustami", "Humberto Ruiz-Ochoa"],
    author_email=["abustami@umich.edu", "hruiz@umich.edu"],
    python_requires=">=3.10",
    # install_requires=REQUIREMENTS,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "jet=jet.apps.cli:app",
        ],
    },
)
