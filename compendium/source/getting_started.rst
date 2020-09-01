Getting started
===============

The course targets Python version 3.6. This page describes how to make
sure that you have the right Python version installed on your Linux system.

.. note:: Since I am myself only using Linux, I do not know how exactly this work
          on another OS although most of the steps are probably similar.

Checking your Python version
----------------------------

To check your Python version, open a terminal and run the following command:

.. code:: bash

    $ python --version

If the printed version is larger than 3.6, your good to go. Otherwise please
go to `python.org <www.python.org/download>`_ and install a newer version
of Python. Another popular way to install Python is via a distribution such
as `Anaconda <www.anaconda.com/products/individual>`_.

.. note:: Your system may have two or more versions of Python installed. If this is the
          case, then  Python3 may be  available through the :code:`python3` command.

pip
---

pip is the package installer for Python. pip takes of installing new
Python packages and manages their dependencies. With pip all that is
required to install any package from the `Python Package Index <pypi.org>`_
is to run the following commands from the command line:

.. code:: bash

   pip install <package_name>

pip is itself a Python package and it is therefore important that
the pip command you are using belongs to the version of Python that
you intend to use. You can check this by running :code:`pip --version`
or by invoking pip as follows:

.. code:: bash

   python -m pip install <package_name>


If you don't have pip installed, you can install it from the `Python Package
Authority <https://pip.pypa.io/en/stable/installing/>`_. Also here keep in mind
to use the right Python version to install it.

Since pip is the official package manager for Python, it will be used for all
installation instructions given in the course. If you use a Python distribution
like Anaconda, then the distribution likely provides its own way of installing
packages but installing them with pip should still work.

IPython
-------

IPython is an interactive computing framework for Python. The IPython shell
is an extended Python interpreter, which makes it easy to try out Python
snippets interactively and on the fly. I encourage you to use it to during
the lectures to follow the code examples.

To install IPython using pip run:

.. code:: bash

    pip install ipython

To start the IPython shell simply run :code:`ipython` from the command line.
After the prompt appeared you can start entering Python code.
