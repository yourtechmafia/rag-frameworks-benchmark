pnpm pack
=========

Create a tarball from a package.

Options[#](#options)
--------------------

### --recursive, -r[#](#--recursive--r)

Added in: v10.11.0

Pack all packages from the workspace.

### --out <path>[#](#--out-path)

Customizes the output path for the tarball. Use `%s` and `%v` to include the package name and version, e.g., `%s.tgz` or `some-dir/%s-%v.tgz`. By default, the tarball is saved in the current working directory with the name `<package-name>-<version>.tgz`.

### --pack-destination <dir>[#](#--pack-destination-dir)

Directory in which `pnpm pack` will save tarballs. The default is the current working directory.

### --pack-gzip-level <level>[#](#--pack-gzip-level-level)

Specifying custom compression level.

### --json[#](#--json)

Log output in JSON format.

### --filter <package\_selector>[#](#--filter-package_selector)

Added in: v10.11.0

[Read more about filtering.](/filtering)

### --dry-run[#](#--dry-run)

Added in: v10.26.0

Does everything a normal run does, except actually packing the tarball. Useful for verifying the contents of the tarball.

### --skip-manifest-obfuscation[#](#--skip-manifest-obfuscation)

Added in: v11.3.0

Keep the original `packageManager` field and publish lifecycle scripts in the packed manifest instead of stripping them. The pnpm-specific `pnpm` field is still omitted.

Life Cycle Scripts[#](#life-cycle-scripts)
------------------------------------------

* `prepack`
* `prepare`
* `postpack`

Tip

You can also use the [`beforePacking` hook](/pnpmfile#hooksbeforepackingpkg-pkg--promisepkg) to programmatically modify the `package.json` contents before the tarball is created. This is useful for removing development-only fields or adding publication metadata without modifying your local `package.json`.