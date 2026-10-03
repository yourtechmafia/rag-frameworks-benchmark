[Skip to content](#http-credentials)

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
    - [The auth CLI](../cli/)
    - HTTP credentials

      [HTTP credentials](./)



      Table of contents
      * [netrc files](#netrc-files)
      * [The uv credentials store](#the-uv-credentials-store)
      * [Keyring providers](#keyring-providers)
      * [Persistence of credentials](#persistence-of-credentials)
      * [Learn more](#learn-more)
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

* [netrc files](#netrc-files)
* [The uv credentials store](#the-uv-credentials-store)
* [Keyring providers](#keyring-providers)
* [Persistence of credentials](#persistence-of-credentials)
* [Learn more](#learn-more)

1. [Introduction](../../..)
2. [Concepts](../../)
3. [Authentication](../)

[HTTP credentials](#http-credentials)
=====================================

uv supports credentials over HTTP when querying package registries.

Authentication can come from the following sources, in order of precedence:

* The URL, e.g., `https://<user>:<password>@<hostname>/...`
* A [netrc](#netrc-files) configuration file
* The uv credentials store
* A [keyring provider](#keyring-providers) (off by default)

Authentication may be used for hosts specified in the following contexts:

* `[index]`
* `index-url`
* `extra-index-url`
* `find-links`
* `package @ https://...`

[netrc files](#netrc-files)
---------------------------

[`.netrc`](https://everything.curl.dev/usingcurl/netrc) files are a long-standing plain text format
for storing credentials on a system.

Reading credentials from `.netrc` files is always enabled. The target file path will be loaded from
the `NETRC` environment variable if defined, falling back to `~/.netrc` if not.

[The uv credentials store](#the-uv-credentials-store)
-----------------------------------------------------

uv can read and write credentials from a store using the [`uv auth` commands](../cli/).

Credentials are stored in a plaintext file in uv's state directory, e.g.,
`~/.local/share/uv/credentials/credentials.toml` on Unix. This file is currently not intended to be
edited manually.

Note

A secure, system native storage mechanism is in [preview](../../preview/) — it is still
experimental and being actively developed. In the future, this will become the default storage
mechanism.

When enabled, uv will use the secret storage mechanism native to your operating system. On
macOS, it uses the Keychain Services. On Windows, it uses the Windows Credential Manager. On
Linux, it uses the DBus-based Secret Service API.

Currently, uv only searches the native store for credentials it has added to the secret store —
it will not retrieve credentials persisted by other applications.

Set `UV_PREVIEW_FEATURES=native-auth` to use this storage mechanism.

[Keyring providers](#keyring-providers)
---------------------------------------

A keyring provider is a concept from `pip` allowing retrieval of credentials from an interface
matching the popular [keyring](https://github.com/jaraco/keyring) Python package.

The "subprocess" keyring provider invokes the `keyring` command to fetch credentials. uv does not
support additional keyring provider types at this time.

Set `--keyring-provider subprocess`, `UV_KEYRING_PROVIDER=subprocess`, or
`tool.uv.keyring-provider = "subprocess"` to use the provider.

[Persistence of credentials](#persistence-of-credentials)
---------------------------------------------------------

If authentication is found for a single index URL or net location (scheme, host, and port), it will
be cached for the duration of the command and used for other queries to that index or net location.
Authentication is not cached across invocations of uv.

When using `uv add`, uv *will not* persist index credentials to the `pyproject.toml` or `uv.lock`.
These files are often included in source control and distributions, so it is generally unsafe to
include credentials in them. However, uv *will* persist credentials for direct URLs, i.e.,
`package @ https://username:password:example.com/foo.whl`, as there is not currently a way to
otherwise provide those credentials.

If credentials were attached to an index URL during `uv add`, uv may fail to fetch dependencies from
indexes which require authentication on subsequent operations. See the
[index authentication documentation](../../indexes/#authentication) for details on persistent
authentication for indexes.

[Learn more](#learn-more)
-------------------------

See the [index authentication documentation](../../indexes/#authentication) for details on
authenticating index URLs.

See the [`pip` compatibility guide](../../../pip/compatibility/#registry-authentication) for details
on differences from `pip`.

September 2, 2025

Back to top