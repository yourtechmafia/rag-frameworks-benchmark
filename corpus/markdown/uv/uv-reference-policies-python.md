[Skip to content](#python-support)

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
* [Concepts](../../../concepts/)

  Concepts
  + [Projects](../../../concepts/projects/)

    Projects
    - [Structure and files](../../../concepts/projects/layout/)
    - [Creating projects](../../../concepts/projects/init/)
    - [Managing dependencies](../../../concepts/projects/dependencies/)
    - [Running commands](../../../concepts/projects/run/)
    - [Locking and syncing](../../../concepts/projects/sync/)
    - [Configuring projects](../../../concepts/projects/config/)
    - [Building distributions](../../../concepts/projects/build/)
    - [Exporting lockfiles](../../../concepts/projects/export/)
    - [Using workspaces](../../../concepts/projects/workspaces/)
  + [Tools](../../../concepts/tools/)
  + [Python versions](../../../concepts/python-versions/)
  + [Configuration files](../../../concepts/configuration-files/)
  + [Package indexes](../../../concepts/indexes/)
  + [Resolution](../../../concepts/resolution/)
  + [Build backend](../../../concepts/build-backend/)
  + [Authentication](../../../concepts/authentication/)

    Authentication
    - [The auth CLI](../../../concepts/authentication/cli/)
    - [HTTP credentials](../../../concepts/authentication/http/)
    - [Git credentials](../../../concepts/authentication/git/)
    - [TLS certificates](../../../concepts/authentication/certificates/)
    - [Third-party services](../../../concepts/authentication/third-party/)
  + [Caching](../../../concepts/cache/)
  + [Preview features](../../../concepts/preview/)
  + [The pip interface](../../../pip/)

    The pip interface
    - [Using environments](../../../pip/environments/)
    - [Managing packages](../../../pip/packages/)
    - [Inspecting environments](../../../pip/inspection/)
    - [Declaring dependencies](../../../pip/dependencies/)
    - [Locking environments](../../../pip/compile/)
    - [Compatibility with pip](../../../pip/compatibility/)
* [Reference](../../)

  Reference
  + [Commands](../../cli/)
  + [Settings](../../settings/)
  + [Environment variables](../../environment/)
  + [Storage](../../storage/)
  + [Installer options](../../installer/)
  + [Troubleshooting](../../troubleshooting/)

    Troubleshooting
    - [Build failures](../../troubleshooting/build-failures/)
    - [Reproducible examples](../../troubleshooting/reproducible-examples/)
  + [Contributing](../../contributing/)
  + [Internals](../../internals/)

    Internals
    - [Resolver](../../internals/resolver/)
    - [Workspace Metadata](../../internals/metadata/)
  + [Benchmarks](../../benchmarks/)
  + [Policies](../)

    Policies
    - [Versioning](../versioning/)
    - [Platform support](../platforms/)
    - Python support

      [Python support](./)



      Table of contents
      * [Python versions](#python-versions)
      * [Python implementations](#python-implementations)
    - [Rust support](../rust/)
    - [License](../license/)

Table of contents

* [Python versions](#python-versions)
* [Python implementations](#python-implementations)

1. [Introduction](../../..)
2. [Reference](../../)
3. [Policies](../)

[Python support](#python-support)
=================================

[Python versions](#python-versions)
-----------------------------------

uv has Tier 1 support for the following Python versions:

* 3.10
* 3.11
* 3.12
* 3.13
* 3.14

As with [platforms](../platforms/), Tier 1 support can be thought of "guaranteed to work". uv is
continuously tested against these versions.

uv has Tier 2 support for:

* 3.6
* 3.7
* 3.8
* 3.9

uv is "expected to work" with these versions. uv is tested against these versions, but they have
reached their [end-of-life](https://devguide.python.org/versions/) and no longer receive security
fixes. We do not recommend using these versions.

uv also has Tier 2 support for pre-releases of Python 3.15.

uv does not work with Python versions prior to 3.6.

[Python implementations](#python-implementations)
-------------------------------------------------

uv has Tier 1 support for the following Python implementations:

* CPython

As with [platforms](../platforms/), Tier 1 support can be thought of "guaranteed to work". uv
supports managed installations of these implementations, and the builds are maintained by Astral.

uv has Tier 2 support for:

* PyPy
* GraalPy
* Pyodide

uv is "expected to work" with these implementations. uv also supports managed installations of these
Python implementations, but the builds are not maintained by Astral.

uv has Tier 3 support for:

* Pyston

uv "should work" with these implementations, but stability may vary.

March 19, 2026

Back to top