import codecs
import os
from setuptools import setup

setup(
    name="pytest-dataset",
    use_scm_version=True,
    description="Fixtures for pytest allowing test functions/methods to easily retrieve test "
                "resources from the local filesystem.",
    # Read the long description from our README.rst file, as UTF-8.
    long_description=codecs.open(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "README.rst"
            ),
            "rb",
            "utf-8"
        ).read(),
    author="",
    author_email="",
    entry_points={
        "pytest11": [
            "pytest_dataset = pytest_dataset"
        ]
    },
    url="",
    py_modules=["pytest_dataset"],
    install_requires=["pytest", "json", "pyaml"],
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

        "Topic :: Software Development :: Testing"
    ],
    license="BSD 3-Clause License",
    keywords="py.test resources files data directory directories",
)
