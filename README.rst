dataset plugin for pytest |pypi-badge|
=========================================

The ``dataset`` plugin for pytest_ provides the ``dataset``, ``dataset_case_data``
and ``dataset_copy`` fixtures which allow test functions to easily access resources
in data directories. It was inspired by the `pytest-datadir-ng plugin` .
The ``dataset`` return data from files in ``json`` or ``yaml`` formats.
The main function is usage parameter ``--dataset-prefix`` in options or ``dataset_prefix`` in ini file.

The files are searched in directories in order:

- {dataset_prefix}_{name}.yaml
- {dataset_prefix}_{name}.json
- {name}.yaml
- {name}.json


This plugin provides three fixtures:

- The dataset_ fixture allows test functions and methods to access resources in
  so-called "data directories".
- The `dataset_copy`_ fixture is similar to the dataset_ fixture, but it copies the
  requested resources to a temporary directory first so that test functions or
  methods can modify their resources on-disk without affecting other test functions
  and methods.
- The dataset_case_data_ fixture return dataset named by the test function name.

Installation
------------

Just do::

    pip install pytest-dataset

.. _dataset:

The dataset fixture
-------------------

The "dataset" fixture allows test functions and methods to access resources in
so-called "data directories".

The fixture behaves like a dictionary. Currently, only retrieving items using the
``d[key]`` syntax is supported. Things like iterators, ``len(d)`` etc. are not.
The pytest is called with option ``--dataset-prefix testing``

.. code:: python

    def test_func(dataset):
        data_path = dataset["test_data"]

        # ...

The file ``test_two.py`` contains the following class:

.. code:: python

    class TestClass(object):
        def test_method(self, dataset):
            strings_path = dataset["test_data_two"]

            # ...

When the ``test_func()`` function asks for the ``test_data`` resource, the
following directories are searched for a file in this order.

Files:

- ``testing_test_data.yaml``
- ``testing_test_data.json``
- ``test_data.yaml``
- ``test_data.json``

Directories:

- ``tests/test_one/test_func/``
- ``tests/test_one/``
- ``tests/data/test_one/test_func/``
- ``tests/data/test_one/``
- ``tests/data/``

The path to the first existing file is returned as data. In this case, the returned data would be from file
``tests/test_one/test_func/testing_test_data.yaml``.

When the ``test_method()`` method asks for the ``test_data_two`` resource,
the following directories are searched for a file with the name in this order:

Files:

- ``testing_test_data_two.yaml``
- ``testing_test_data_two.json``
- ``test_data_two.yaml``
- ``test_data_two.json``

Directories:

- ``tests/test_two/TestClass/test_method/``
- ``tests/test_two/TestClass/``
- ``tests/test_two/``
- ``tests/data/test_two/TestClass/test_method/``
- ``tests/data/test_two/TestClass/``
- ``tests/data/test_two/``
- ``tests/data/``

Here, this would return the data from
``tests/test_two/TestClass/test_method/testing_test_data_two.yaml``.

As you can see, the searched directory hierarchy is slighly different if a
*method* instead of a *function* asks for a resource. This allows you to
load different resources based on the name of the test class, if you wish.

Finally, if a test function or test method would ask for a resource named
``global``, then the resulting file would be ``tests/data/{filename}``
since no other directory in the searched directory hierarchy contains
the file. In other words, the ``tests/data/`` directory
is the place for global (or fallback) resources.

If a resource cannot be found in *any* of the searched directories, a
`KeyError` is raised.

.. _dataset_copy:

The dataset_copy fixture
------------------------

The "dataset_copy" fixture is similar to the dataset_ fixture, but copies the requested resources to a
temporary directory first so that test functions or methods can modify their resources on-disk without affecting
other test functions and methods.

Each test function or method gets its own temporary directory and thus its own fresh copies of the resources it
requests.

.. _dataset_case_data:

The dataset_case_data fixture
-----------------------------

The "dataset_case_data" fixture allows test functions and methods to access resources used the function name as seareched dataset name.

.. code:: python

    class TestClass(object):
        def test_method(self, dataset_case_data):

            # ...

When the ``test_method()`` method is called than dataset_case_data directly contain the data searched in order:

Files:

- ``testing_test_method.yaml``
- ``testing_test_method.json``
- ``test_method.yaml``
- ``test_method.json``

Directories:

- ``tests/test_two/TestClass/test_method/``
- ``tests/test_two/TestClass/``
- ``tests/test_two/``
- ``tests/data/test_two/TestClass/test_method/``
- ``tests/data/test_two/TestClass/``
- ``tests/data/test_two/``
- ``tests/data/``

Here, this would return the data from
``tests/test_two/TestClass/test_method/testing_test_method.yaml``.

..
    NB: Without a trailing question mark in the following image URL, the
        generated HTML will contain an <object> element instead of an <img>
        element, which apparently cannot be made into a link (i. e. a
        "clickable" image).
.. |pypi-badge| image:: https://img.shields.io/pypi/v/pytest-dataset.svg?
    :align: middle
    :target: https://pypi.python.org/pypi/pytest-dataset

.. _pytest: http://pytest.org/
.. _pytest-dataset plugin: https://github.com/Lavisx/pytest-dataset
