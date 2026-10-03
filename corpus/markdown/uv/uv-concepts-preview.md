[Skip to content](#preview-features)

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
* [Concepts](../)

  Concepts
  + [Projects](../projects/)

    Projects
    - [Structure and files](../projects/layout/)
    - [Creating projects](../projects/init/)
    - [Managing dependencies](../projects/dependencies/)
    - [Running commands](../projects/run/)
    - [Locking and syncing](../projects/sync/)
    - [Configuring projects](../projects/config/)
    - [Building distributions](../projects/build/)
    - [Exporting lockfiles](../projects/export/)
    - [Using workspaces](../projects/workspaces/)
  + [Tools](../tools/)
  + [Python versions](../python-versions/)
  + [Configuration files](../configuration-files/)
  + [Package indexes](../indexes/)
  + [Resolution](../resolution/)
  + [Build backend](../build-backend/)
  + [Authentication](../authentication/)

    Authentication
    - [The auth CLI](../authentication/cli/)
    - [HTTP credentials](../authentication/http/)
    - [Git credentials](../authentication/git/)
    - [TLS certificates](../authentication/certificates/)
    - [Third-party services](../authentication/third-party/)
  + [Caching](../cache/)
  + Preview features

    [Preview features](./)



    Table of contents
    - [Enabling preview features](#enabling-preview-features)
    - [Using preview features](#using-preview-features)
    - [Available preview features](#available-preview-features)
    - [Disabling preview features](#disabling-preview-features)
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

* [Enabling preview features](#enabling-preview-features)
* [Using preview features](#using-preview-features)
* [Available preview features](#available-preview-features)
* [Disabling preview features](#disabling-preview-features)

1. [Introduction](../..)
2. [Concepts](../)

[Preview features](#preview-features)
=====================================

uv includes opt-in preview features to provide an opportunity for community feedback and increase
confidence that changes are a net-benefit before enabling them for everyone.

[Enabling preview features](#enabling-preview-features)
-------------------------------------------------------

To enable all preview features, use the `--preview` flag:

```
$ uv run --preview ...
```

Or, set the `UV_PREVIEW` environment variable:

```
$ UV_PREVIEW=1 uv run ...
```

To enable specific preview features, use the `--preview-features` flag:

```
$ uv run --preview-features foo ...
```

The `--preview-features` flag can be repeated to enable multiple features:

```
$ uv run --preview-features foo --preview-features bar ...
```

Or, features can be provided in a comma separated list:

```
$ uv run --preview-features foo,bar ...
```

The `UV_PREVIEW_FEATURES` environment variable can be used similarly, e.g.:

```
$ UV_PREVIEW_FEATURES=foo,bar uv run ...
```

Preview features can also be enabled in `uv.toml`, or under `[tool.uv]` in `pyproject.toml` and PEP
723 metadata:

```
preview-features = ["foo", "bar"]
```

Set `preview-features = true` to enable all preview features.

Some preview features take effect before configuration files are loaded and cannot be enabled from
configuration.

For backwards compatibility, enabling preview features that do not exist will warn, but not error,
regardless of the source.

[Using preview features](#using-preview-features)
-------------------------------------------------

Often, preview features can be used without changing any preview settings if the behavior change is
gated by some sort of user interaction, For example, while `pylock.toml` support is in preview, you
can use `uv pip install` with a `pylock.toml` file without additional configuration because
specifying the `pylock.toml` file indicates you want to use the feature. However, a warning will be
displayed that the feature is in preview. The preview feature can be enabled to silence the warning.

[Available preview features](#available-preview-features)
---------------------------------------------------------

The following preview features are available:

* [`add-bounds`](#add-bounds): Allows configuring the [default bounds for `uv add`](../../reference/settings/#add-bounds) invocations.
* [`adjust-ulimit`](#adjust-ulimit): On Unix, raises the process's soft open-file limit at startup, up to the hard limit.
* [`artifact-hash-filtering`](#artifact-hash-filtering): Restricts generated requirement hashes to artifacts allowed by binary and build policies.
* [`audit-command`](#audit-command): Allows using `uv audit` and `uv tool audit`.
* [`auth-helper`](#auth-helper): Allows using `uv auth helper` as a credential helper for external tools.
* [`azure-endpoint`](#azure-endpoint): Allows signing requests to Azure Blob Storage endpoints with Azure credentials.
* [`batch-export`](#batch-export): Allows using `uv export --batch`.
* [`build-dependency-check`](#build-dependency-check): Checks build dependencies before nonisolated builds with `uv build`.
* [`build-lazy-imports`](#build-lazy-imports): Enables lazy imports in build backend invocations on CPython 3.15 and later.
  This can affect import-time side effects in third-party build backends.
* [`cache-physical-space`](#cache-physical-space): Reports the physical disk space reclaimed by cache cleanup, accounting for hardlinks and copy-on-write clones.
* [`cache-size`](#cache-size): Allows using `uv cache size`.
* [`centralized-project-envs`](#centralized-project-envs): Stores [project virtual environments](../projects/layout/#centralized-project-environments)
  in the uv cache.
* [`check-command`](#check-command): Allows using `uv check`.
* [`content-addressed-cache`](#content-addressed-cache): Enables content-addressed wheel archives in the cache.
* [`detect-module-conflicts`](#detect-module-conflicts): Warns when multiple packages would install conflicting Python modules into the same
  environment.
* [`extra-build-dependencies`](#extra-build-dependencies): Allows specifying additional dependencies for package builds.
* [`format-command`](#format-command): Allows using `uv format`.
* [`gcs-endpoint`](#gcs-endpoint): Allows signing requests to configured Google Cloud Storage endpoints.
* [`index-by-name`](#index-by-name): Allows selecting configured package indexes by name with `--index` and `--default-index`.
* [`index-exclude-newer`](#index-exclude-newer): Allows setting `exclude-newer` on configured package indexes.
* [`index-hash-algorithm`](#index-hash-algorithm): Allows requiring a hash algorithm for configured package indexes.
* [`init-project-flag`](#init-project-flag): Rejects the deprecated `--project` option in `uv init`.
* [`json-output`](#json-output): Allows `--output-format json` for various uv commands.
* [`lock-without-metadata`](#lock-without-metadata): Omit `package.metadata` from `uv.lock`, except for remote URL dependencies.
* [`lockfile-format-check`](#lockfile-format-check): Rejects non-canonical lockfile formatting when using `--locked` or `--check`.
* [`lockfile-normalization`](#lockfile-normalization): Combines equivalent dependency declarations when writing lockfiles.
* [`malware-check`](#malware-check): Allows `uv sync` and other commands to check for malware using [OSV](https://osv.dev) before
  installing packages.
* [`metadata-json`](#metadata-json): Includes JSON metadata files in built wheels.
* [`minimum-libc-version`](#minimum-libc-version): Allows setting minimum libc versions for universal resolutions.
* [`missing-exclude-newer-package-lock`](#missing-exclude-newer-package-lock): Exclude `exclude-newer-package` entries from the lockfile when not included in the
  project's resolved dependencies.
* [`native-auth`](#native-auth): Enables storage of credentials in a [system-native location](../authentication/http/#the-uv-credentials-store).
* [`no-distutils-patch`](#no-distutils-patch): Stops installing the `_virtualenv.py` / `_virtualenv.pth` distutils configuration monkeypatch
  in virtual environments for Python 3.10 and later.
* [`package-conflicts`](#package-conflicts): Allows defining workspace conflicts at the package level.
* [`packaged-init`](#packaged-init): Makes `uv init` create a packaged application with a `src/` layout, build system, and script
  entry point by default.
* [`project-directory-must-exist`](#project-directory-must-exist): Rejects an invalid `--project` path instead of warning and continuing. Except for `uv init`,
  the path must already exist as a directory or point to a `pyproject.toml` file. This feature
  takes effect before configuration is loaded.
* [`publish-require-normalized`](#publish-require-normalized): Requires normalized distribution filenames when publishing, skipping files whose names are
  not normalized.
* [`pylock`](#pylock): Allows installing from `pylock.toml` files.
* [`python-install-default`](#python-install-default): Allows [installing `python` and `python3` executables](../python-versions/#installing-python-executables).
* [`relocatable-envs-default`](#relocatable-envs-default): Creates relocatable virtual environments by default.
* [`resolution-inputs`](#resolution-inputs): Omits redundant runtime constraints and records consultations to omit unused overrides, exclusions,
  dependency metadata, and package-specific upload cutoffs from the lockfile.
* [`s3-endpoint`](#s3-endpoint): Allows signing requests to configured S3-compatible endpoints.
* [`sbom-export`](#sbom-export): Allows using `uv export --format=cyclonedx1.5`.
* [`special-conda-env-names`](#special-conda-env-names): Stops treating Conda environments named `base` or `root` as special.
* [`tar-codec`](#tar-codec): Uses the new `tar-codec` encoding/decoding backend, instead of `astral-tokio-tar`.
* [`target-workspace-discovery`](#target-workspace-discovery): Uses the directory containing a local `uv run` target, rather than the current working
  directory, as the starting point for project and workspace discovery. This feature takes
  effect before configuration is loaded.
* [`toml-backwards-compatibility`](#toml-backwards-compatibility): Rewrites `pyproject.toml` as TOML 1.0 when building source distributions, preserving the
  original as `pyproject.toml.orig` to ensure compatibility with older build tools.
* [`tool-install-locks`](#tool-install-locks): Stores a `uv.lock` alongside each installed tool and reuses it for reproducible installations,
  upgrades, and audits.
* [`venv-safe-clear`](#venv-safe-clear): Prevents `uv venv --clear` from clearing a directory that does not contain a `pyvenv.cfg` file
  unless `--force` is provided.
* [`workspace-dir`](#workspace-dir): Allows using `uv workspace dir`.
* [`workspace-list`](#workspace-list): Allows using `uv workspace list`.
* [`workspace-list-scripts`](#workspace-list-scripts): Allows using `uv workspace list --scripts`.
* [`workspace-metadata`](#workspace-metadata): Allows using `uv workspace metadata`.

[Disabling preview features](#disabling-preview-features)
---------------------------------------------------------

The `--no-preview` option can be used to disable preview features.

July 24, 2026

Back to top