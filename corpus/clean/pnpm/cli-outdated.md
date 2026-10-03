pnpm outdated
=============

Checks for outdated packages. The check can be limited to a subset of the
installed packages by providing arguments (patterns are supported).

Examples:

```
pnpm outdated
pnpm outdated "*gulp-*" @babel/core
```

Options
--------------------

### --recursive, -r

Check for outdated dependencies in every package found in subdirectories, or in
every workspace package when executed inside a workspace.

### --filter <package\_selector>

[Read more about filtering.](/filtering)

### --global, -g

List outdated global packages.

### --long

Print details.

### --format <format>

* Default: **table**
* Type: **table**, **list**, **json**

Prints the outdated dependencies in the given format.

### --compatible

Prints only versions that satisfy specifications in `package.json`.

### --dev, -D

Checks only `devDependencies`.

### --prod, -P

Checks only `dependencies` and `optionalDependencies`.

### --no-optional

Doesn't check `optionalDependencies`.

### --sort-by

Specifies the order in which the output results are sorted. Currently only the value `name` is accepted.

### --include-github-actions

Added in: v11.16.0

Also check the GitHub Actions referenced by the repository's workflow files for updates. You can enable this by default by setting [`update.githubActions`](/settings/dependency-resolution#updategithubactions) to `true` in `pnpm-workspace.yaml`. See [Updating GitHub Actions](/cli/update#updating-github-actions).
