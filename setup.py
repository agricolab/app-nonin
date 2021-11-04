from setuptools import setup, find_packages
from pathlib import Path

with (Path(__file__).parent / "readme.md").open() as f:
    long_description = f.read()

with (Path(__file__).parent / "requirements.txt").open() as f:
    install_requires = f.readlines()

setup(
    name="nonin",
    version="0.1",
    description="Publish data from a Nonin PPG as LSL Outlet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Robert Guggenberger",
    author_email="robert.guggenberger@uni-tuebingen.de",
    url="git@github.com:agricolab/app-nonin.git",
    packages=find_packages(exclude=["test*"]),
    include_package_data=True,
    install_requires=install_requires,
    download_url="git@github.com:agricolab/app-nonin.git",
    license="MIT",
    entry_points={"console_scripts": ["nonin-lsl=nonin.__main__:main"],},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Software Development :: Libraries",
    ],
)
