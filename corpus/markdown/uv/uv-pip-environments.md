[Skip to content](#using-python-environments)

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
  + [The pip interface](../)

    The pip interface
    - Using environments

      [Using environments](./)



      Table of contents
      * [Creating a virtual environment](#creating-a-virtual-environment)
      * [Using a virtual environment](#using-a-virtual-environment)
      * [Deactivating an environment](#deactivating-an-environment)
      * [Using arbitrary Python environments](#using-arbitrary-python-environments)
      * [Discovery of Python environments](#discovery-of-python-environments)
    - [Managing packages](../packages/)
    - [Inspecting environments](../inspection/)
    - [Declaring dependencies](../dependencies/)
    - [Locking environments](../compile/)
    - [Compatibility with pip](../compatibility/)
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

* [Creating a virtual environment](#creating-a-virtual-environment)
* [Using a virtual environment](#using-a-virtual-environment)
* [Deactivating an environment](#deactivating-an-environment)
* [Using arbitrary Python environments](#using-arbitrary-python-environments)
* [Discovery of Python environments](#discovery-of-python-environments)

1. [Introduction](../..)
2. [Concepts](../../concepts/)
3. [The pip interface](../)

[Using Python environments](#using-python-environments)
=======================================================

Each Python installation has an environment that is active when Python is used. Packages can be
installed into an environment to make their modules available from your Python scripts. Generally,
it is considered best practice not to modify a Python installation's environment. This is especially
important for Python installations that come with the operating system which often manage the
packages themselves. A virtual environment is a lightweight way to isolate packages from a Python
installation's environment. Unlike `pip`, uv requires using a virtual environment by default.

[Creating a virtual environment](#creating-a-virtual-environment)
-----------------------------------------------------------------

uv supports creating virtual environments, e.g., to create a virtual environment at `.venv`:

```
$ uv venv
```

A specific name or path can be specified, e.g., to create a virtual environment at `my-name`:

```
$ uv venv my-name
```

A Python version can be requested, e.g., to create a virtual environment with Python 3.11:

```
$ uv venv --python 3.11
```

Note this requires the requested Python version to be available on the system. However, if
unavailable, uv will download Python for you. See the
[Python version](../../concepts/python-versions/) documentation for more details.

[Using a virtual environment](#using-a-virtual-environment)
-----------------------------------------------------------

When using the default virtual environment name, uv will automatically find and use the virtual
environment during subsequent invocations.

```
$ uv venv

$ # Install a package in the new virtual environment
$ uv pip install ruff
```

The virtual environment can be "activated" to make its packages available:

macOS and LinuxWindows

```
$ source .venv/bin/activate
```

```
PS> .venv\Scripts\activate
```

Note

The default activation script on Unix is for POSIX compliant shells like `sh`, `bash`, or `zsh`.
There are additional activation scripts for common alternative shells.

fishcsh / tcshNushell

```
$ source .venv/bin/activate.fish
```

```
$ source .venv/bin/activate.csh
```

```
$ use .venv\Scripts\activate.nu
```

[Deactivating an environment](#deactivating-an-environment)
-----------------------------------------------------------

To exit a virtual environment, use the `deactivate` command:

```
$ deactivate
```

[Using arbitrary Python environments](#using-arbitrary-python-environments)
---------------------------------------------------------------------------

Since uv has no dependency on Python, it can install into virtual environments other than its own.
For example, setting `VIRTUAL_ENV=/path/to/venv` will cause uv to install into `/path/to/venv`,
regardless of where uv is installed. Note that if `VIRTUAL_ENV` is set to a directory that is
**not** a [PEP 405 compliant](https://peps.python.org/pep-0405/#specification) virtual environment,
it will be ignored.

uv can also install into arbitrary, even non-virtual environments, with the `--python` option. For
example, `uv pip install --python /path/to/python` will install into the environment linked to the
`/path/to/python` interpreter regardless of whether or not it is a virtual environment. The
`--python` option also accepts a path to the root directory of a virtual environment.

For convenience, `uv pip install --system` will install into the system Python environment. Using
`--system` is roughly equivalent to `uv pip install --python $(which python)`, but note that
executables that are linked to virtual environments will be skipped. Although we generally recommend
using virtual environments for dependency management, `--system` is appropriate in continuous
integration and containerized environments.

The `--system` flag is also used to opt in to mutating system environments. For example, the
`--python` argument can be used to request a Python version (e.g., `--python 3.12`), and uv will
search for an interpreter that meets the request. If uv finds a system interpreter (e.g.,
`/usr/lib/python3.12`), then the `--system` flag is required to allow modification of this
non-virtual Python environment. Without the `--system` flag, uv will ignore any interpreters that
are not in virtual environments. Conversely, when the `--system` flag is provided, uv will ignore
any interpreters that *are* in virtual environments.

Installing into system Python across platforms and distributions is notoriously difficult. uv
supports the common cases, but will not work in all cases. For example, installing into system
Python on Debian prior to Python 3.10 is unsupported due to the
[distribution's patching of `distutils` (but not `sysconfig`)](https://ffy00.github.io/blog/02-python-debian-and-the-install-locations/).
While we always recommend the use of virtual environments, uv considers them to be required in these
non-standard environments.

If uv is installed in a Python environment, e.g., with `pip`, it can still be used to modify other
environments. However, when invoked with `python -m uv`, uv will default to using the parent
interpreter's environment. Invoking uv via Python adds startup overhead and is not recommended for
general usage.

uv itself does not depend on Python, but it does need to locate a Python environment to (1) install
dependencies into the environment and (2) build source distributions.

[Discovery of Python environments](#discovery-of-python-environments)
---------------------------------------------------------------------

When running a command that mutates an environment such as `uv pip sync` or `uv pip install`, uv
will search for a virtual environment in the following order:

* An activated virtual environment based on the `VIRTUAL_ENV` environment variable.
* An activated Conda environment based on the `CONDA_PREFIX` environment variable.
* A virtual environment at `.venv` in the current directory, or in the nearest parent directory.

If no virtual environment is found, uv will prompt the user to create one in the current directory
via `uv venv`.

If the `--system` flag is included, uv will skip virtual environments search for an installed Python
version. Similarly, when running a command that does not mutate the environment such as
`uv pip compile`, uv does not *require* a virtual environment — however, a Python interpreter is
still required. See the documentation on
[Python discovery](../../concepts/python-versions/#discovery-of-python-versions) for details on the
discovery of installed Python versions.

March 24, 2026

Back to top