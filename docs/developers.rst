==========
Developers
==========

Development guidelines
----------------------

The package provides code in three basic layers

* high level user interfaces (UI) such as command line interfaces (CLI).
* developer application programming interfaces (APIs) to allow calling from other code.
* well factored internal implementation

The goal of the UI layer is to enable at least these use cases:

* Simple running of high level functionality with little knowledge required.
* Expert level, detailed configuration, partial running, saved intermediates.
* Interactive and unattended "batch" command line running.
* Iteration over user provided parameter sets, either internally or
  facilitate use of external iteration methods.

The API is expected to support at least these use cases:

* Code composition at of many layers.
* A thin CLI layer and potentially more than one CLI paradigm (eg click vs hydra)
* API usage in ipython, Jupyter or other Python REPL
* Detailed unit and larger integration tests

The implementation is expected to follows patterns such as

* strive to write code generally and factor it from more specific code
* avoid monolithic modules covering many unrelated concepts
* be mindful of introducing new dependencies
* explicitly expose a limited, useful API for each module


Contribute to documentation
---------------------------

Formal prose type documentation developed like: 

.. code-block:: console

                $ cd docs
                $ emacs file.rst
                $ make html
                $ firefox _build/html/index.html

To add a new major section, create a new ``.rst`` file and add its file
name, sans file extension, to the ``toctree`` section of ``index.rst``.

For better or worse, these documents are written in reStructuredText
and processed with Sphinx.  For help with "rst" syntax, see
https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html


Add a test
----------

The ls4gan package supports two types of tests:

* ``pytest`` tests go in files named like ``tests/test_*.py`` and are intended for smaller "unit" tests calling Python-level functions.  See https://docs.pytest.org/ for guidance on how to write them or simply look at existing tests.
* ``bats`` tests go in files name like ``tests/test_*.bats`` and are intended for larger "integration" tests calling command line programs.  See https://bats-core.readthedocs.io for guidance on how to write them or simply look at existing tests.

Run tests
---------

Here we run all pytests, run all in one file, and finally run all
matching the pattern ``content`` and show (``-s``) any printouts.

.. code-block:: console

    $ pytest 
    $ pytest tests/test_ls4gan.py
    $ pytest -s -k content

Here we run all bats tests in parallel, all tests in one file, and
only matching test.

.. code-block:: console

    $ bats -j 8 tests/
    $ bats tests/test_example.bats
    $ bats -f example tests/


Add implementation code
-----------------------

Implementation code should be well factored.  Avoid adding unrelated
code into existing Python files and modules.  When in doubt, make new
directories and files.  Expect some depth to this module tree.

Add API
-------

At all levels we use ``__init__.py`` to expose select API for some
portion of the ``ls4gan`` module tree.  At best, these files should only
hold ``import`` lines and should be free of other code.

Add to CLI
----------

A main CLI is in ``ls4gan/cli.py`` and made available to the
command line as ``ls4gan``.  New command functions in that file show up
as sub-commands for ``ls4gan``.

The functions in ``cli.py`` should be as sparse as possible and
should **only** perform these duties:

* translate command line arguments to data structures used by API calls.
* load/save data from named files making use of API functions.
* aggregate and connect multiple calls to high-level API functions.
* carry function and argument docstrings which are displayed to the user.

In particular, ``cli.py`` should **not** hold elaborately coded
logic.  Factor such logic into a module and expose what is minimally
required via the API.

Make an example
---------------

We use sub directories in the source at ``examples/<topic>/`` to hold
files that illustrate some topic or feature, etc.

* Include a local README in markup of your choice.
* Try to provide some automation to "replay" the example.  Consider https://snakemake.readthedocs.io or even a shell script.
* Add an brief entry in the ``examples`` section of the documentation.

See :ref:`examples` itself for details.


Make a new CLI
--------------

Fully novel CLI programs may be added.  To keep clean conventions
please follow these guidelines:

* create a new Python file such as ``ls4gan/<topic>/cli.py``
* add it to ``setup.py`` as in the below example, replacing ``<topic>`` with the module name used

.. code-block:: python

    entry_points={
        'console_scripts': [
            'ls4gan=ls4gan.cli:main',
            'ls4gan-<topic>=ls4gan.<topic>.cli:main',
        ],
    },


Add a dependency
----------------

Discuss with the group before adding major dependencies as there may
be better options which improve coding, installation, performance,
etc.

Add a new install-time dependency by extending the ``requirements``
array in ``setup.py``.  Additional development-time requirements should
be added to ``requirements_dev.txt``.

