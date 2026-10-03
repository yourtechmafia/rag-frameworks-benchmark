[Skip to content](#versioning)

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
    - Versioning

      [Versioning](./)



      Table of contents
      * [Crate versioning](#crate-versioning)
      * [Cache versioning](#cache-versioning)
      * [Lockfile versioning](#lockfile-versioning)
    - [Platform support](../platforms/)
    - [Python support](../python/)
    - [Rust support](../rust/)
    - [License](../license/)

Table of contents

* [Crate versioning](#crate-versioning)
* [Cache versioning](#cache-versioning)
* [Lockfile versioning](#lockfile-versioning)

1. [Introduction](../../..)
2. [Reference](../../)
3. [Policies](../)

[Versioning](#versioning)
=========================

uv is widely used in production and is stable software.

uv uses a custom versioning scheme in which the minor version number is bumped for breaking changes,
and the patch version number is bumped for bug fixes, enhancements, and other non-breaking changes.

The care we take in backwards-incompatible changes is proportional to the expected real-world
impact, not a function of arbitrary version numbering policies. We value the ability to iterate on
new features quickly and gather changes that *could* be breaking into clearly marked releases.

uv's changelog can be [viewed on GitHub](https://github.com/astral-sh/uv/blob/main/CHANGELOG.md).

[Crate versioning](#crate-versioning)
-------------------------------------

uv's crates are published to [crates.io](https://crates.io). The following crates follow the normal
uv versioning policy:

* `uv`
* `uv-build`
* `uv-version`

The `uv` and `uv-build` crates are versioned by the binary command-line interface. The Rust
interface of these crates does not follow semantic versioning.

The remainder of uv's crates provide **no stability guarantees**. The Rust interface is considered
internal and unstable. Consequently, they are versioned as `0.0.x`. The patch version is incremented
on every uv release, regardless of changes to the crate.

[Cache versioning](#cache-versioning)
-------------------------------------

Cache versions are considered internal to uv, and so may be changed in a minor or patch release. See
[Cache versioning](../../../concepts/cache/#cache-versioning) for more.

[Lockfile versioning](#lockfile-versioning)
-------------------------------------------

The `uv.lock` schema version is considered part of the public API, and so will only be incremented
in a minor release as a breaking change. See
[Lockfile versioning](../../../concepts/resolution/#lockfile-versioning) for more.

January 16, 2026

Back to top