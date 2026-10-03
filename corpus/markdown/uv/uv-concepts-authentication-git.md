[Skip to content](#git-credentials)

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
    - [HTTP credentials](../http/)
    - Git credentials

      [Git credentials](./)



      Table of contents
      * [SSH authentication](#ssh-authentication)

        + [HTTP authentication](#http-authentication)
      * [Persistence of credentials](#persistence-of-credentials)
      * [Git credential helpers](#git-credential-helpers)
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

* [SSH authentication](#ssh-authentication)

  + [HTTP authentication](#http-authentication)
* [Persistence of credentials](#persistence-of-credentials)
* [Git credential helpers](#git-credential-helpers)

1. [Introduction](../../..)
2. [Concepts](../../)
3. [Authentication](../)

[Git credentials](#git-credentials)
===================================

uv allows packages to be installed from private Git repositories using SSH or HTTP authentication.

[SSH authentication](#ssh-authentication)
-----------------------------------------

To authenticate using an SSH key, use the `ssh://` protocol:

* `git+ssh://git@<hostname>/...` (e.g., `git+ssh://[email protected]/astral-sh/uv`)
* `git+ssh://git@<host>/...` (e.g., `git+ssh://[email protected]/astral-sh/uv`)

SSH authentication requires using the username `git`.

See the
[GitHub SSH documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)
for more details on how to configure SSH.

### [HTTP authentication](#http-authentication)

To authenticate over HTTP Basic authentication using a password or token:

* `git+https://<user>:<token>@<hostname>/...` (e.g.,
  `git+https://git:[email protected]/astral-sh/uv`)
* `git+https://<token>@<hostname>/...` (e.g., `git+https://[email protected]/astral-sh/uv`)
* `git+https://<user>@<hostname>/...` (e.g., `git+https://[email protected]/astral-sh/uv`)

Note

When using a GitHub personal access token, the username is arbitrary. GitHub doesn't allow you to
use your account name and password in URLs like this, although other hosts may.

If there are no credentials present in the URL and authentication is needed, the
[Git credential helper](#git-credential-helpers) will be queried.

[Persistence of credentials](#persistence-of-credentials)
---------------------------------------------------------

When using `uv add`, uv *will not* persist Git credentials to the `pyproject.toml` or `uv.lock`.
These files are often included in source control and distributions, so it is generally unsafe to
include credentials in them.

If you have a Git credential helper configured, your credentials may be automatically persisted,
resulting in successful subsequent fetches of the dependency. However, if you do not have a Git
credential helper or the project is used on a machine without credentials seeded, uv will fail to
fetch the dependency.

You *may* force uv to persist Git credentials by passing the `--raw` option to `uv add`. However, we
strongly recommend setting up a [credential helper](#git-credential-helpers) instead.

[Git credential helpers](#git-credential-helpers)
-------------------------------------------------

Git credential helpers are used to store and retrieve Git credentials. See the
[Git documentation](https://git-scm.com/doc/credential-helpers) to learn more.

If you're using GitHub, the simplest way to set up a credential helper is to
[install the `gh` CLI](https://github.com/cli/cli#installation) and use:

```
$ gh auth login
```

See the [`gh auth login`](https://cli.github.com/manual/gh_auth_login) documentation for more
details.

Note

When using `gh auth login` interactively, the credential helper will be configured automatically.
But when using `gh auth login --with-token`, as in the uv
[GitHub Actions guide](../../../guides/integration/github/#private-repos), the
[`gh auth setup-git`](https://cli.github.com/manual/gh_auth_setup-git) command will need to be
run afterwards to configure the credential helper.

August 28, 2025

Back to top