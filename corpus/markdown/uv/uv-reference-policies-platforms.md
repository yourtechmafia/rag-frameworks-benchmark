[Skip to content](#platform-support)

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
* [Reference](../../)

  Reference
  + [Commands](../../cli/)
  + [Settings](../../settings/)
  + [Environment variables](../../environment/)
  + [Storage](../../storage/)
  + [Installer options](../../installer/)
  + [Troubleshooting](../../troubleshooting/)

    Troubleshooting
    - [Build failures](../../troubleshooting/build-failures/)
    - [Reproducible examples](../../troubleshooting/reproducible-examples/)
  + [Contributing](../../contributing/)
  + [Internals](../../internals/)

    Internals
    - [Resolver](../../internals/resolver/)
    - [Workspace Metadata](../../internals/metadata/)
  + [Benchmarks](../../benchmarks/)
  + [Policies](../)

    Policies
    - [Versioning](../versioning/)
    - Platform support

      [Platform support](./)



      Table of contents
      * [Linux versions](#linux-versions)
      * [Windows versions](#windows-versions)
      * [macOS versions](#macos-versions)
    - [Python support](../python/)
    - [Rust support](../rust/)
    - [License](../license/)

Table of contents

* [Linux versions](#linux-versions)
* [Windows versions](#windows-versions)
* [macOS versions](#macos-versions)

1. [Introduction](../../..)
2. [Reference](../../)
3. [Policies](../)

[Platform support](#platform-support)
=====================================

uv has Tier 1 support for the following platforms:

* macOS (Apple Silicon)
* macOS (x86\_64)
* Linux (x86\_64)
* Windows (x86\_64)

uv is continuously built, tested, and developed against its Tier 1 platforms. Inspired by the Rust
project, Tier 1 can be thought of as
["guaranteed to work"](https://doc.rust-lang.org/beta/rustc/platform-support.html#tier-1).

uv has Tier 2 support
(["guaranteed to build"](https://doc.rust-lang.org/beta/rustc/platform-support.html#tier-2-with-host-tools))
for the following platforms:

* Linux (PPC64LE)
* Linux (RISC-V64)
* Linux (aarch64)
* Linux (armv7)
* Linux (i686)
* Linux (s390x)
* Windows (arm64)

uv has Tier 3 support
(["best effort"](https://doc.rust-lang.org/beta/rustc/platform-support.html#tier-3)) for the
following platforms:

* FreeBSD (x86\_64)
* Windows (i686)

uv provides official binaries on GitHub and pre-built wheels on [PyPI](https://pypi.org/project/uv/)
for its Tier 1 and Tier 2 platforms.

Tier 2 platforms are continuously built, but the uv test suite is not run on them and stability may
vary in practice.

Tier 3 platforms may not be built or tested, but uv will accept patches to fix bugs.

[Linux versions](#linux-versions)
---------------------------------

On Linux, compatibility is determined by libc version.

uv publishes both glibc-based and musl-based distributions.

For glibc-based Linux distributions, uv publishes
[manylinux-compatible](https://peps.python.org/pep-0600/) wheels and corresponding binaries. These
artifacts depend on glibc being available on the host system. In a manylinux wheel tag, the version
encodes the minimum supported glibc version for that wheel; for example, `manylinux_2_17_x86_64`
requires glibc 2.17+.

uv's official glibc-based wheels and binaries are published for the following targets:

* `x86_64-unknown-linux-gnu` (`manylinux_2_17_x86_64`)
* `aarch64-unknown-linux-gnu` (`manylinux_2_28_aarch64`)
* `armv7-unknown-linux-gnueabihf` (`manylinux_2_17_armv7l`)
* `i686-unknown-linux-gnu` (`manylinux_2_17_i686`)
* `powerpc64le-unknown-linux-gnu` (`manylinux_2_17_ppc64le`)
* `riscv64gc-unknown-linux-gnu` (`manylinux_2_31_riscv64`)
* `s390x-unknown-linux-gnu` (`manylinux_2_17_s390x`)

uv also publishes musl-based wheels and fully statically linked binaries for the following targets:

* `x86_64-unknown-linux-musl` (`musllinux_1_1_x86_64`)
* `aarch64-unknown-linux-musl` (`musllinux_1_1_aarch64`)
* `armv7-unknown-linux-musleabihf` (`musllinux_1_1_armv7l`)
* `i686-unknown-linux-musl` (`musllinux_1_1_i686`)
* `riscv64gc-unknown-linux-musl` (`musllinux_1_1_riscv64`)
* `arm-unknown-linux-musleabihf` (`linux_armv6l`)

The wheels are published with [musllinux-compatible](https://peps.python.org/pep-0656/) tags.
However, the embedded `uv` binaries are fully statically linked and do not require musl libc on the
host system.

The official [Docker images](../../../guides/integration/docker/) include these fully statically
linked musl uv binaries for amd64 and arm64.

[Windows versions](#windows-versions)
-------------------------------------

The minimum supported Windows versions are Windows 10 and Windows Server 2016, following
[Rust's own Tier 1 support](https://blog.rust-lang.org/2024/02/26/Windows-7.html).

[macOS versions](#macos-versions)
---------------------------------

uv supports macOS 13+ (Ventura).

uv is known to work on macOS 12, but requires installation of a `realpath` executable.

March 20, 2026

Back to top