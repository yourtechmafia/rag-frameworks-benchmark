[Skip to content](#storage)

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
* [Reference](../)

  Reference
  + [Commands](../cli/)
  + [Settings](../settings/)
  + [Environment variables](../environment/)
  + Storage

    [Storage](./)



    Table of contents
    - [Storage directories](#storage-directories)

      * [Temporary directory](#temporary-directory)
      * [Cache directory](#cache-directory)
      * [Persistent data directory](#persistent-data-directory)
      * [Configuration directories](#configuration-directories)
      * [Executable directory](#executable-directory)
    - [Types of data](#types-of-data)

      * [Dependency cache](#dependency-cache)
      * [Python versions](#python-versions)
      * [Python executables](#python-executables)
      * [Tools](#tools)
      * [Tool executables](#tool-executables)
      * [The uv executable](#the-uv-executable)
      * [Configuration files](#configuration-files)
      * [Project virtual environments](#project-virtual-environments)
      * [Script virtual environments](#script-virtual-environments)
  + [Installer options](../installer/)
  + [Troubleshooting](../troubleshooting/)

    Troubleshooting
    - [Build failures](../troubleshooting/build-failures/)
    - [Reproducible examples](../troubleshooting/reproducible-examples/)
  + [Contributing](../contributing/)
  + [Internals](../internals/)

    Internals
    - [Resolver](../internals/resolver/)
    - [Workspace Metadata](../internals/metadata/)
  + [Benchmarks](../benchmarks/)
  + [Policies](../policies/)

    Policies
    - [Versioning](../policies/versioning/)
    - [Platform support](../policies/platforms/)
    - [Python support](../policies/python/)
    - [Rust support](../policies/rust/)
    - [License](../policies/license/)

Table of contents

* [Storage directories](#storage-directories)

  + [Temporary directory](#temporary-directory)
  + [Cache directory](#cache-directory)
  + [Persistent data directory](#persistent-data-directory)
  + [Configuration directories](#configuration-directories)
  + [Executable directory](#executable-directory)
* [Types of data](#types-of-data)

  + [Dependency cache](#dependency-cache)
  + [Python versions](#python-versions)
  + [Python executables](#python-executables)
  + [Tools](#tools)
  + [Tool executables](#tool-executables)
  + [The uv executable](#the-uv-executable)
  + [Configuration files](#configuration-files)
  + [Project virtual environments](#project-virtual-environments)
  + [Script virtual environments](#script-virtual-environments)

1. [Introduction](../..)
2. [Reference](../)

[Storage](#storage)
===================

[Storage directories](#storage-directories)
-------------------------------------------

uv uses the following high-level directories for storage.

For each location, uv checks for the existence of environment variables in the given order and uses
the first path found.

The paths of storage directories are platform-specific. uv follows the
[XDG](https://specifications.freedesktop.org/basedir-spec/latest/) conventions on Linux and macOS
and the [Known Folder](https://learn.microsoft.com/en-us/windows/win32/shell/known-folders) scheme
on Windows.

### [Temporary directory](#temporary-directory)

The temporary directory is used for ephemeral data.

UnixWindows

1. `$TMPDIR`
2. `/tmp`

1. `%TMP%`
2. `%TEMP%`
3. `%USERPROFILE%`

### [Cache directory](#cache-directory)

The cache directory is used for data that is disposable, but is useful to be long-lived.

UnixWindows

1. `$XDG_CACHE_HOME/uv`
2. `$HOME/.cache/uv`

1. `%LOCALAPPDATA%\uv\cache`
2. `uv\cache` within [`FOLDERID_LocalAppData`](https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid#FOLDERID_LocalAppData)

### [Persistent data directory](#persistent-data-directory)

The persistent data directory is used for non-disposable data.

UnixWindows

1. `$XDG_DATA_HOME/uv`
2. `$HOME/.local/share/uv`
3. `$CWD/.uv`

1. `%APPDATA%\uv\data`
2. `.\.uv`

### [Configuration directories](#configuration-directories)

The configuration directories are used to store changes to uv's settings.

User-level configuration

UnixWindows

1. `$XDG_CONFIG_HOME/uv`
2. `$HOME/.config/uv`

1. `%APPDATA%\uv`
2. `uv` within [`FOLDERID_RoamingAppData`](https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid#FOLDERID_RoamingAppData)

System-level configuration

UnixWindows

1. `$XDG_CONFIG_DIRS/uv`
2. `/etc/uv`

1. `%PROGRAMDATA%\uv`
2. `uv` within [`FOLDERID_AppDataProgramData`](https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid#FOLDERID_AppDataProgramData)

### [Executable directory](#executable-directory)

The executable directory is used to store files that can be run by the user, i.e., a directory that
should be on the `PATH`.

UnixWindows

1. `$XDG_BIN_HOME`
2. `$XDG_DATA_HOME/../bin`
3. `$HOME/.local/bin`

1. `%XDG_BIN_HOME%`
2. `%XDG_DATA_HOME%\..\bin`
3. `%USERPROFILE%\.local\bin`

[Types of data](#types-of-data)
-------------------------------

### [Dependency cache](#dependency-cache)

uv uses a local cache to avoid re-downloading and re-building dependencies.

By default, the cache is stored in the [cache directory](#cache-directory) but it can be overridden
via command line arguments, environment variables, or settings as detailed in
[the cache documentation](../../concepts/cache/#cache-directory). When the cache is disabled, the
cache will be stored in a [temporary directory](#temporary-directory).

Use `uv cache dir` to show the current cache directory path.

Important

For optimal performance, the cache directory needs to be on the same filesystem as virtual
environments.

### [Python versions](#python-versions)

uv can install managed [Python versions](../../concepts/python-versions/), e.g., with
`uv python install`.

By default, Python versions managed by uv are stored in a `python/` subdirectory of the
[persistent data directory](#persistent-data-directory), e.g., `~/.local/share/uv/python`.

Use `uv python dir` to show the Python installation directory.

Use the `UV_PYTHON_INSTALL_DIR` environment variable to override the installation directory.

Note

Changing where Python is installed will not be automatically reflected in existing virtual environments; they will keep referring to the old location, and will need to be updated manually (e.g. by re-creating them).

### [Python executables](#python-executables)

uv installs executables for [Python versions](#python-versions), e.g., `python3.13`.

By default, Python executables are stored in the [executable directory](#executable-directory).

Use `uv python dir --bin` to show the Python executable directory.

Use the `UV_PYTHON_BIN_DIR` environment variable to override the Python executable directory.

### [Tools](#tools)

uv can install Python packages as [command-line tools](../../concepts/tools/) using
`uv tool install`.

By default, tools are installed in a `tools/` subdirectory of the
[persistent data directory](#persistent-data-directory), e.g., `~/.local/share/uv/tools`.

Use `uv tool dir` to show the tool installation directory.

Use the `UV_TOOL_DIR` environment variable to configure the installation directory.

### [Tool executables](#tool-executables)

uv installs executables for installed [tools](#tools), e.g., `ruff`.

By default, tool executables are stored in the [executable directory](#executable-directory).

Use `uv tool dir --bin` to show the tool executable directory.

Use the `UV_TOOL_BIN_DIR` environment variable to configure the tool executable directory.

### [The uv executable](#the-uv-executable)

When using uv's [standalone installer](../installer/) to install uv, the `uv` and `uvx` executables
are installed into the [executable directory](#executable-directory).

Use the `UV_INSTALL_DIR` environment variable to configure uv's installation directory.

### [Configuration files](#configuration-files)

uv's behavior can be configured through TOML files.

Configuration files are discovered in the [configuration directories](#configuration-directories).

For more details, see the [configuration files documentation](../../concepts/configuration-files/).

### [Project virtual environments](#project-virtual-environments)

When working on [projects](../../concepts/projects/), uv creates a dedicated virtual
environment for each project.

By default, project virtual environments are created in `.venv` in the project or workspace root,
i.e., next to the `pyproject.toml`.

Use the `UV_PROJECT_ENVIRONMENT` environment variable to override this location. For more details,
see the
[projects environment documentation](../../concepts/projects/config/#project-environment-path).

With the [`centralized-project-envs` preview feature](../../concepts/preview/), uv stores default
project environments in the [cache directory](#cache-directory). They can be removed by
`uv cache clean` or `uv cache prune` and are recreated when next needed. See the
[centralized project environments](../../concepts/projects/layout/#centralized-project-environments)
documentation for details.

### [Script virtual environments](#script-virtual-environments)

When running [scripts with inline metadata](../../guides/scripts/), uv creates a dedicated virtual
environment for each script in the [cache directory](#cache-directory).

June 25, 2026

Back to top