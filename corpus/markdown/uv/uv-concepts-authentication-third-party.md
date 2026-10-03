[Skip to content](#third-party-services)

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
    - [Git credentials](../git/)
    - [TLS certificates](../certificates/)
    - Third-party services

      [Third-party services](./)



      Table of contents
      * [Authentication with alternative package indexes](#authentication-with-alternative-package-indexes)
      * [Hugging Face support](#hugging-face-support)
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

* [Authentication with alternative package indexes](#authentication-with-alternative-package-indexes)
* [Hugging Face support](#hugging-face-support)

1. [Introduction](../../..)
2. [Concepts](../../)
3. [Authentication](../)

[Third-party services](#third-party-services)
=============================================

[Authentication with alternative package indexes](#authentication-with-alternative-package-indexes)
---------------------------------------------------------------------------------------------------

See the dedicated guides for authentication with popular alternative Python package indexes:

* [Azure Artifacts](../../../guides/integration/azure/)
* [Google Artifact Registry](../../../guides/integration/google/)
* [AWS CodeArtifact](../../../guides/integration/aws/)
* [JFrog Artifactory](../../../guides/integration/jfrog/)

[Hugging Face support](#hugging-face-support)
---------------------------------------------

uv supports automatic authentication for the Hugging Face Hub. Specifically, if the `HF_TOKEN`
environment variable is set, uv will propagate it to requests to `huggingface.co`.

This is particularly useful for accessing private scripts in Hugging Face Datasets. For example, you
can run the following command to execute the script `main.py` script from a private dataset:

```
$ HF_TOKEN=hf_... uv run https://huggingface.co/datasets/<user>/<name>/resolve/<branch>/main.py
```

You can disable automatic Hugging Face authentication by setting the `UV_NO_HF_TOKEN=1` environment
variable.

March 23, 2026

Back to top