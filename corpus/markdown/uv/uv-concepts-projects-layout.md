[Skip to content](#project-structure-and-files)

[![logo](../../../assets/logo-letter.svg)](../../.. "uv")
uv

[uv](https://github.com/astral-sh/uv "Go to repository")

* [Introduction](../../..)
* [Getting started](../../../getting-started/)

  Getting started
  + [Installation](../../../getting-started/installation/)
  + [First steps](../../../getting-started/first-steps/)
  + [Features](../../../getting-started/features/)
  + [Getting help](../../../getting-started/help/)
* [Guides](../../../guides/)

  Guides
  + [Installing Python](../../../guides/install-python/)
  + [Running scripts](../../../guides/scripts/)
  + [Using tools](../../../guides/tools/)
  + [Working on projects](../../../guides/projects/)
  + [Publishing packages](../../../guides/package/)
  + [Migration](../../../guides/migration/)

    Migration
    - [From pip to a uv project](../../../guides/migration/pip-to-project/)
  + [Integrations](../../../guides/integration/)

    Integrations
    - [Docker](../../../guides/integration/docker/)
    - [Jupyter](../../../guides/integration/jupyter/)
    - [marimo](../../../guides/integration/marimo/)
    - [GitHub Actions](../../../guides/integration/github/)
    - [GitLab CI/CD](../../../guides/integration/gitlab/)
    - [Pre-commit](../../../guides/integration/pre-commit/)
    - [PyTorch](../../../guides/integration/pytorch/)
    - [FastAPI](../../../guides/integration/fastapi/)
    - [Bazel](../../../guides/integration/bazel/)
    - [Azure Artifacts](../../../guides/integration/azure/)
    - [Google Artifact Registry](../../../guides/integration/google/)
    - [AWS CodeArtifact](../../../guides/integration/aws/)
    - [JFrog Artifactory](../../../guides/integration/jfrog/)
    - [Renovate](../../../guides/integration/renovate/)
    - [Dependabot](../../../guides/integration/dependabot/)
    - [AWS Lambda](../../../guides/integration/aws-lambda/)
    - [Coiled](../../../guides/integration/coiled/)
* [Concepts](../../)

  Concepts
  + [Projects](../)

    Projects
    - Structure and files

      [Structure and files](./)



      Table of contents
      * [The pyproject.toml](#the-pyprojecttoml)
      * [The project environment](#the-project-environment)

        + [Centralized project environments](#centralized-project-environments)
      * [The lockfile](#the-lockfile)

        + [Relationship to pylock.toml](#relationship-to-pylocktoml)
    - [Creating projects](../init/)
    - [Managing dependencies](../dependencies/)
    - [Running commands](../run/)
    - [Locking and syncing](../sync/)
    - [Configuring projects](../config/)
    - [Building distributions](../build/)
    - [Exporting lockfiles](../export/)
    - [Using workspaces](../workspaces/)
  + [Tools](../../tools/)
  + [Python versions](../../python-versions/)
  + [Configuration files](../../configuration-files/)
  + [Package indexes](../../indexes/)
  + [Resolution](../../resolution/)
  + [Build backend](../../build-backend/)
  + [Authentication](../../authentication/)

    Authentication
    - [The auth CLI](../../authentication/cli/)
    - [HTTP credentials](../../authentication/http/)
    - [Git credentials](../../authentication/git/)
    - [TLS certificates](../../authentication/certificates/)
    - [Third-party services](../../authentication/third-party/)
  + [Caching](../../cache/)
  + [Preview features](../../preview/)
  + [The pip interface](../../../pip/)

    The pip interface
    - [Using environments](../../../pip/environments/)
    - [Managing packages](../../../pip/packages/)
    - [Inspecting environments](../../../pip/inspection/)
    - [Declaring dependencies](../../../pip/dependencies/)
    - [Locking environments](../../../pip/compile/)
    - [Compatibility with pip](../../../pip/compatibility/)
* [Reference](../../../reference/)

  Reference
  + [Commands](../../../reference/cli/)
  + [Settings](../../../reference/settings/)
  + [Environment variables](../../../reference/environment/)
  + [Storage](../../../reference/storage/)
  + [Installer options](../../../reference/installer/)
  + [Troubleshooting](../../../reference/troubleshooting/)

    Troubleshooting
    - [Build failures](../../../reference/troubleshooting/build-failures/)
    - [Reproducible examples](../../../reference/troubleshooting/reproducible-examples/)
  + [Contributing](../../../reference/contributing/)
  + [Internals](../../../reference/internals/)

    Internals
    - [Resolver](../../../reference/internals/resolver/)
    - [Workspace Metadata](../../../reference/internals/metadata/)
  + [Benchmarks](../../../reference/benchmarks/)
  + [Policies](../../../reference/policies/)

    Policies
    - [Versioning](../../../reference/policies/versioning/)
    - [Platform support](../../../reference/policies/platforms/)
    - [Python support](../../../reference/policies/python/)
    - [Rust support](../../../reference/policies/rust/)
    - [License](../../../reference/policies/license/)

Table of contents

* [The pyproject.toml](#the-pyprojecttoml)
* [The project environment](#the-project-environment)

  + [Centralized project environments](#centralized-project-environments)
* [The lockfile](#the-lockfile)

  + [Relationship to pylock.toml](#relationship-to-pylocktoml)

1. [Introduction](../../..)
2. [Concepts](../../)
3. [Projects](../)

[Project structure and files](#project-structure-and-files)
===========================================================

[The `pyproject.toml`](#the-pyprojecttoml)
------------------------------------------

Python project metadata is defined in a
[`pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) file. uv
requires this file to identify the root directory of a project.

Tip

`uv init` can be used to create a new project. See [Creating projects](../init/) for
details.

A minimal project definition includes a name and version:

pyproject.toml

```
[project]
name = "example"
version = "0.1.0"
```

Additional project metadata and configuration includes:

* [Python version requirement](../config/#python-version-requirement)
* [Dependencies](../dependencies/)
* [Build system](../config/#build-systems)
* [Entry points (commands)](../config/#entry-points)

[The project environment](#the-project-environment)
---------------------------------------------------

When working on a project with uv, uv will create a virtual environment as needed. While some uv
commands will create a temporary environment (e.g., `uv run --isolated`), uv also manages a
persistent environment with the project and its dependencies in a `.venv` directory next to the
`pyproject.toml`. By default, it is stored inside the project to make it easy for editors to find —
they need the environment to give code completions and type hints. It is not recommended to include
the `.venv` directory in version control; it is automatically excluded from `git` with an internal
`.gitignore` file.

To run a command in the project environment, use `uv run`. Alternatively the project environment can
be activated as normal for a virtual environment.

When `uv run` is invoked, it will create the project environment if it does not exist yet or ensure
it is up-to-date if it exists. The project environment can also be explicitly created with
`uv sync`. See the [locking and syncing](../sync/) documentation for details.

It is *not* recommended to modify the project environment manually, e.g., with `uv pip install`. For
project dependencies, use `uv add` to add a package to the environment. For one-off requirements,
use [`uvx`](../../../guides/tools/) or
[`uv run --with`](../run/#requesting-additional-dependencies).

Tip

If you don't want uv to manage the project environment, set [`managed = false`](../../../reference/settings/#managed)
to disable automatic locking and syncing of the project. For example:

pyproject.toml

```
[tool.uv]
managed = false
```

### [Centralized project environments](#centralized-project-environments)

With the [`centralized-project-envs` preview feature](../../preview/), uv stores the default project
environment in its cache. uv attempts to maintain a `.venv` directory link to the cached environment
so existing activation and editor workflows can continue to use the usual path. If link creation
fails, uv attempts to write the cached environment path to `.venv` instead. If both attempts fail,
uv continues using the cached environment directly, but tools relying on `.venv` may not discover
it. Switching interpreters selects separate cached environments and can reuse them later.

Explicit project environment paths, including `UV_PROJECT_ENVIRONMENT` and environments selected
with `--active`, are not centralized. The feature has no effect when `--no-cache` is enabled.

The feature also applies to pathless `uv venv` invocations from a project or workspace root.

[The lockfile](#the-lockfile)
-----------------------------

uv creates a `uv.lock` file next to the `pyproject.toml`.

`uv.lock` is a *universal* or *cross-platform* lockfile that captures the packages that would be
installed across all possible Python markers such as operating system, architecture, and Python
version.

Unlike the `pyproject.toml`, which is used to specify the broad requirements of your project, the
lockfile contains the exact resolved versions that are installed in the project environment. This
file should be checked into version control, allowing for consistent and reproducible installations
across machines.

A lockfile ensures that developers working on the project are using a consistent set of package
versions. Additionally, it ensures when deploying the project as an application that the exact set
of used package versions is known.

The lockfile is [automatically created and updated](../sync/#automatic-lock-and-sync) during uv
invocations that use the project environment, i.e., `uv sync` and `uv run`. The lockfile may also be
explicitly updated using `uv lock`.

`uv.lock` is a human-readable TOML file but is managed by uv and should not be edited manually. The
`uv.lock` format is specific to uv and not usable by other tools.

### [Relationship to `pylock.toml`](#relationship-to-pylocktoml)

In [PEP 751](https://peps.python.org/pep-0751/), Python standardized a new resolution file format,
`pylock.toml`.

`pylock.toml` is a resolution output format intended to replace `requirements.txt` (e.g., in the
context of `uv pip compile`, whereby a "locked" `requirements.txt` file is generated from a set of
input requirements). `pylock.toml` is standardized and tool-agnostic, such that in the future,
`pylock.toml` files generated by uv could be installed by other tools, and vice versa.

Some of uv's functionality cannot be expressed in the `pylock.toml` format; as such, uv will
continue to use the `uv.lock` format within the project interface.

However, uv supports `pylock.toml` as an export target and in the `uv pip` CLI. For example:

* To export a `uv.lock` to the `pylock.toml` format, run: `uv export -o pylock.toml`
* To generate a `pylock.toml` file from a set of requirements, run:
  `uv pip compile requirements.in -o pylock.toml`
* To install from a `pylock.toml` file, run: `uv pip sync pylock.toml` or
  `uv pip install -r pylock.toml`

July 21, 2026

Back to top