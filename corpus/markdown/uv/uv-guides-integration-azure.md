[Skip to content](#azure-artifacts)

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
    - [Bazel](../bazel/)
    - Azure Artifacts

      [Azure Artifacts](./)



      Table of contents
      * [Authenticate with an Azure access token](#authenticate-with-an-azure-access-token)
      * [Authenticate with keyring and artifacts-keyring](#authenticate-with-keyring-and-artifacts-keyring)
      * [Publishing packages](#publishing-packages)
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

* [Authenticate with an Azure access token](#authenticate-with-an-azure-access-token)
* [Authenticate with keyring and artifacts-keyring](#authenticate-with-keyring-and-artifacts-keyring)
* [Publishing packages](#publishing-packages)

1. [Introduction](../../..)
2. [Guides](../../)
3. [Integrations](../)

[Azure Artifacts](#azure-artifacts)
===================================

uv can install packages from
[Azure Artifacts](https://learn.microsoft.com/en-us/azure/devops/artifacts/start-using-azure-artifacts?view=azure-devops&tabs=nuget%2Cnugetserver),
either by using a
[Personal Access Token](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows)
(PAT), or using the [`keyring`](https://github.com/jaraco/keyring) package.

To use Azure Artifacts, add the index to your project:

pyproject.toml

```
[[tool.uv.index]]
name = "private-registry"
url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/simple/"
```

[Authenticate with an Azure access token](#authenticate-with-an-azure-access-token)
-----------------------------------------------------------------------------------

If there is a personal access token (PAT) available (e.g.,
[`$(System.AccessToken)` in an Azure pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml#systemaccesstoken)),
credentials can be provided via "Basic" HTTP authentication scheme. Include the PAT in the password
field of the URL. A username must be included as well, but can be any string.

For example, with the token stored in the `$AZURE_ARTIFACTS_TOKEN` environment variable, set
credentials for the index with:

```
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=dummy
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$AZURE_ARTIFACTS_TOKEN"
```

Note

`PRIVATE_REGISTRY` should match the name of the index defined in your `pyproject.toml`.

[Authenticate with `keyring` and `artifacts-keyring`](#authenticate-with-keyring-and-artifacts-keyring)
-------------------------------------------------------------------------------------------------------

You can also authenticate to Artifacts using [`keyring`](https://github.com/jaraco/keyring) package
with the [`artifacts-keyring` plugin](https://github.com/Microsoft/artifacts-keyring). Because these
two packages are required to authenticate to Azure Artifacts, they must be pre-installed from a
source other than Artifacts.

The `artifacts-keyring` plugin wraps the
[Azure Artifacts Credential Provider tool](https://github.com/microsoft/artifacts-credprovider). The
credential provider supports a few different authentication modes including interactive login — see
the [tool's documentation](https://github.com/microsoft/artifacts-credprovider) for information on
configuration.

uv only supports using the `keyring` package in
[subprocess mode](../../../reference/settings/#keyring-provider). The `keyring` executable must be in
the `PATH`, i.e., installed globally or in the active environment. The `keyring` CLI requires a
username in the URL, and it must be `VssSessionToken`.

```
# Pre-install keyring and the Artifacts plugin from the public PyPI
uv tool install keyring --with artifacts-keyring

# Enable keyring authentication
export UV_KEYRING_PROVIDER=subprocess

# Set the username for the index
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=VssSessionToken
```

Note

The [`tool.uv.keyring-provider`](../../../reference/settings/#keyring-provider)
setting can be used to enable keyring in your `uv.toml` or `pyproject.toml`.

Similarly, the username for the index can be added directly to the index URL.

[Publishing packages](#publishing-packages)
-------------------------------------------

If you also want to publish your own packages to Azure Artifacts, you can use `uv publish` as
described in the [Building and publishing guide](../../package/).

First, add a `publish-url` to the index you want to publish packages to. For example:

pyproject.toml

```
[[tool.uv.index]]
name = "private-registry"
url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/simple/"
publish-url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/upload/"
```

Then, configure credentials (if not using keyring):

```
$ export UV_PUBLISH_USERNAME=dummy
$ export UV_PUBLISH_PASSWORD="$AZURE_ARTIFACTS_TOKEN"
```

And publish the package:

```
$ uv publish --index private-registry
```

To use `uv publish` without adding the `publish-url` to the project, you can set `UV_PUBLISH_URL`:

```
$ export UV_PUBLISH_URL=https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/upload/
$ uv publish
```

Note this method is not preferable because uv cannot check if the package is already published
before uploading artifacts.

March 23, 2026

Back to top