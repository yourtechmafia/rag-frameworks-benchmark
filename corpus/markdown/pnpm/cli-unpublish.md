pnpm unpublish
==============

Added in: v11.0.0

Remove a published package version from the registry.

```
pnpm unpublish [<pkg>[@<version>]] [--force]
```

Warning

Unpublishing is generally discouraged. Most registries (including the public npm registry) restrict when and how packages can be unpublished. Prefer [`pnpm deprecate`](/cli/deprecate) whenever possible.

Examples[#](#examples)
----------------------

Unpublish a specific version:

```
pnpm unpublish foo@1.0.0
```

Unpublish a range of versions using a semver specifier:

```
pnpm unpublish "foo@<2"
```

Unpublish an entire package (all versions). Requires `--force`:

```
pnpm unpublish foo --force
```

When run without arguments inside a package directory, pnpm unpublishes the current package version read from the local `package.json`.

Options[#](#options)
--------------------

### --force[#](#--force)

Required when removing an entire package (all versions) rather than a specific version or range.

### --registry <url>[#](#--registry-url)

The registry to publish to. Defaults to the registry configured for the package.

### --otp <code>[#](#--otp-code)

When the registry requires two-factor authentication, supply the one-time password via this flag or the `PNPM_CONFIG_OTP` environment variable.