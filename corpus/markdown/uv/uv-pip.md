[Skip to content](#the-pip-interface)

[![logo](../assets/logo-letter.svg)](.. "uv")
uv

[uv](https://github.com/astral-sh/uv "Go to repository")

* [Introduction](..)
* [Getting started](../getting-started/)

  Getting started
  + [Installation](../getting-started/installation/)
  + [First steps](../getting-started/first-steps/)
  + [Features](../getting-started/features/)
  + [Getting help](../getting-started/help/)
* [Guides](../guides/)

  Guides
  + [Installing Python](../guides/install-python/)
  + [Running scripts](../guides/scripts/)
  + [Using tools](../guides/tools/)
  + [Working on projects](../guides/projects/)
  + [Publishing packages](../guides/package/)
  + [Migration](../guides/migration/)

    Migration
    - [From pip to a uv project](../guides/migration/pip-to-project/)
  + [Integrations](../guides/integration/)

    Integrations
    - [Docker](../guides/integration/docker/)
    - [Jupyter](../guides/integration/jupyter/)
    - [marimo](../guides/integration/marimo/)
    - [GitHub Actions](../guides/integration/github/)
    - [GitLab CI/CD](../guides/integration/gitlab/)
    - [Pre-commit](../guides/integration/pre-commit/)
    - [PyTorch](../guides/integration/pytorch/)
    - [FastAPI](../guides/integration/fastapi/)
    - [Bazel](../guides/integration/bazel/)
    - [Azure Artifacts](../guides/integration/azure/)
    - [Google Artifact Registry](../guides/integration/google/)
    - [AWS CodeArtifact](../guides/integration/aws/)
    - [JFrog Artifactory](../guides/integration/jfrog/)
    - [Renovate](../guides/integration/renovate/)
    - [Dependabot](../guides/integration/dependabot/)
    - [AWS Lambda](../guides/integration/aws-lambda/)
    - [Coiled](../guides/integration/coiled/)
* [Concepts](../concepts/)

  Concepts
  + [Projects](../concepts/projects/)

    Projects
    - [Structure and files](../concepts/projects/layout/)
    - [Creating projects](../concepts/projects/init/)
    - [Managing dependencies](../concepts/projects/dependencies/)
    - [Running commands](../concepts/projects/run/)
    - [Locking and syncing](../concepts/projects/sync/)
    - [Configuring projects](../concepts/projects/config/)
    - [Building distributions](../concepts/projects/build/)
    - [Exporting lockfiles](../concepts/projects/export/)
    - [Using workspaces](../concepts/projects/workspaces/)
  + [Tools](../concepts/tools/)
  + [Python versions](../concepts/python-versions/)
  + [Configuration files](../concepts/configuration-files/)
  + [Package indexes](../concepts/indexes/)
  + [Resolution](../concepts/resolution/)
  + [Build backend](../concepts/build-backend/)
  + [Authentication](../concepts/authentication/)

    Authentication
    - [The auth CLI](../concepts/authentication/cli/)
    - [HTTP credentials](../concepts/authentication/http/)
    - [Git credentials](../concepts/authentication/git/)
    - [TLS certificates](../concepts/authentication/certificates/)
    - [Third-party services](../concepts/authentication/third-party/)
  + [Caching](../concepts/cache/)
  + [Preview features](../concepts/preview/)
  + [The pip interface](./)

    The pip interface
    - [Using environments](environments/)
    - [Managing packages](packages/)
    - [Inspecting environments](inspection/)
    - [Declaring dependencies](dependencies/)
    - [Locking environments](compile/)
    - [Compatibility with pip](compatibility/)
* [Reference](../reference/)

  Reference
  + [Commands](../reference/cli/)
  + [Settings](../reference/settings/)
  + [Environment variables](../reference/environment/)
  + [Storage](../reference/storage/)
  + [Installer options](../reference/installer/)
  + [Troubleshooting](../reference/troubleshooting/)

    Troubleshooting
    - [Build failures](../reference/troubleshooting/build-failures/)
    - [Reproducible examples](../reference/troubleshooting/reproducible-examples/)
  + [Contributing](../reference/contributing/)
  + [Internals](../reference/internals/)

    Internals
    - [Resolver](../reference/internals/resolver/)
    - [Workspace Metadata](../reference/internals/metadata/)
  + [Benchmarks](../reference/benchmarks/)
  + [Policies](../reference/policies/)

    Policies
    - [Versioning](../reference/policies/versioning/)
    - [Platform support](../reference/policies/platforms/)
    - [Python support](../reference/policies/python/)
    - [Rust support](../reference/policies/rust/)
    - [License](../reference/policies/license/)

1. [Introduction](..)
2. [Concepts](../concepts/)
3. [The pip interface](./)

[The pip interface](#the-pip-interface)
=======================================

uv provides a drop-in replacement for common `pip`, `pip-tools`, and `virtualenv` commands. These
commands work directly with the virtual environment, in contrast to uv's primary interfaces where
the virtual environment is managed automatically. The `uv pip` interface exposes the speed and
functionality of uv to power users and projects that are not ready to transition away from `pip` and
`pip-tools`.

The following sections discuss the basics of using `uv pip`:

* [Creating and using environments](environments/)
* [Installing and managing packages](packages/)
* [Inspecting environments and packages](inspection/)
* [Declaring package dependencies](dependencies/)
* [Locking and syncing environments](compile/)

Please note these commands do not *exactly* implement the interfaces and behavior of the tools they
are based on. The further you stray from common workflows, the more likely you are to encounter
differences. Consult the [pip-compatibility guide](compatibility/) for details.

Important

uv does not rely on or invoke pip. The pip interface is named as such to highlight its dedicated
purpose of providing low-level commands that match pip's interface and to separate it from the
rest of uv's commands which operate at a higher level of abstraction.

August 8, 2024

Back to top