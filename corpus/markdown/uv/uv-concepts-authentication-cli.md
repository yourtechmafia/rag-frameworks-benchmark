[Skip to content](#the-uv-auth-cli)

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
  + [Projects](../../projects/)

    Projects
    - [Structure and files](../../projects/layout/)
    - [Creating projects](../../projects/init/)
    - [Managing dependencies](../../projects/dependencies/)
    - [Running commands](../../projects/run/)
    - [Locking and syncing](../../projects/sync/)
    - [Configuring projects](../../projects/config/)
    - [Building distributions](../../projects/build/)
    - [Exporting lockfiles](../../projects/export/)
    - [Using workspaces](../../projects/workspaces/)
  + [Tools](../../tools/)
  + [Python versions](../../python-versions/)
  + [Configuration files](../../configuration-files/)
  + [Package indexes](../../indexes/)
  + [Resolution](../../resolution/)
  + [Build backend](../../build-backend/)
  + [Authentication](../)

    Authentication
    - The auth CLI

      [The auth CLI](./)



      Table of contents
      * [Logging in to a service](#logging-in-to-a-service)
      * [Logging out of a service](#logging-out-of-a-service)
      * [Showing credentials for a service](#showing-credentials-for-a-service)
      * [Using credentials with external tools](#using-credentials-with-external-tools)
      * [Configuring the storage backend](#configuring-the-storage-backend)
    - [HTTP credentials](../http/)
    - [Git credentials](../git/)
    - [TLS certificates](../certificates/)
    - [Third-party services](../third-party/)
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

* [Logging in to a service](#logging-in-to-a-service)
* [Logging out of a service](#logging-out-of-a-service)
* [Showing credentials for a service](#showing-credentials-for-a-service)
* [Using credentials with external tools](#using-credentials-with-external-tools)
* [Configuring the storage backend](#configuring-the-storage-backend)

1. [Introduction](../../..)
2. [Concepts](../../)
3. [Authentication](../)

[The `uv auth` CLI](#the-uv-auth-cli)
=====================================

uv provides a high-level interface for storing and retrieving credentials from services.

[Logging in to a service](#logging-in-to-a-service)
---------------------------------------------------

To add credentials for service, use the `uv auth login` command:

```
$ uv auth login example.com
```

This will prompt for the credentials.

The credentials can also be provided using the `--username` and `--password` options, or the
`--token` option for services which use a `__token__` or arbitrary username.

Note

We recommend providing the secret via stdin. Use `-` to indicate the value should be read from
stdin, e.g., for `--password`:

```
$ echo 'my-password' | uv auth login example.com --password -
```

The same pattern can be used with `--token`.

Once credentials are added, uv will use them for packaging operations that require fetching content
from the given service. At this time, only HTTPS Basic authentication is supported. The credentials
will not yet be used for Git requests.

Note

The credentials will not be validated, i.e., incorrect credentials will not fail.

[Logging out of a service](#logging-out-of-a-service)
-----------------------------------------------------

To remove credentials, use the `uv auth logout` command:

```
$ uv auth logout example.com
```

Note

The credentials will not be invalidated with the remote server, i.e., they will only be removed
from local storage not rendered unusable.

[Showing credentials for a service](#showing-credentials-for-a-service)
-----------------------------------------------------------------------

To show the credential stored for a given URL, use the `uv auth token` command:

```
$ uv auth token example.com
```

If a username was used to log in, it will need to be provided as well, e.g.:

```
$ uv auth token --username foo example.com
```

[Using credentials with external tools](#using-credentials-with-external-tools)
-------------------------------------------------------------------------------

`uv auth helper` allows tools that support credential helpers to request HTTP credentials from uv.
At this time, uv supports the
[Bazel credential helper protocol](https://github.com/bazelbuild/proposals/blob/main/designs/2022-06-07-bazel-credential-helpers.md).

The command is intended to be invoked by external tools. It reads a JSON request from stdin and
writes a JSON response to stdout. When matching credentials are available, the response includes the
`Authorization` header:

```
$ echo '{"uri": "https://example.com/path"}' | uv --preview-features auth-helper auth helper --protocol=bazel get
{"headers":{"Authorization":["Basic ..."]}}
```

If no credentials are found, uv will return an empty set of headers:

```
{ "headers": {} }
```

Note

`uv auth helper` is experimental. Use `--preview-features auth-helper` or
`UV_PREVIEW_FEATURES=auth-helper` to disable the warning.

The [Bazel integration guide](../../../guides/integration/bazel/) explains how to use this command
with Bazel.

[Configuring the storage backend](#configuring-the-storage-backend)
-------------------------------------------------------------------

Credentials are persisted to the uv [credentials store](../http/#the-uv-credentials-store).

By default, credentials are written to a plaintext file. An encrypted system-native storage backend
can be enabled with `UV_PREVIEW_FEATURES=native-auth`.

May 13, 2026

Back to top