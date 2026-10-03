pnpm dist-tag
=============

Added in: v11.0.0

Manage distribution tags for a package. Dist-tags provide human-readable aliases (like `latest`, `next`, `beta`) that point to specific package versions on the registry.

```
pnpm dist-tag add <pkg>@<version> [<tag>]
pnpm dist-tag rm <pkg> <tag>
pnpm dist-tag ls [<pkg>]
```

Subcommands
----------------------------

### add <pkg>@<version> [<tag>]

Tag the specified version of a package with a dist-tag. If `<tag>` is omitted, the value of the [`tag`](/settings/other#tag) setting is used (defaults to `latest`).

```
pnpm dist-tag add foo@1.2.0 next
```

### rm <pkg> <tag>

Remove a dist-tag from a package.

```
pnpm dist-tag rm foo next
```

### ls [<pkg>]

List all dist-tags for a package. If no package name is given, the dist-tags for the current package (read from the local `package.json`) are shown.

```
pnpm dist-tag ls foo
```

Options
--------------------

### --registry <url>

The registry to operate on. Defaults to the registry configured for the package.

### --otp <code>

When the registry requires two-factor authentication, supply the one-time password via this flag or the `PNPM_CONFIG_OTP` environment variable.
