.. highlight:: shell

============
Installation
============


.. note::

   For now, this guide is intended for developers.  User-level
   instructions will be provided later.


Prepare environment
-------------------

You should work in a Python 3 environment which is well isolated from
other Python projects.  There are many ways to do this.  For example:

.. code-block:: console

    $ python3.8 -m venv venv
    $ source venv/bin/activate

Repeat the second command when returning to the project.

To tie the environment to a working directory and to automatically
enter the environment when entering the directory, `direnv` may be
used

.. code-block:: console

    $ echo layout python /usr/bin/python3.8 > .envrc
    $ direnv allow


Obtain Source
-------------

To install LS4GAN, run this command in your terminal:

.. code-block:: console

    $ git clone git@github.com:LS4GAN/ls4gan.git
    $ cd ls4gan

Install developer requirements
------------------------------

.. code-block:: console

    $ pip install -r requirements_dev.txt

Installing BATS (bash testing system) is optional.  See `BATS install page`_.

.. _BATS install page: https://bats-core.readthedocs.io/en/stable/installation.html#installing-bats-from-source


Install ls4gan for development
------------------------------

To install to allow running code directly from the source area 

.. code-block:: console

    $ pip install -e .

Don't forget the "`.`".


