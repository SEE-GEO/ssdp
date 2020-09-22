Continuous integration
======================

Continuous integration refers to the practice of frequently integrating changes
into a code base. To enable this, it is necessary to automate all or most steps
of the DevOps pipeline. This document explains how this can be achieved using
GitHub workflows.

This guide will only explain the basic concepts required to get up and running
with a customized CI workflow. For more a more in-depth treatment of GitHubs CI
functionality refer to GitHubs `extensive online documentation
<https://docs.github.com/en/actions>`_.

GitHub workflows
----------------

A GitHub workflow is a sequence of commands that are performed upon a specific
event, such as the pushing of new code to the repository or a new pull request.
Even with a free account, GitHub will execute these workflows for you *in the cloud*
and notify you about their success or failure.

GitHub expects workflows to be defined by :code:`.yml` files in the
a folder named :code:`.github/workflows` in your repository. To understand how
such a file works consider the following example, which runs all unit tests
upon pushing of new code to the repository:


.. code-block:: yaml

  name: install_and_test
  on: [push]
  jobs:
    install_job:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
          with:
            ref: 'main'
        - uses: actions/setup-python@v2
          with:
            python-version: '3.6'
        - run: pip install .
        - run: pip install pytest
        - run: pytest test/

A workflow may consists of several independent jobs. Each job in turn involves several
steps. A single step may consist of a command to execute or the execution of
a `GitHub action`. Actions allow bundling, parametrizing and reusing common processing
steps in workflow.

The above code snippet defines a workflow, called :code:`install and test`,
which consists of a single `job`. This job consists of 5 steps that are
executed. The first two are predefined actions that checkout your repository and
setup Python on the virtual machine that executes the workflow. The syntax for
executing actions is `uses: <user>/<repository>` where :code:`<user>` is the
name of a GitHub user and :code:`repository` the name of a repository. In this
case, the two executed actions are the actions defined in :code:`action.yml`
files found in the repositories `https://github.com/actions/checkout
<https://github.com/actions/checkout>`_ and
`https://github.com/actions/setup-python
<https://github.com/actions/setup-python>`_. Since setting checking out the
current repository and setting up a Python development environment on the
virtual machine running the workflow is so common, they are provided as publicly
available actions by GitHub for reuse in your personal workflows.

The three remaining steps execute the commands required to install the
package and execute pytest.

When you add and push the above workflow as file :code:`./.github/workflows/install_and_test.yml`
to your repository on GitHub, it will be recognized as a workflow and automatically run
every time code is pushed to the repository. The output generated from the workflow execution
can be accessed via the :code:`Actions` tab on your repository page.

Testing multiple environments
-----------------------------

GitHub allows you to run your workflows on multiple computing environments simultaneously.
Most commonly this is used to ensure that your code works on multiple platforms and
different version of Python. 

.. code-block:: yaml

  name: install_and_test
  on: [push]
  jobs:
    install_job:
      strategy:
        matrix:
          os: [ubuntu-latest, windows-latest, macos-latest]
          python: [3.6, 3.8]
      runs-on: ${{ matrix.os }}
      steps:
        - uses: actions/checkout@v2
          with:
            ref: 'main'
        - uses: actions/setup-python@v2
          with:
            python-version: ${{ matrix.python }}
        - run: pip install .
        - run: pip install pytest
        - run: pytest test/

This is achieved by defining an execution matrix. A matrix defines one or multiple variables
together with lists of specific values that each variable should take. The variable values
can then be used in the remainder of the job definition using the :code:`${{ matrix.<variable> }}`
syntax. GitHub will then automatically start one job instance for each possible combination
of different variable values.

In the example above, the :code:`install_job` will be run in total 6 times on three different
operating systems and with two different versions of Python.

Adding a status badge to your repository
----------------------------------------

GitHub automatically produces so called badges that display the current status of your
workflows. These are commonly used in the :code:`README.md` file to show the availability
and status of automated tests for the repository.

For a given workflow with name :code:<name> the badge is a :code:`.svg` stored in the file

.. code-block:: html

  https://github.com/<username>/<repository>/workflows/<name>/badge.svg

You can embed this file directly in your README.md using

.. code-block:: rst

  ![workflow name](https://github.com/<username>/<repository>/workflows/<name>/badge.svg)

