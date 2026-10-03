[Skip to content](#using-uv-with-bazel)

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
* [Guides](../../)

  Guides
  + [Installing Python](../../install-python/)
  + [Running scripts](../../scripts/)
  + [Using tools](../../tools/)
  + [Working on projects](../../projects/)
  + [Publishing packages](../../package/)
  + [Migration](../../migration/)

    Migration
    - [From pip to a uv project](../../migration/pip-to-project/)
  + [Integrations](../)

    Integrations
    - [Docker](../docker/)
    - [Jupyter](../jupyter/)
    - [marimo](../marimo/)
    - [GitHub Actions](../github/)
    - [GitLab CI/CD](../gitlab/)
    - [Pre-commit](../pre-commit/)
    - [PyTorch](../pytorch/)
    - [FastAPI](../fastapi/)
    - Bazel

      [Bazel](./)



      Table of contents
      * [Authentication](#authentication)
    - [Azure Artifacts](../azure/)
    - [Google Artifact Registry](../google/)
    - [AWS CodeArtifact](../aws/)
    - [JFrog Artifactory](../jfrog/)
    - [Renovate](../renovate/)
    - [Dependabot](../dependabot/)
    - [AWS Lambda](../aws-lambda/)
    - [Coiled](../coiled/)
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

* [Authentication](#authentication)

1. [Introduction](../../..)
2. [Guides](../../)
3. [Integrations](../)

[Using uv with Bazel](#using-uv-with-bazel)
===========================================

For broader Bazel workflows with uv, see the
[`rules_py` uv guide](https://github.com/aspect-build/rules_py#dependency-resolution-with-uv) or the
[`rules_python` uv guide](https://rules-python.readthedocs.io/en/latest/pypi/lock.html#uv-pip-compile-bzlmod-only).

[Authentication](#authentication)
---------------------------------

Bazel 7 and newer supports credential helpers via the `--credential_helper` option. To use
credentials stored by uv for Bazel fetches, first authenticate uv with the service that hosts the
files Bazel needs to fetch:

```
$ uv auth login https://packages.example.com
```

Then, configure Bazel to invoke
[`uv auth helper`](../../../concepts/authentication/cli/#using-credentials-with-external-tools) for
matching hosts:

.bazelrc

```
common --credential_helper=packages.example.com=%workspace%/bazel/uv-auth-helper
common --credential_helper=files.example.com=%workspace%/bazel/uv-auth-helper
```

Replace the host patterns with the hosts that serve the index and files Bazel will fetch.

Finally, add the wrapper script referenced by `.bazelrc`:

bazel/uv-auth-helper

```
#!/usr/bin/env bash
exec uv --preview-features auth-helper auth helper --protocol=bazel "$@"
```

The script must be executable:

```
$ chmod +x bazel/uv-auth-helper
```

May 13, 2026

Back to top