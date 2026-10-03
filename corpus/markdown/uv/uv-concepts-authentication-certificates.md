[Skip to content](#tls-certificates)

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
    - TLS certificates

      [TLS certificates](./)



      Table of contents
      * [TLS backend](#tls-backend)
      * [System certificates](#system-certificates)
      * [Custom certificates](#custom-certificates)
      * [Insecure hosts](#insecure-hosts)
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

* [TLS backend](#tls-backend)
* [System certificates](#system-certificates)
* [Custom certificates](#custom-certificates)
* [Insecure hosts](#insecure-hosts)

1. [Introduction](../../..)
2. [Concepts](../../)
3. [Authentication](../)

[TLS certificates](#tls-certificates)
=====================================

uv uses TLS to securely communicate with package indexes and other HTTPS servers. TLS certificates
are used to verify the identity of these servers, ensuring that connections are not intercepted.

[TLS backend](#tls-backend)
---------------------------

uv uses [`rustls`](https://github.com/rustls/rustls), a memory-safe TLS implementation written in
Rust, with [`aws-lc-rs`](https://github.com/aws/aws-lc-rs) as the cryptography provider.

uv supports the following X.509 certificate signature algorithms:

* ECDSA (P-256, P-384, P-521) with SHA-256, SHA-384, or SHA-512
* Ed25519
* RSA PKCS#1 v1.5 (2048–8192 bit) with SHA-256, SHA-384, or SHA-512
* RSA-PSS (2048–8192 bit) with SHA-256, SHA-384, or SHA-512

[System certificates](#system-certificates)
-------------------------------------------

By default, uv uses bundled Mozilla root certificates for TLS verification. In some cases, you may
want to use the platform's native certificate store instead — for example, if you're relying on a
corporate trust root (e.g., for a mandatory proxy) that's included in your system's certificate
store.

To use system certificates, pass the [`--system-certs`](../../../reference/cli/#uv) flag, set the
[`UV_SYSTEM_CERTS`](../../../reference/environment/#uv_system_certs) environment variable to `true`,
or set [`system-certs = true`](../../../reference/settings/#system-certs) in `uv.toml`.

When using system certificates, certificate verification is performed by
[`rustls-platform-verifier`](https://github.com/rustls/rustls-platform-verifier), which delegates to
the operating system's certificate verifier.

[Custom certificates](#custom-certificates)
-------------------------------------------

To use custom CA certificates, set the
[`SSL_CERT_FILE`](../../../reference/environment/#ssl_cert_file) environment variable to the path of
a PEM-encoded certificate bundle (e.g., `certs.pem`, `ca-bundle.crt`), or set
[`SSL_CERT_DIR`](../../../reference/environment/#ssl_cert_dir) to one or more directories containing
PEM-encoded certificate files. Multiple entries are supported, separated using a platform-specific
delimiter (`:` on Unix, `;` on Windows).

Note

For a single `uv pip` invocation, pass [`--cert`](../../../reference/cli/#uv-pip) with the path
to a PEM-encoded certificate bundle. The bundle replaces uv's default certificate source for
that invocation.

Certificates are usually stored with `.pem`, `.crt`, or `.cer` extensions, but uv will attempt to
read a certificate from any regular file in the provided `SSL_CERT_DIR`.

Files that cannot be parsed as PEM certificates are ignored. uv resolves symlinks and ignores
dangling symlinks.

DER-encoded files are not supported.

When set to non-empty values, these environment variables **override** the default certificate
source entirely — only the provided certificates will be trusted. If a configured file or directory
does not exist or contains no valid certificates, no default certificates will be trusted.

`SSL_CERT_FILE` can point to a single certificate or a bundle containing multiple certificates.
`SSL_CERT_DIR` can include multiple directory entries; uv will load all valid certificates from each
directory.

If client certificate authentication (mTLS) is desired, set the
[`SSL_CLIENT_CERT`](../../../reference/environment/#ssl_client_cert) environment variable to the path
of a PEM formatted file containing the certificate followed by the private key.

[Insecure hosts](#insecure-hosts)
---------------------------------

If you're using a setup in which you want to trust a self-signed certificate or otherwise disable
certificate verification, you can instruct uv to allow insecure connections to dedicated hosts via
the [`allow-insecure-host`](../../../reference/settings/#allow-insecure-host) configuration option.
For example, adding the following to `pyproject.toml` will allow insecure connections to
`example.com`:

```
[tool.uv]
allow-insecure-host = ["example.com"]
```

`allow-insecure-host` expects to receive a hostname (e.g., `localhost`) or hostname-port pair (e.g.,
`localhost:8080`), and is only applicable to HTTPS connections, as HTTP connections are inherently
insecure.

Use `allow-insecure-host` with caution and only in trusted environments, as it can expose you to
security risks due to the lack of certificate verification.

July 28, 2026

Back to top