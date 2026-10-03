pnpm stage
==========

Added in: v11.3.0

Stages packages for publishing using npm's [staged publishing](https://docs.npmjs.com/staged-publishing) workflow. Staged versions are not resolved by `pnpm install` until they are explicitly approved, letting you defer proof-of-presence (2FA) to a later point in time — useful for verifying release artifacts, smoke-testing CI, or coordinating multi-package releases.

```
pnpm stage <subcommand> [options]
```

Subcommands[#](#subcommands)
----------------------------

### publish[#](#publish)

Stage a package for publishing.

```
pnpm stage publish [<tarball>|<dir>] [--tag <tag>] [--access <public|restricted>] [options]
```

Accepts the same arguments as [`pnpm publish`](/cli/publish), but uploads the tarball to staging instead of promoting it to the live registry. The resulting **stage id** is printed and can be used with the other subcommands.

Use `--recursive` (or `-r`) to stage every publishable package in the workspace.

### list[#](#list)

List all staged package versions, or list the staged versions of a specific package.

```
pnpm stage list [<package-spec>]
```

### view[#](#view)

Show details of a specific staged version.

```
pnpm stage view <stage-id>
```

### approve[#](#approve)

Approve a staged version, promoting it to the live registry. This is the step that consumes the one-time password.

```
pnpm stage approve [<stage-id>...] [--otp <otp>]
```

Since v12.0.0, several stage ids may be approved at once, and running `approve`
with none opens an interactive picker over the staged versions:

```
pnpm stage approve                     # pick interactively
pnpm stage approve <stage-id> <stage-id>
```

The whole batch is approved with a **single** one-time password; pnpm asks for a
new one only once the registry stops accepting the current one.

Inside a workspace the selected packages are approved in dependency order, and a
package whose workspace dependency could not be approved is skipped rather than
published against a dependency that never reached the registry.

### reject[#](#reject)

Reject a staged version and remove it from staging.

```
pnpm stage reject <stage-id> [--otp <otp>]
```

### download[#](#download)

Download the tarball of a staged version for inspection.

```
pnpm stage download <stage-id>
```

Options[#](#options)
--------------------

### --registry <url>[#](#--registry-url)

The base URL of the npm registry. Defaults to the configured default registry.

### --tag <tag>[#](#--tag-tag)

Registers the staged package with the given dist-tag. Defaults to `latest`.

### --access <public|restricted>[#](#--access-publicrestricted)

Tells the registry whether the staged package should be public or restricted.

### --json[#](#--json)

Show information in JSON format. Applies to `list`, `view`, `publish`, and `download`.

### --dry-run[#](#--dry-run)

Does everything `stage publish` would do except uploading to the registry.

### --otp <otp>[#](#--otp-otp)

One-time password for `approve` and `reject`.

### --recursive, -r[#](#--recursive--r)

Stage all publishable packages from the workspace.

### --filter <package\_selector>[#](#--filter-package_selector)

[Read more about filtering.](/filtering)