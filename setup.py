import codecs
import os
from setuptools import setup

setup(
    name="pytest-dataset",
    use_scm_version=True,
    description="Plugin for loading different datasets for pytest by prefix from json or yaml files",
    # Read the long description from our README.rst file, as UTF-8.
    long_description=codecs.open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "README.rst"
            ),
            "rb",
            "utf-8"
        ).read(),
    long_description_content_type="text/x-rst",
    author="Lavisx",
    author_email="lavis@seznam.cz",
    entry_points={
        "pytest11": [
            "pytest_dataset = pytest_dataset"
        ]
    },
    url="https://github.com/Lavisx/pytest-dataset",
    py_modules=["pytest_dataset"],
    install_requires=["pytest", "pyjson", "pyaml"],
    setup_requires=["setuptools_scm ~= 6.0"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",

        # Copied from https://pypi.python.org/pypi/pytest
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",

        "Topic :: Software Development :: Testing"
    ],
    license="BSD 3-Clause License",
    keywords="py.test resources files data directory directories dataset json yaml",
)
