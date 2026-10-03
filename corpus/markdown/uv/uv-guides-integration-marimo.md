[Skip to content](#using-uv-with-marimo)

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
    - marimo

      [marimo](./)



      Table of contents
      * [Using marimo as a standalone tool](#using-marimo-as-a-standalone-tool)
      * [Using marimo with inline script metadata](#using-marimo-with-inline-script-metadata)
      * [Using marimo within a project](#using-marimo-within-a-project)
      * [Using marimo in a non-project environment](#using-marimo-in-a-non-project-environment)
      * [Running marimo notebooks as scripts](#running-marimo-notebooks-as-scripts)
    - [GitHub Actions](../github/)
    - [GitLab CI/CD](../gitlab/)
    - [Pre-commit](../pre-commit/)
    - [PyTorch](../pytorch/)
    - [FastAPI](../fastapi/)
    - [Bazel](../bazel/)
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

* [Using marimo as a standalone tool](#using-marimo-as-a-standalone-tool)
* [Using marimo with inline script metadata](#using-marimo-with-inline-script-metadata)
* [Using marimo within a project](#using-marimo-within-a-project)
* [Using marimo in a non-project environment](#using-marimo-in-a-non-project-environment)
* [Running marimo notebooks as scripts](#running-marimo-notebooks-as-scripts)

1. [Introduction](../../..)
2. [Guides](../../)
3. [Integrations](../)

[Using uv with marimo](#using-uv-with-marimo)
=============================================

[marimo](https://github.com/marimo-team/marimo) is an open-source Python notebook that blends
interactive computing with the reproducibility and reusability of traditional software, letting you
version with Git, run as scripts, and share as apps. Because marimo notebooks are stored as pure
Python scripts, they are able to integrate tightly with uv.

You can readily use marimo as a standalone tool, as self-contained scripts, in projects, and in
non-project environments.

[Using marimo as a standalone tool](#using-marimo-as-a-standalone-tool)
-----------------------------------------------------------------------

For ad-hoc access to marimo notebooks, start a marimo server at any time in an isolated environment
with:

```
$ uvx marimo edit
```

Start a specific notebook with:

```
$ uvx marimo edit my_notebook.py
```

[Using marimo with inline script metadata](#using-marimo-with-inline-script-metadata)
-------------------------------------------------------------------------------------

Because marimo notebooks are stored as Python scripts, they can encapsulate their own dependencies
using inline script metadata, via uv's [support for scripts](../../scripts/). For example,
to add `numpy` as a dependency to your notebook, use this command:

```
$ uv add --script my_notebook.py numpy
```

To interactively edit a notebook containing inline script metadata, use:

```
$ uvx marimo edit --sandbox my_notebook.py
```

marimo will automatically use uv to start your notebook in an isolated virtual environment with your
script's dependencies. Packages installed from the marimo UI will automatically be added to the
notebook's script metadata.

You can optionally run these notebooks as Python scripts, without opening an interactive session:

```
$ uv run my_notebook.py
```

[Using marimo within a project](#using-marimo-within-a-project)
---------------------------------------------------------------

If you're working within a [project](../../../concepts/projects/), you can start a marimo
notebook with access to the project's virtual environment via the following command (assuming marimo
is a project dependency):

```
$ uv run marimo edit my_notebook.py
```

To make additional packages available to your notebook, either add them to your project with
`uv add`, or use marimo's built-in package installation UI, which will invoke `uv add` on your
behalf.

If marimo is not a project dependency, you can still run a notebook with the following command:

```
$ uv run --with marimo marimo edit my_notebook.py
```

This will let you import your project's modules while editing your notebook. However, packages
installed via marimo's UI when running in this way will not be added to your project, and may
disappear on subsequent marimo invocations.

[Using marimo in a non-project environment](#using-marimo-in-a-non-project-environment)
---------------------------------------------------------------------------------------

To run marimo in a virtual environment that isn't associated with a
[project](../../../concepts/projects/), add marimo to the environment directly:

```
$ uv venv
$ uv pip install numpy
$ uv pip install marimo
$ uv run marimo edit
```

From here, `import numpy` will work within the notebook, and marimo's UI installer will add packages
to the environment with `uv pip install` on your behalf.

[Running marimo notebooks as scripts](#running-marimo-notebooks-as-scripts)
---------------------------------------------------------------------------

Regardless of how your dependencies are managed (with inline script metadata, within a project, or
with a non-project environment), you can run marimo notebooks as scripts with:

```
$ uv run my_notebook.py
```

This executes your notebook as a Python script, without opening an interactive session in your
browser.

May 27, 2025

Back to top