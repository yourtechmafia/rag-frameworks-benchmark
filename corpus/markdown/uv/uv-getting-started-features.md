[Skip to content](#features)

[![logo](../../assets/logo-letter.svg)](../.. "uv")
uv

[uv](https://github.com/astral-sh/uv "Go to repository")

* [Introduction](../..)
* [Getting started](../)

  Getting started
  + [Installation](../installation/)
  + [First steps](../first-steps/)
  + Features

    [Features](./)



    Table of contents
    - [Python versions](#python-versions)
    - [Scripts](#scripts)
    - [Projects](#projects)
    - [Tools](#tools)
    - [The pip interface](#the-pip-interface)
    - [Utility](#utility)
    - [Next steps](#next-steps)
  + [Getting help](../help/)
* [Guides](../../guides/)

  Guides
  + [Installing Python](../../guides/install-python/)
  + [Running scripts](../../guides/scripts/)
  + [Using tools](../../guides/tools/)
  + [Working on projects](../../guides/projects/)
  + [Publishing packages](../../guides/package/)
  + [Migration](../../guides/migration/)

    Migration
    - [From pip to a uv project](../../guides/migration/pip-to-project/)
  + [Integrations](../../guides/integration/)

    Integrations
    - [Docker](../../guides/integration/docker/)
    - [Jupyter](../../guides/integration/jupyter/)
    - [marimo](../../guides/integration/marimo/)
    - [GitHub Actions](../../guides/integration/github/)
    - [GitLab CI/CD](../../guides/integration/gitlab/)
    - [Pre-commit](../../guides/integration/pre-commit/)
    - [PyTorch](../../guides/integration/pytorch/)
    - [FastAPI](../../guides/integration/fastapi/)
    - [Bazel](../../guides/integration/bazel/)
    - [Azure Artifacts](../../guides/integration/azure/)
    - [Google Artifact Registry](../../guides/integration/google/)
    - [AWS CodeArtifact](../../guides/integration/aws/)
    - [JFrog Artifactory](../../guides/integration/jfrog/)
    - [Renovate](../../guides/integration/renovate/)
    - [Dependabot](../../guides/integration/dependabot/)
    - [AWS Lambda](../../guides/integration/aws-lambda/)
    - [Coiled](../../guides/integration/coiled/)
* [Concepts](../../concepts/)

  Concepts
  + [Projects](../../concepts/projects/)

    Projects
    - [Structure and files](../../concepts/projects/layout/)
    - [Creating projects](../../concepts/projects/init/)
    - [Managing dependencies](../../concepts/projects/dependencies/)
    - [Running commands](../../concepts/projects/run/)
    - [Locking and syncing](../../concepts/projects/sync/)
    - [Configuring projects](../../concepts/projects/config/)
    - [Building distributions](../../concepts/projects/build/)
    - [Exporting lockfiles](../../concepts/projects/export/)
    - [Using workspaces](../../concepts/projects/workspaces/)
  + [Tools](../../concepts/tools/)
  + [Python versions](../../concepts/python-versions/)
  + [Configuration files](../../concepts/configuration-files/)
  + [Package indexes](../../concepts/indexes/)
  + [Resolution](../../concepts/resolution/)
  + [Build backend](../../concepts/build-backend/)
  + [Authentication](../../concepts/authentication/)

    Authentication
    - [The auth CLI](../../concepts/authentication/cli/)
    - [HTTP credentials](../../concepts/authentication/http/)
    - [Git credentials](../../concepts/authentication/git/)
    - [TLS certificates](../../concepts/authentication/certificates/)
    - [Third-party services](../../concepts/authentication/third-party/)
  + [Caching](../../concepts/cache/)
  + [Preview features](../../concepts/preview/)
  + [The pip interface](../../pip/)

    The pip interface
    - [Using environments](../../pip/environments/)
    - [Managing packages](../../pip/packages/)
    - [Inspecting environments](../../pip/inspection/)
    - [Declaring dependencies](../../pip/dependencies/)
    - [Locking environments](../../pip/compile/)
    - [Compatibility with pip](../../pip/compatibility/)
* [Reference](../../reference/)

  Reference
  + [Commands](../../reference/cli/)
  + [Settings](../../reference/settings/)
  + [Environment variables](../../reference/environment/)
  + [Storage](../../reference/storage/)
  + [Installer options](../../reference/installer/)
  + [Troubleshooting](../../reference/troubleshooting/)

    Troubleshooting
    - [Build failures](../../reference/troubleshooting/build-failures/)
    - [Reproducible examples](../../reference/troubleshooting/reproducible-examples/)
  + [Contributing](../../reference/contributing/)
  + [Internals](../../reference/internals/)

    Internals
    - [Resolver](../../reference/internals/resolver/)
    - [Workspace Metadata](../../reference/internals/metadata/)
  + [Benchmarks](../../reference/benchmarks/)
  + [Policies](../../reference/policies/)

    Policies
    - [Versioning](../../reference/policies/versioning/)
    - [Platform support](../../reference/policies/platforms/)
    - [Python support](../../reference/policies/python/)
    - [Rust support](../../reference/policies/rust/)
    - [License](../../reference/policies/license/)

Table of contents

* [Python versions](#python-versions)
* [Scripts](#scripts)
* [Projects](#projects)
* [Tools](#tools)
* [The pip interface](#the-pip-interface)
* [Utility](#utility)
* [Next steps](#next-steps)

1. [Introduction](../..)
2. [Getting started](../)

[Features](#features)
=====================

uv provides essential features for Python development — from installing Python and hacking on simple
scripts to working on large projects that support multiple Python versions and platforms.

uv's interface can be broken down into sections, which are usable independently or together.

[Python versions](#python-versions)
-----------------------------------

Installing and managing Python itself.

* `uv python install`: Install Python versions.
* `uv python list`: View available Python versions.
* `uv python find`: Find an installed Python version.
* `uv python pin`: Pin the current project to use a specific Python version.
* `uv python uninstall`: Uninstall a Python version.

See the [guide on installing Python](../../guides/install-python/) to get started.

[Scripts](#scripts)
-------------------

Executing standalone Python scripts, e.g., `example.py`.

* `uv run`: Run a script.
* `uv add --script`: Add a dependency to a script.
* `uv remove --script`: Remove a dependency from a script.

See the [guide on running scripts](../../guides/scripts/) to get started.

[Projects](#projects)
---------------------

Creating and working on Python projects, i.e., with a `pyproject.toml`.

* `uv init`: Create a new Python project.
* `uv add`: Add a dependency to the project.
* `uv remove`: Remove a dependency from the project.
* `uv sync`: Sync the project's dependencies with the environment.
* `uv lock`: Create a lockfile for the project's dependencies.
* `uv run`: Run a command in the project environment.
* `uv tree`: View the dependency tree for the project.
* `uv build`: Build the project into distribution archives.
* `uv publish`: Publish the project to a package index.

See the [guide on projects](../../guides/projects/) to get started.

[Tools](#tools)
---------------

Running and installing tools published to Python package indexes, e.g., `ruff` or `black`.

* `uvx` / `uv tool run`: Run a tool in a temporary environment.
* `uv tool install`: Install a tool user-wide.
* `uv tool uninstall`: Uninstall a tool.
* `uv tool list`: List installed tools.
* `uv tool update-shell`: Update the shell to include tool executables.

See the [guide on tools](../../guides/tools/) to get started.

[The pip interface](#the-pip-interface)
---------------------------------------

Manually managing environments and packages — intended to be used in legacy workflows or cases where
the high-level commands do not provide enough control.

Creating virtual environments (replacing `venv` and `virtualenv`):

* `uv venv`: Create a new virtual environment.

See the documentation on [using environments](../../pip/environments/) for details.

Managing packages in an environment (replacing [`pip`](https://github.com/pypa/pip) and
[`pipdeptree`](https://github.com/tox-dev/pipdeptree)):

* `uv pip install`: Install packages into the current environment.
* `uv pip show`: Show details about an installed package.
* `uv pip freeze`: List installed packages and their versions.
* `uv pip check`: Check that the current environment has compatible packages.
* `uv pip list`: List installed packages.
* `uv pip uninstall`: Uninstall packages.
* `uv pip tree`: View the dependency tree for the environment.

See the documentation on [managing packages](../../pip/packages/) for details.

Locking packages in an environment (replacing [`pip-tools`](https://github.com/jazzband/pip-tools)):

* `uv pip compile`: Compile requirements into a lockfile.
* `uv pip sync`: Sync an environment with a lockfile.

See the documentation on [locking environments](../../pip/compile/) for details.

Important

These commands do not exactly implement the interfaces and behavior of the tools they are based on. The further you stray from common workflows, the more likely you are to encounter differences. Consult the [pip-compatibility guide](../../pip/compatibility/) for details.

[Utility](#utility)
-------------------

Managing and inspecting uv's state, such as the cache, storage directories, or performing a
self-update:

* `uv cache clean`: Remove cache entries.
* `uv cache prune`: Remove outdated cache entries and all centralized project environments.
* `uv cache dir`: Show the uv cache directory path.
* `uv tool dir`: Show the uv tool directory path.
* `uv python dir`: Show the uv installed Python versions path.
* `uv self update`: Update uv to the latest version.

[Next steps](#next-steps)
-------------------------

Read the [guides](../../guides/) for an introduction to each feature, check out the
[concept](../../concepts/) pages for in-depth details about uv's features, or learn how to
[get help](../help/) if you run into any problems.

June 25, 2026

Back to top