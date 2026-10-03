pnpm repo
=========

Added in: v11.3.0

Opens the URL of a package's repository in the browser.

```
pnpm repo [<pkg> ...]
```

With no arguments, opens the repository of the current project (read from the `repository` field of `package.json`).

With one or more package names, fetches each package's metadata from the registry and opens its repository URL.

The repository URL is normalized to its web equivalent — e.g. `git+ssh://git@github.com/foo/bar.git` opens as `https://github.com/foo/bar`. When the `repository` field includes a `directory`, the URL points at that subdirectory inside the repo.

Examples[#](#examples)
----------------------

```
# Open the repo of the current project
pnpm repo

# Open the repo of a package on the registry
pnpm repo lodash

# Open multiple repos at once
pnpm repo react react-dom
```

Options[#](#options)
--------------------

### --registry <url>[#](#--registry-url)

The registry from which to fetch package metadata when an explicit package name is given. Per-scope and named registries (configured via [`registries`](/settings/dependency-resolution#registries) and [`namedRegistries`](/settings/dependency-resolution#namedregistries)) are respected.