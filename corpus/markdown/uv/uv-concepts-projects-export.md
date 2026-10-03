[Skip to content](#exporting-a-lockfile)

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
  + [Projects](../)

    Projects
    - [Structure and files](../layout/)
    - [Creating projects](../init/)
    - [Managing dependencies](../dependencies/)
    - [Running commands](../run/)
    - [Locking and syncing](../sync/)
    - [Configuring projects](../config/)
    - [Building distributions](../build/)
    - Exporting lockfiles

      [Exporting lockfiles](./)



      Table of contents
      * [Overview of export formats](#overview-of-export-formats)
      * [requirements.txt format](#requirementstxt-format)

        + [Basic usage](#basic-usage)
      * [pylock.toml format](#pylocktoml-format)

        + [Basic usage](#basic-usage_1)
      * [CycloneDX SBOM format](#cyclonedx-sbom-format)

        + [What is CycloneDX?](#what-is-cyclonedx)
        + [Basic usage](#basic-usage_2)
        + [SBOM Structure](#sbom-structure)
      * [Next steps](#next-steps)
    - [Using workspaces](../workspaces/)
  + [Tools](../../tools/)
  + [Python versions](../../python-versions/)
  + [Configuration files](../../configuration-files/)
  + [Package indexes](../../indexes/)
  + [Resolution](../../resolution/)
  + [Build backend](../../build-backend/)
  + [Authentication](../../authentication/)

    Authentication
    - [The auth CLI](../../authentication/cli/)
    - [HTTP credentials](../../authentication/http/)
    - [Git credentials](../../authentication/git/)
    - [TLS certificates](../../authentication/certificates/)
    - [Third-party services](../../authentication/third-party/)
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

* [Overview of export formats](#overview-of-export-formats)
* [requirements.txt format](#requirementstxt-format)

  + [Basic usage](#basic-usage)
* [pylock.toml format](#pylocktoml-format)

  + [Basic usage](#basic-usage_1)
* [CycloneDX SBOM format](#cyclonedx-sbom-format)

  + [What is CycloneDX?](#what-is-cyclonedx)
  + [Basic usage](#basic-usage_2)
  + [SBOM Structure](#sbom-structure)
* [Next steps](#next-steps)

1. [Introduction](../../..)
2. [Concepts](../../)
3. [Projects](../)

[Exporting a lockfile](#exporting-a-lockfile)
=============================================

uv can export a lockfile to different formats for integration with other tools and workflows. The
`uv export` command supports multiple output formats, each suited to different use cases.

For more details on lockfiles and how they're created, see the [project layout](../layout/) and
[locking and syncing](../sync/) documentation.

[Overview of export formats](#overview-of-export-formats)
---------------------------------------------------------

uv supports three export formats:

* `requirements.txt`: The traditional pip-compatible
  [requirements file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/).
* `pylock.toml`: The standardized Python lockfile format defined in
  [PEP 751](https://peps.python.org/pep-0751/).
* `CycloneDX`: An industry-standard [Software Bill of Materials (SBOM)](https://cyclonedx.org/)
  format.

The format can be specified with the `--format` flag:

```
$ uv export --format requirements.txt
$ uv export --format pylock.toml
$ uv export --format cyclonedx1.5
```

Tip

By default, `uv export` prints to stdout. Use `--output-file` to write to a file for any format:

```
$ uv export --format requirements.txt --output-file requirements.txt
$ uv export --format pylock.toml --output-file pylock.toml
$ uv export --format cyclonedx1.5 --output-file sbom.json
```

[`requirements.txt` format](#requirementstxt-format)
----------------------------------------------------

The `requirements.txt` format is the most widely supported format for Python dependencies. It can be
used with `pip` and other Python package managers.

### [Basic usage](#basic-usage)

```
$ uv export --format requirements.txt
```

The generated `requirements.txt` file can then be installed via `uv pip install`, or with other
tools like `pip`.

Note

In general, we recommend against using both a `uv.lock` and a `requirements.txt` file. The
`uv.lock` format is more powerful and includes features that cannot be expressed in
`requirements.txt`. If you find yourself exporting a `uv.lock` file, consider opening an issue
to discuss your use case.

[`pylock.toml` format](#pylocktoml-format)
------------------------------------------

[PEP 751](https://peps.python.org/pep-0751/) defines a TOML-based lockfile format for Python
dependencies. uv can export your project's dependency lockfile to this format.

### [Basic usage](#basic-usage_1)

```
$ uv export --format pylock.toml
```

Relative local paths are written relative to the output file's directory. When writing to stdout,
they are relative to the current working directory. Use `--output-file` when writing a `pylock.toml`
in another directory.

[CycloneDX SBOM format](#cyclonedx-sbom-format)
-----------------------------------------------

uv can export your project's dependency lockfile as a Software Bill of Materials (SBOM) in CycloneDX
format. SBOMs provide a comprehensive inventory of all software components in your application,
which is useful for security auditing, compliance, and supply chain transparency.

Important

Support for exporting to CycloneDX is in [preview](../../preview/), and may change in any future release.

### [What is CycloneDX?](#what-is-cyclonedx)

[CycloneDX](https://cyclonedx.org/) is an industry-standard format for creating Software Bill of
Materials. CycloneDX is machine readable and widely supported by security scanning tools,
vulnerability databases, and Software Composition Analysis (SCA) platforms.

### [Basic usage](#basic-usage_2)

To export your project's lockfile as a CycloneDX SBOM:

```
$ uv export --format cyclonedx1.5
```

This will generate a JSON-encoded CycloneDX v1.5 document containing your project and all of its
dependencies.

### [SBOM Structure](#sbom-structure)

The generated SBOM follows the
[CycloneDX specification](https://cyclonedx.org/specification/overview/). uv also includes the
following custom properties on components:

* `uv:package:marker`: Environment markers (e.g., `python_version >= "3.8"`)
* `uv:workspace:path`: Relative path for workspace members

[Next steps](#next-steps)
-------------------------

To learn more about lockfiles and exporting, see the [locking and syncing](../sync/) documentation
and the [command reference](../../../reference/cli/#uv-export).

Or, read on to learn how to
[build and publish your project to a package index](../../../guides/package/).

September 28, 2026

Back to top