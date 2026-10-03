[Skip to content](#getting-help)

[![logo](../../assets/logo-letter.svg)](../.. "uv")
uv

[uv](https://github.com/astral-sh/uv "Go to repository")

* [Introduction](../..)
* [Getting started](../)

  Getting started
  + [Installation](../installation/)
  + [First steps](../first-steps/)
  + [Features](../features/)
  + Getting help

    [Getting help](./)



    Table of contents
    - [Help menus](#help-menus)
    - [Displaying verbose output](#displaying-verbose-output)
    - [Viewing the version](#viewing-the-version)
    - [Troubleshooting issues](#troubleshooting-issues)
    - [Open an issue on GitHub](#open-an-issue-on-github)
    - [Chat on Discord](#chat-on-discord)
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

Table of contents

* [Help menus](#help-menus)
* [Displaying verbose output](#displaying-verbose-output)
* [Viewing the version](#viewing-the-version)
* [Troubleshooting issues](#troubleshooting-issues)
* [Open an issue on GitHub](#open-an-issue-on-github)
* [Chat on Discord](#chat-on-discord)

1. [Introduction](../..)
2. [Getting started](../)

[Getting help](#getting-help)
=============================

[Help menus](#help-menus)
-------------------------

The `--help` flag can be used to view the help menu for a command, e.g., for `uv`:

```
$ uv --help
```

To view the help menu for a specific command, e.g., for `uv init`:

```
$ uv init --help
```

When using the `--help` flag, uv displays a condensed help menu. To view a longer help menu for a
command, use `uv help`:

```
$ uv help
```

To view the long help menu for a specific command, e.g., for `uv init`:

```
$ uv help init
```

When using the long help menu, uv will attempt to use `less` or `more` to "page" the output so it is
not all displayed at once. To exit the pager, press `q`.

[Displaying verbose output](#displaying-verbose-output)
-------------------------------------------------------

The `-v` flag can be used to display verbose output for a command, e.g., for `uv sync`:

```
$ uv sync -v
```

The `-v` flag can be repeated to increase verbosity, e.g.:

```
$ uv sync -vv
```

Often, the verbose output will include additional information about why uv is behaving in a certain
way.

[Viewing the version](#viewing-the-version)
-------------------------------------------

When seeking help, it's important to determine the version of uv that you're using — sometimes the
problem is already solved in a newer version.

To check the installed version:

```
$ uv self version
```

The following are also valid:

```
$ uv --version      # Same output as `uv self version`
$ uv -V             # Will not include the build commit and date
```

Note

Before uv 0.7.0, `uv version` was used instead of `uv self version`.

[Troubleshooting issues](#troubleshooting-issues)
-------------------------------------------------

The reference documentation contains a
[troubleshooting guide](../../reference/troubleshooting/) for common issues.

[Open an issue on GitHub](#open-an-issue-on-github)
---------------------------------------------------

The [issue tracker](https://github.com/astral-sh/uv/issues) on GitHub is a good place to report bugs
and request features. Make sure to search for similar issues first, as it is common for someone else
to encounter the same problem.

[Chat on Discord](#chat-on-discord)
-----------------------------------

Astral has a [Discord server](https://discord.com/invite/astral-sh), which is a great place to ask
questions, learn more about uv, and engage with other community members.

September 17, 2025

Back to top