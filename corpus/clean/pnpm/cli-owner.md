pnpm owner
==========

Added in: v11.1.0

Aliases: `owners`

Manages package owners on the registry.

Commands
----------------------

### ls

```
pnpm owner ls <package>
```

Aliases: `list`

List all owners of a package. This is the default subcommand if no other subcommand is given.

### add

```
pnpm owner add <package> <user>
```

Add a user as an owner of a package. Requires authentication.

### rm

```
pnpm owner rm <package> <user>
```

Remove a user from the list of owners of a package. Requires authentication.

Options
--------------------

### --registry <url>

The base URL of the npm registry to use for the operation. Per-scope and named registries (configured via [`registries`](/settings/dependency-resolution#registries) and [`namedRegistries`](/settings/dependency-resolution#namedregistries)) are respected for the package being modified.

### --otp <otp>

When the registry requires two-factor authentication, this option supplies a one-time password.
