[Skip to content](#authentication)

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
* [Concepts](../)

  Concepts
  + [Projects](../projects/)

    Projects
    - [Structure and files](../projects/layout/)
    - [Creating projects](../projects/init/)
    - [Managing dependencies](../projects/dependencies/)
    - [Running commands](../projects/run/)
    - [Locking and syncing](../projects/sync/)
    - [Configuring projects](../projects/config/)
    - [Building distributions](../projects/build/)
    - [Exporting lockfiles](../projects/export/)
    - [Using workspaces](../projects/workspaces/)
  + [Tools](../tools/)
  + [Python versions](../python-versions/)
  + [Configuration files](../configuration-files/)
  + [Package indexes](../indexes/)
  + [Resolution](../resolution/)
  + [Build backend](../build-backend/)
  + [Authentication](./)

    Authentication
    - [The auth CLI](cli/)
    - [HTTP credentials](http/)
    - [Git credentials](git/)
    - [TLS certificates](certificates/)
    - [Third-party services](third-party/)
  + [Caching](../cache/)
  + [Preview features](../preview/)
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
2. [Concepts](../)
3. [Authentication](./)

[Authentication](#authentication)
=================================

Authentication is required when working with private repositories or package indexes.

Learn more about authentication in uv:

* [Using the `uv auth` CLI](cli/)
* [HTTP authentication](http/)
* [Git authentication](git/)
* [TLS certificates](certificates/)
* [Third-party services](third-party/)

August 30, 2025

Back to top