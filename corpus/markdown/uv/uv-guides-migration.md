[Skip to content](#migration-guides)

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
  + [Installing Python](../install-python/)
  + [Running scripts](../scripts/)
  + [Using tools](../tools/)
  + [Working on projects](../projects/)
  + [Publishing packages](../package/)
  + [Migration](./)

    Migration
    - [From pip to a uv project](pip-to-project/)
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

1. [Introduction](../..)
2. [Guides](../)
3. [Migration](./)

[Migration guides](#migration-guides)
=====================================

Learn how to migrate from other tools to uv:

* [Migrate from pip to uv projects](pip-to-project/)

Note

Other guides, such as migrating from another project management tool, or from pip to `uv pip`
are not yet available. See [#5200](https://github.com/astral-sh/uv/issues/5200) to track
progress.

Or, explore the [integration guides](../integration/) to learn how to use uv with other
software.

July 2, 2025

Back to top