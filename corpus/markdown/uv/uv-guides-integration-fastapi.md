[Skip to content](#using-uv-with-fastapi)

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
    - FastAPI

      [FastAPI](./)



      Table of contents
      * [Migrating an existing FastAPI project](#migrating-an-existing-fastapi-project)
      * [Deployment](#deployment)
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

* [Migrating an existing FastAPI project](#migrating-an-existing-fastapi-project)
* [Deployment](#deployment)

1. [Introduction](../../..)
2. [Guides](../../)
3. [Integrations](../)

[Using uv with FastAPI](#using-uv-with-fastapi)
===============================================

[FastAPI](https://github.com/fastapi/fastapi) is a modern, high-performance Python web framework.
You can use uv to manage your FastAPI project, including installing dependencies, managing
environments, running FastAPI applications, and more.

Note

You can view the source code for this guide in the [uv-fastapi-example](https://github.com/astral-sh/uv-fastapi-example) repository.

[Migrating an existing FastAPI project](#migrating-an-existing-fastapi-project)
-------------------------------------------------------------------------------

As an example, consider the sample application defined in the
[FastAPI documentation](https://fastapi.tiangolo.com/tutorial/bigger-applications/), structured as
follows:

```
project
└── app
    ├── __init__.py
    ├── main.py
    ├── dependencies.py
    ├── routers
    │   ├── __init__.py
    │   ├── items.py
    │   └── users.py
    └── internal
        ├── __init__.py
        └── admin.py
```

To use uv with this application, inside the `project` directory run:

```
$ uv init --no-package
```

This creates a `pyproject.toml` file for a
[flat, unpackaged project](../../../concepts/projects/init/#unpackaged-applications).

Then, add a dependency on FastAPI:

```
$ uv add fastapi --extra standard
```

You should now have the following structure:

```
project
├── pyproject.toml
└── app
    ├── __init__.py
    ├── main.py
    ├── dependencies.py
    ├── routers
    │   ├── __init__.py
    │   ├── items.py
    │   └── users.py
    └── internal
        ├── __init__.py
        └── admin.py
```

And the contents of the `pyproject.toml` file should look something like this:

pyproject.toml

```
[project]
name = "uv-fastapi-example"
version = "0.1.0"
description = "FastAPI project"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "fastapi[standard]",
]
```

From there, you can run the FastAPI application with:

```
$ uv run fastapi dev
```

`uv run` will automatically resolve and lock the project dependencies (i.e., create a `uv.lock`
alongside the `pyproject.toml`), create a virtual environment, and run the command in that
environment.

Test the app by opening <http://127.0.0.1:8000/?token=jessica> in a web browser.

[Deployment](#deployment)
-------------------------

To deploy the FastAPI application with Docker, you can use the following `Dockerfile`:

Dockerfile

```
FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache

# Run the application.
CMD ["/app/.venv/bin/fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]
```

Build the Docker image with:

```
$ docker build -t fastapi-app .
```

Run the Docker container locally with:

```
$ docker run -p 8000:80 fastapi-app
```

Navigate to <http://127.0.0.1:8000/?token=jessica> in your browser to verify that the app is running
correctly.

Tip

For more on using uv with Docker, see the [Docker guide](../docker/).

July 28, 2026

Back to top