[Skip to content](#declaring-dependencies)

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
    - [Using environments](../environments/)
    - [Managing packages](../packages/)
    - [Inspecting environments](../inspection/)
    - Declaring dependencies

      [Declaring dependencies](./)



      Table of contents
      * [Using pyproject.toml](#using-pyprojecttoml)
      * [Using requirements.in](#using-requirementsin)
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

* [Using pyproject.toml](#using-pyprojecttoml)
* [Using requirements.in](#using-requirementsin)

1. [Introduction](../..)
2. [Concepts](../../concepts/)
3. [The pip interface](../)

[Declaring dependencies](#declaring-dependencies)
=================================================

It is best practice to declare dependencies in a static file instead of modifying environments with
ad-hoc installations. Once dependencies are defined, they can be [locked](../compile/) to create a
consistent, reproducible environment.

[Using `pyproject.toml`](#using-pyprojecttoml)
----------------------------------------------

The `pyproject.toml` file is the Python standard for defining configuration for a project.

To define project dependencies in a `pyproject.toml` file:

pyproject.toml

```
[project]
dependencies = [
  "httpx",
  "ruff>=0.3.0"
]
```

To define optional dependencies in a `pyproject.toml` file:

pyproject.toml

```
[project.optional-dependencies]
cli = [
  "rich",
  "click",
]
```

Each of the keys defines an "extra", which can be installed using the `--extra` and `--all-extras`
flags or `package[<extra>]` syntax. See the documentation on
[installing packages](../packages/#installing-packages-from-files) for more details.

See the official
[`pyproject.toml` guide](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) for
more details on getting started with a `pyproject.toml`.

[Using `requirements.in`](#using-requirementsin)
------------------------------------------------

It is also common to use a lightweight
[requirements file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/) to
declare the dependencies for the project. Each requirement is defined on its own line. Commonly,
this file is called `requirements.in` to distinguish it from `requirements.txt` which is used for
the locked dependencies.

To define dependencies in a `requirements.in` file:

requirements.in

```
httpx
ruff>=0.3.0
```

Optional dependencies groups are not supported in this format.

July 23, 2026

Back to top