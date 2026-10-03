pnpm ci
=======

Added in: v11.0.0

Aliases: `clean-install`, `ic`, `install-clean`

Perform a clean install. This command runs [`pnpm clean`](/cli/clean) followed by [`pnpm install --frozen-lockfile`](/cli/install).

Designed for CI/CD environments where reproducible builds are critical.

```
pnpm ci
```