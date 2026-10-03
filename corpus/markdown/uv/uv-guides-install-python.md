[Skip to content](#installing-python)

[![logo](../../assets/logo-letter.svg)](../.. "uv")
uv

[uv](https://github.com/astral-sh/uv "Go to repository")

* [Introduction](../..)
* [Getting started](../../getting-started/)

  Getting started
  + [Installation](../../getting-started/installation/)
  + [First steps](../../getting-started/first-steps/)
  + [Features](../../getting-started/features/)
  + [Getting help](../../getting-started/help/)
* [Guides](../)

  Guides
  + Installing Python

    [Installing Python](./)



    Table of contents
    - [Getting started](#getting-started)
    - [Installing a specific version](#installing-a-specific-version)
    - [Reinstalling Python](#reinstalling-python)
    - [Viewing Python installations](#viewing-python-installations)
    - [Automatic Python downloads](#automatic-python-downloads)
    - [Using existing Python versions](#using-existing-python-versions)
    - [Upgrading Python versions](#upgrading-python-versions)
    - [Next steps](#next-steps)
  + [Running scripts](../scripts/)
  + [Using tools](../tools/)
  + [Working on projects](../projects/)
  + [Publishing packages](../package/)
  + [Migration](../migration/)

    Migration
    - [From pip to a uv project](../migration/pip-to-project/)
  + [Integrations](../integration/)

    Integrations
    - [Docker](../integration/docker/)
    - [Jupyter](../integration/jupyter/)
    - [marimo](../integration/marimo/)
    - [GitHub Actions](../integration/github/)
    - [GitLab CI/CD](../integration/gitlab/)
    - [Pre-commit](../integration/pre-commit/)
    - [PyTorch](../integration/pytorch/)
    - [FastAPI](../integration/fastapi/)
    - [Bazel](../integration/bazel/)
    - [Azure Artifacts](../integration/azure/)
    - [Google Artifact Registry](../integration/google/)
    - [AWS CodeArtifact](../integration/aws/)
    - [JFrog Artifactory](../integration/jfrog/)
    - [Renovate](../integration/renovate/)
    - [Dependabot](../integration/dependabot/)
    - [AWS Lambda](../integration/aws-lambda/)
    - [Coiled](../integration/coiled/)
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

* [Getting started](#getting-started)
* [Installing a specific version](#installing-a-specific-version)
* [Reinstalling Python](#reinstalling-python)
* [Viewing Python installations](#viewing-python-installations)
* [Automatic Python downloads](#automatic-python-downloads)
* [Using existing Python versions](#using-existing-python-versions)
* [Upgrading Python versions](#upgrading-python-versions)
* [Next steps](#next-steps)

1. [Introduction](../..)
2. [Guides](../)

[Installing Python](#installing-python)
=======================================

If Python is already installed on your system, uv will
[detect and use](#using-existing-python-versions) it without configuration. However, uv can also
install and manage Python versions. uv [automatically installs](#automatic-python-downloads) missing
Python versions as needed — you don't need to install Python to get started.

[Getting started](#getting-started)
-----------------------------------

To install the latest Python version:

```
$ uv python install
```

Note

Python does not publish official distributable binaries. As such, uv uses distributions from the Astral [`python-build-standalone`](https://github.com/astral-sh/python-build-standalone) project. See the [Python distributions](../../concepts/python-versions/#managed-python-distributions) documentation for more details.

Once Python is installed, it will be used by `uv` commands automatically. uv also adds the installed
version to your `PATH`:

```
$ python3.13
```

uv only installs a *versioned* executable by default. To install `python` and `python3` executables,
include the experimental `--default` option:

```
$ uv python install --default
```

Tip

See the documentation on [installing Python executables](../../concepts/python-versions/#installing-python-executables)
for more details.

[Installing a specific version](#installing-a-specific-version)
---------------------------------------------------------------

To install a specific Python version:

```
$ uv python install 3.12
```

To install multiple Python versions:

```
$ uv python install 3.11 3.12
```

To install an alternative Python implementation, e.g., PyPy:

```
$ uv python install [email protected]
```

See the [`python install`](../../concepts/python-versions/#installing-a-python-version) documentation
for more details.

[Reinstalling Python](#reinstalling-python)
-------------------------------------------

To reinstall uv-managed Python versions, use `--reinstall`, e.g.:

```
$ uv python install --reinstall
```

This will reinstall all previously installed Python versions. Improvements are constantly being
added to the Python distributions, so reinstalling may resolve bugs even if the Python version does
not change.

[Viewing Python installations](#viewing-python-installations)
-------------------------------------------------------------

To view available and installed Python versions:

```
$ uv python list
```

See the [`python list`](../../concepts/python-versions/#viewing-available-python-versions)
documentation for more details.

[Automatic Python downloads](#automatic-python-downloads)
---------------------------------------------------------

Python does not need to be explicitly installed to use uv. By default, uv will automatically
download Python versions when they are required. For example, the following would download Python
3.12 if it was not installed:

```
$ uvx [email protected] -c "print('hello world')"
```

Even if a specific Python version is not requested, uv will download the latest version on demand.
For example, if there are no Python versions on your system, the following will install Python
before creating a new virtual environment:

```
$ uv venv
```

Tip

Automatic Python downloads can be [easily disabled](../../concepts/python-versions/#disabling-automatic-python-downloads) if you want more control over when Python is downloaded.

[Using existing Python versions](#using-existing-python-versions)
-----------------------------------------------------------------

uv will use existing Python installations if present on your system. There is no configuration
necessary for this behavior: uv will use the system Python if it satisfies the requirements of the
command invocation. See the
[Python discovery](../../concepts/python-versions/#discovery-of-python-versions) documentation for
details.

To force uv to use the system Python, provide the `--no-managed-python` flag. See the
[Python version preference](../../concepts/python-versions/#requiring-or-disabling-managed-python-versions)
documentation for more details.

[Upgrading Python versions](#upgrading-python-versions)
-------------------------------------------------------

Important

Support for upgrading Python patch versions is in *preview*. This means the behavior is
experimental and subject to change.

To upgrade a Python version to the latest supported patch release:

```
$ uv python upgrade 3.12
```

To upgrade all uv-managed Python versions:

```
$ uv python upgrade
```

See the [`python upgrade`](../../concepts/python-versions/#upgrading-python-versions) documentation
for more details.

[Next steps](#next-steps)
-------------------------

To learn more about `uv python`, see the [Python version concept](../../concepts/python-versions/)
page and the [command reference](../../reference/cli/#uv-python).

Or, read on to learn how to [run scripts](../scripts/) and invoke Python with uv.

July 17, 2025

Back to top