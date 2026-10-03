pnpm with
=========

Added in: v11.0.0

Run pnpm at a specific version (or the currently running one) for a single invocation, ignoring the `packageManager` and `devEngines.packageManager` fields of the project's manifest.

```
pnpm with <version|current> <args...>
```

The downloaded pnpm is installed using the same mechanism as [`pnpm self-update`](/cli/self-update) and cached in the global virtual store for reuse on subsequent runs.

Examples
----------------------

Run the globally installed pnpm, ignoring the version pinned in the manifest:

```
pnpm with current install
```

Run a specific version:

```
pnpm with 12.3.4 install
```

Use a dist-tag:

```
pnpm with next install
```

Related settings
--------------------------------------

### pmOnFail

If you want to permanently skip the `packageManager` / `devEngines.packageManager` check (for example, because version management is handled by asdf, mise, Volta, or a similar tool), set the [`pmOnFail`](/settings/cli#pmonfail) setting to `ignore` instead of running every command through `pnpm with`:

pnpm-workspace.yaml

```
pmOnFail: ignore
```
