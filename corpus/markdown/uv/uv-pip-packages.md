[Skip to content](#managing-packages)

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
  + [The pip interface](../)

    The pip interface
    - [Using environments](../environments/)
    - Managing packages

      [Managing packages](./)



      Table of contents
      * [Installing a package](#installing-a-package)
      * [Editable packages](#editable-packages)
      * [Installing packages from files](#installing-packages-from-files)
      * [Uninstalling a package](#uninstalling-a-package)
    - [Inspecting environments](../inspection/)
    - [Declaring dependencies](../dependencies/)
    - [Locking environments](../compile/)
    - [Compatibility with pip](../compatibility/)
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

* [Installing a package](#installing-a-package)
* [Editable packages](#editable-packages)
* [Installing packages from files](#installing-packages-from-files)
* [Uninstalling a package](#uninstalling-a-package)

1. [Introduction](../..)
2. [Concepts](../../concepts/)
3. [The pip interface](../)

[Managing packages](#managing-packages)
=======================================

[Installing a package](#installing-a-package)
---------------------------------------------

To install a package into the virtual environment, e.g., Flask:

```
$ uv pip install flask
```

To install a package with optional dependencies enabled, e.g., Flask with the "dotenv" extra:

```
$ uv pip install "flask[dotenv]"
```

To install multiple packages, e.g., Flask and Ruff:

```
$ uv pip install flask ruff
```

To install a package with a constraint, e.g., Ruff v0.2.0 or newer:

```
$ uv pip install 'ruff>=0.2.0'
```

To install a package at a specific version, e.g., Ruff v0.3.0:

```
$ uv pip install 'ruff==0.3.0'
```

To install a package from the disk:

```
$ uv pip install "ruff @ ./projects/ruff"
```

To install a package from GitHub:

```
$ uv pip install "git+https://github.com/astral-sh/ruff"
```

To install a package from GitHub at a specific reference:

```
$ # Install a tag
$ uv pip install "git+https://github.com/astral-sh/[email protected]"

$ # Install a commit
$ uv pip install "git+https://github.com/astral-sh/ruff@1fadefa67b26508cc59cf38e6130bde2243c929d"

$ # Install a branch
$ uv pip install "git+https://github.com/astral-sh/ruff@main"
```

See the [Git authentication](../../concepts/authentication/git/) documentation for installation from
a private repository.

[Editable packages](#editable-packages)
---------------------------------------

Editable packages do not need to be reinstalled for changes to their source code to be active.

To install the current project as an editable package

```
$ uv pip install -e .
```

To install a project in another directory as an editable package:

```
$ uv pip install -e "ruff @ ./project/ruff"
```

[Installing packages from files](#installing-packages-from-files)
-----------------------------------------------------------------

Multiple packages can be installed at once from standard file formats.

Install from a `requirements.txt` file:

```
$ uv pip install -r requirements.txt
```

See the [`uv pip compile`](../compile/) documentation for more information on `requirements.txt`
files.

Install from a `pyproject.toml` file:

```
$ uv pip install -r pyproject.toml
```

Install from a `pyproject.toml` file with optional dependencies enabled, e.g., the "foo" extra:

```
$ uv pip install -r pyproject.toml --extra foo
```

Install from a `pyproject.toml` file with all optional dependencies enabled:

```
$ uv pip install -r pyproject.toml --all-extras
```

To install dependency groups in the current project directory's `pyproject.toml`, for example the
group `foo`:

```
$ uv pip install --group foo
```

To specify the project directory where groups should be sourced from:

```
$ uv pip install --project some/path/ --group foo --group bar
```

Alternatively, you can specify a path to a `pyproject.toml` for each group:

```
$ uv pip install --group some/path/pyproject.toml:foo --group other/pyproject.toml:bar
```

Note

As in pip, `--group` flags do not apply to other sources specified with flags like `-r` or `-e`.
For instance, `uv pip install -r some/path/pyproject.toml --group foo` sources `foo`
from `./pyproject.toml` and **not** `some/path/pyproject.toml`.

[Uninstalling a package](#uninstalling-a-package)
-------------------------------------------------

To uninstall a package, e.g., Flask:

```
$ uv pip uninstall flask
```

To uninstall multiple packages, e.g., Flask and Ruff:

```
$ uv pip uninstall flask ruff
```

August 28, 2025

Back to top