Other Settings
==============

### savePrefix[#](#saveprefix)

* Default: **'^'**
* Type: **'^'**, **'~'**, **''**, **'='**

Configure how versions of packages installed to a `package.json` file get
prefixed.

For example, if a package has version `1.2.3`, by default its version is set to
`^1.2.3` which allows minor upgrades for that package, but after
`pnpm config set save-prefix='~'` it would be set to `~1.2.3` which only allows
patch upgrades.

Since v11.19.0, `=` is also accepted: newly added dependencies are saved with an
explicit `=` operator (`=1.2.3`), which pins the exact version. `pnpm update`
keeps the `=` operator when it updates such a pin.

This setting is ignored when the added package has a range specified. For
instance, `pnpm add foo@2` will set the version of `foo` in `package.json` to
`2`, regardless of the value of `savePrefix`.

### saveTypes[#](#savetypes)

Added in: v12.6.0

* Default: **false**
* Type: **Boolean**

When set to `true`, `pnpm add` saves available `@types/*` packages in
`devDependencies` alongside registry dependencies. Packages that declare bundled
TypeScript types are skipped.

pnpm-workspace.yaml

```
saveTypes: true
```

You can also pass it as a CLI flag: `pnpm add --save-types express`.

### tag[#](#tag)

* Default: **latest**
* Type: **String**

If you `pnpm add` a package and you don't provide a specific version, then it
will install the package at the version registered under the tag from this
setting.

This also sets the tag that is added to the `package@version` specified by the
`pnpm tag` command if no explicit tag is given.

### globalDir[#](#globaldir)

* Default:
  + If the **$XDG\_DATA\_HOME** env variable is set, then **$XDG\_DATA\_HOME/pnpm/global**
  + On Windows: **~/AppData/Local/pnpm/global**
  + On macOS: **~/Library/pnpm/global**
  + On Linux: **~/.local/share/pnpm/global**
* Type: **path**

Specify a custom directory to store global packages.

### globalBinDir[#](#globalbindir)

* Default:
  + If the **$XDG\_DATA\_HOME** env variable is set, then **$XDG\_DATA\_HOME/pnpm/bin**
  + On Windows: **~/AppData/Local/pnpm/bin**
  + On macOS: **~/Library/pnpm/bin**
  + On Linux: **~/.local/share/pnpm/bin**
* Type: **path**

Allows to set the target directory for the bin files of globally installed packages.

Tip

In pnpm v11, globally installed binaries are stored in a `bin` subdirectory of `PNPM_HOME` instead of directly in `PNPM_HOME`. This prevents internal directories like `global/` and `store/` from polluting shell autocompletion when `PNPM_HOME` is on PATH. After upgrading, run `pnpm setup` to update your shell configuration.

### globalShims[#](#globalshims)

Added in: v12.0.0-rc.2

* Default: **{ node: auto, deno: auto, bun: auto }**
* Type: **Boolean**, **Object**

Controls which globally installed packages get [project-aware shims](/global-packages#project-aware-global-bins) — global commands that run the version the current project asks for instead of the globally installed one.

The setting is a map from **package name** to policy. The key is the name of the package that *provides* the command, not the command itself, so an entry for `typescript` covers its `tsc` bin.

```
globalShims:
  node: auto
  deno: false
  typescript: prompt
```

The supported policies are:

| Value | Behavior |
| --- | --- |
| `auto` (or `true`) | Switch automatically when the candidate is authenticated by a publisher signature; otherwise ask for confirmation once. |
| `prompt` | Put every candidate through the confirmation gate, including signature-verified ones. Answers are still remembered, so this asks once per project and candidate, not on every run. |
| `always` | Always switch, never ask. Usable in CI, where a prompt would fall back to the global version. |
| `false` | Disable the project-aware shim for this package. |

Since v12.0.0-rc.6, two commands write entries here for you: [`pnpm shim add <pkg>`](/cli/shim) records the package it links a shim for, and installing a [package manager](/package-managers) globally (`pnpm add -g yarn`) records that package manager so it follows a project's pin. Neither overwrites an entry you set yourself — including `false`, and including a `globalShims: false` that turns every shim off.

Layers merge key by key over the built-in defaults, so a single entry can change one package without restating the rest — `globalShims: { bun: false }` leaves `node` and `deno` at `auto`.

The scalar shorthands replace the whole map instead of merging: `globalShims: false` disables every project-aware shim, and `globalShims: true` resets to the defaults.

Warning

This setting is only read from locations a project cannot write to: the [global configuration file](/cli/config), a `pnpm-workspace.yaml` in the pnpm home directory itself, and the `PNPM_CONFIG_GLOBAL_SHIMS` environment variable (a JSON value), applied in that order. A project's own `pnpm-workspace.yaml` is ignored — otherwise a repository could grant itself the right to run its own binaries in place of your global ones.

Disabling a package, or changing its policy, takes effect on the very next command — the setting is re-read on each dispatch, so no reinstall is needed.

Newly *enabling* a package is the exception. pnpm decides at install time which bins to write dispatching shims for, so a package that was already installed globally while it was disabled needs to be reinstalled to pick up the change:

```
pnpm add -g typescript
```

To bypass dispatch for a single invocation, set `PNPM_SHIM_BYPASS=1`:

```
PNPM_SHIM_BYPASS=1 node --version
```

Note

Project-aware shims are a pnpm v12 feature and are not available in v11.

### npmrcAuthFile[#](#npmrcauthfile)

Added in: v11.0.0

* Default: **~/.npmrc**
* Type: **path**

The path to a file containing registry authentication tokens. By default, pnpm reads auth tokens from `~/.npmrc` as a fallback for registry authentication. Use this setting to point to a different file instead.

This setting cannot be set in `pnpm-workspace.yaml` at the project level; set it in the global configuration file, via the `--npmrc-auth-file` CLI option, or via the `PNPM_CONFIG_NPMRC_AUTH_FILE` environment variable (the npm-style `NPM_CONFIG_USERCONFIG` is honored as a fallback). A relative path is resolved against the working directory.

### stateDir[#](#statedir)

* Default:
  + If the **$XDG\_STATE\_HOME** env variable is set, then **$XDG\_STATE\_HOME/pnpm**
  + On Windows: **~/AppData/Local/pnpm-state**
  + On macOS: **~/.pnpm-state**
  + On Linux: **~/.local/state/pnpm**
* Type: **path**

The directory where pnpm stores machine-level state, including the update checker's `pnpm-state.json` file.

Since v12.5.0, [task concurrency groups](/workspace-task-orchestration#concurrencygroups) also store their shared slot files under `stateDir/run-slots`. Processes must use the same `stateDir` to share group limits. Different state directories create independent slot pools, so their combined task count can exceed the configured limit.

Set `stateDir` in the [global configuration file](/cli/config) or on the command line. It is ignored in project `pnpm-workspace.yaml` files.

### cacheDir[#](#cachedir)

* Default:
  + If the **$XDG\_CACHE\_HOME** env variable is set, then **$XDG\_CACHE\_HOME/pnpm**
  + On Windows: **~/AppData/Local/pnpm-cache**
  + On macOS: **~/Library/Caches/pnpm**
  + On Linux: **~/.cache/pnpm**
* Type: **path**

The location of the cache (package metadata, dlx cache, and some install verification results).

Like the store, the cache directory is intended to be shared only between mutually trusted users, jobs, and processes. If you configure or restore a shared `cacheDir`, protect it with filesystem permissions so untrusted users cannot write to it.

### useStderr[#](#usestderr)

* Default: **false**
* Type: **Boolean**

When true, all the output is written to stderr.

### updateNotifier[#](#updatenotifier)

* Default: **true**
* Type: **Boolean**

Set to `false` to suppress the update notification when using an older version of pnpm than the latest.

`pnpm install` and `pnpm add` check at most once a day, and print how to get the
newer version. pnpm 12 recognized but ignored this setting until v12.0.0, where
it started checking too.

### preferSymlinkedExecutables[#](#prefersymlinkedexecutables)

* Default: **true**, when **node-linker** is set to **hoisted** and the system is POSIX
* Type: **Boolean**

Create symlinks to executables in `node_modules/.bin` instead of command shims. This setting is ignored on Windows, where only command shims work.

### ignoreCompatibilityDb[#](#ignorecompatibilitydb)

* Default: **false**
* Type: **Boolean**

During installation the dependencies of some packages are automatically patched. If you want to disable this, set this config to `true`.

The patches are applied from Yarn's [`@yarnpkg/extensions`](https://github.com/yarnpkg/berry/blob/master/packages/yarnpkg-extensions/sources/index.ts) package, plus pnpm's
own curated entries.

Since v12.0.0, the database no longer carries entries that were derived from
static analysis of published packages. Those entries named packages a dependent
imported only for its *types*. Adding them was at best unnecessary and at worst
broke the dependent: `@typescript-eslint/types` gained a `typescript` dependency
resolved to the newest release, which put TypeScript 7 under older
`@typescript-eslint` versions and made ESLint fail with `Cannot read properties of undefined (reading 'Intrinsic')`.

### resolutionMode[#](#resolutionmode)

* Default: **highest** (was **lowest-direct** from v8.0.0 to v8.6.12)
* Type: **highest**, **time-based**, **lowest-direct**

When `resolutionMode` is set to `time-based`, dependencies will be resolved the following way:

1. Direct dependencies will be resolved to their lowest versions. So if there is `foo@^1.1.0` in the dependencies, then `1.1.0` will be installed.
2. Subdependencies will be resolved from versions that were published no later than one hour after the newest direct dependency. If none of those versions satisfies a subdependency's range, pnpm installs the lowest version that does.

If [`minimumReleaseAge`](/settings/dependency-resolution#minimumreleaseage) is also set, pnpm resolves subdependencies against whichever of the two cutoffs is earlier. If no version published before that cutoff satisfies a subdependency's range, pnpm installs the lowest matching version that is older than the `minimumReleaseAge` cutoff. If every matching version is newer than the `minimumReleaseAge` cutoff, pnpm falls back to the lowest matching version, and [`minimumReleaseAgeStrict`](/settings/dependency-resolution#minimumreleaseagestrict) decides whether pnpm installs it or fails. Only the `minimumReleaseAge` cutoff decides which versions pnpm reports as too new. A version that is newer than the time-based cutoff but older than the `minimumReleaseAge` cutoff is installed without a warning or error.

With this resolution mode installations with warm cache are faster. It also reduces the chance of subdependency hijacking as subdependencies will be updated only if direct dependencies are updated.

This resolution mode works only with npm's [full metadata](https://github.com/npm/registry/blob/master/docs/responses/package-metadata.md#full-metadata-format). So it is slower in some scenarios. However, if you use [Verdaccio](https://verdaccio.org/) v5.15.1 or newer, you may set the `registrySupportsTimeField` setting to `true`, and it will be really fast.

When `resolutionMode` is set to `lowest-direct`, direct dependencies will be resolved to their lowest versions.

Only the dependencies declared in `package.json` count as direct here. A peer dependency that [`autoInstallPeers`](/settings/peer-dependencies#autoinstallpeers) adds is not something the project declared, so it is resolved like a subdependency: to the highest version satisfying the peer range, or under `time-based`, to the highest version within the publish-date cutoff.

### registrySupportsTimeField[#](#registrysupportstimefield)

* Default: **false**
* Type: **Boolean**

Set this to `true` if the registry that you are using returns the "time" field in the abbreviated metadata. [Verdaccio](https://verdaccio.org/) supports this from v5.15.1, as do some registry proxies.

Since v11.23.0, this can also be declared per registry, through the `supportsTimeField` field of a [registry declaration](/registries#supportstimefield). A registry's own declaration wins; this setting is the answer for every registry the project does not describe.

### extendNodePath[#](#extendnodepath)

* Default: **true**
* Type: **Boolean**

When `true`, pnpm sets the `NODE_PATH` environment variable in command shims
(the wrapper scripts created in `node_modules/.bin`). When `false`, `NODE_PATH`
is not set.

#### Why this is needed[#](#why-this-is-needed)

pnpm's [isolated `node_modules` layout](/symlinked-node-modules-structure) means that a package can only access its
own declared dependencies. However, when a CLI tool runs via a command shim, some
libraries (notably [`import-local`](https://github.com/sindresorhus/import-local), used by jest, eslint, and others) resolve
modules from the **current working directory** rather than from the binary's own
location. Since the working directory is the project root — not the package inside
the virtual store — the standard `node_modules` resolution from the CWD won't
find the binary's transitive dependencies.

To bridge this gap, pnpm includes two types of paths in `NODE_PATH`:

1. **The package's own dependencies directory** (e.g.,
   `.pnpm/pkg@version/node_modules`) — this allows CWD-based resolution to find
   the correct versions of the package's sibling dependencies.
2. **The hoisted `node_modules` directory** (e.g., `.pnpm/node_modules`) — this
   is the directory where hoisted packages are placed when [`hoistPattern`](/settings/node-modules#hoistpattern) is
   set. Node.js cannot discover this directory through its standard resolution
   algorithm, so it must be provided via `NODE_PATH`.

`NODE_PATH` is also essential when [`enableGlobalVirtualStore`](/settings/node-modules#enableglobalvirtualstore) is enabled.
With a global virtual store, packages are symlinked from a central location
outside the project, so Node.js's standard upward `node_modules` traversal from
the binary's real path won't reach the project's own `node_modules` or its hoisted
dependencies. In this case, `NODE_PATH` must include both the project's root
`node_modules` and the hoisted directory at `node_modules/.pnpm/node_modules` to
ensure correct resolution.

#### When to disable[#](#when-to-disable)

You may set this to `false` if you are certain that none of the CLI tools in your
project resolve modules from the working directory and you are not using a global
virtual store. Disabling it produces slightly simpler command shims.

### deployAllFiles[#](#deployallfiles)

* Default: **false**
* Type: **Boolean**

When deploying a package or installing a local package, all files of the package are copied. By default, if the package has a `"files"` field in the `package.json`, then only the listed files and directories are copied.

### dedupeDirectDeps[#](#dedupedirectdeps)

* Default: **false**
* Type: **Boolean**

When set to `true`, dependencies that are already symlinked to the root `node_modules` directory of the workspace will not be symlinked to subproject `node_modules` directories.

### optimisticRepeatInstall[#](#optimisticrepeatinstall)

Added in: v10.1.0

* Default: **true**
* Type: **Boolean**

When enabled, a fast check will be performed before proceeding to installation. This way a repeat install or an install on a project with everything up-to-date becomes a lot faster.

### requiredScripts[#](#requiredscripts)

Scripts listed in this array will be required in each project of the workspace. Otherwise, `pnpm -r run <script name>` will fail.

```
requiredScripts:
- build
```

### enablePrePostScripts[#](#enableprepostscripts)

* Default: **true**
* Type: **Boolean**

When `true`, pnpm will run any pre/post scripts automatically. So running `pnpm foo`
will be like running `pnpm prefoo && pnpm foo && pnpm postfoo`.

### scriptShell[#](#scriptshell)

* Default: **null**
* Type: **path**

The shell to use for scripts run with the `pnpm run` command.

For instance, to force usage of Git Bash on Windows:

```
pnpm config set scriptShell "C:\\Program Files\\git\\bin\\bash.exe"
```

Since v12.4.0, a relative path in `pnpm-workspace.yaml` resolves from the workspace root, including for scripts that run in a nested package. A bare command name such as `bash` is still looked up on `PATH`.

### shellEmulator[#](#shellemulator)

* Default: **false**
* Type: **Boolean**

When `true`, pnpm will use a JavaScript implementation of a [bash-like shell](https://www.npmjs.com/package/@yarnpkg/shell) to
execute scripts.

This option simplifies cross-platform scripting. For instance, by default, the
next script will fail on non-POSIX-compliant systems:

```
"scripts": {
  "test": "NODE_ENV=test node test.js"
}
```

But if the `shellEmulator` setting is set to `true`, it will work on all
platforms.

Since v12.8.0, a configured non-empty `scriptShell` wins over `shellEmulator`
for `pnpm run` and lifecycle scripts. The emulator runs only when `scriptShell`
is unset or empty.

Note

Node.js 22 or higher supports running scripts without pnpm's assistance. For the example above, you can run the `test` script with `node --run test`. However, the `shellEmulator` option has no effect on this. Scripts that depend on POSIX features are required to be run `pnpm run` instead of `node --run` to work in non-POSIX-compliant environments.

### catalogMode[#](#catalogmode)

Added in: v10.12.1

* Default: **manual**
* Type: **manual**, **strict**, **prefer**

Controls if and how dependencies are added to the default catalog, when running `pnpm add`. There are three modes:

* **strict** - only allows dependency versions from the catalog. Adding a dependency outside the catalog's version range will cause an error.
* **prefer** - prefers catalog versions, but will fall back to direct dependencies if no compatible version is found.
* **manual** (default) - does not automatically add dependencies to the catalog.

Since v12.3.0, a specifier that names a location rather than a version is never moved into a catalog: local paths, local tarballs, tarball URLs, and `workspace:<path>` ranges stay in the `package.json` that declares them. Such a specifier is resolved relative to its own project, so one catalog entry could not mean the same directory for every project referencing it.

### ci[#](#ci)

Added in: v10.12.1

* Default: **true** (when the environment is detected as CI)
* Type: **Boolean**

This setting explicitly tells pnpm whether the current environment is a CI (Continuous Integration) environment.

### catalogPrune[#](#catalogprune)

Added in: v11.22.0 (as `cleanupUnusedCatalogs` since v10.15.0)

* Default: **false**
* Type: **Boolean**

When set to `true`, pnpm will remove unused catalog entries during installation.

`cleanupUnusedCatalogs` is the deprecated spelling of this setting and continues to work; when both are set, `catalogPrune` wins.

### macosBackup.excludeModulesDir[#](#macosbackupexcludemodulesdir)

Added in: v12.6.0

* Default: **false**
* Type: **Boolean**

When set to `true` on macOS, pnpm marks newly created `node_modules`, virtual-store, and similar directories with the `com.apple.metadata:com_apple_backup_excludeItem` extended attribute, so Time Machine skips them.

Set it in the [global configuration file](/cli/config) or via the `PNPM_CONFIG_MACOS_BACKUP_EXCLUDE_MODULES_DIR` environment variable. This setting is ignored in project `pnpm-workspace.yaml` files and on non-macOS platforms.

config.yaml

```
macosBackup:
  excludeModulesDir: true
```

### macosBackup.excludeStoreDir[#](#macosbackupexcludestoredir)

Added in: v12.6.0

* Default: **false**
* Type: **Boolean**

When set to `true` on macOS, pnpm marks newly created package-store directories with the Time Machine exclusion attribute.

Set it in the [global configuration file](/cli/config) or via the `PNPM_CONFIG_MACOS_BACKUP_EXCLUDE_STORE_DIR` environment variable. This setting is ignored in project `pnpm-workspace.yaml` files and on non-macOS platforms.

config.yaml

```
macosBackup:
  excludeStoreDir: true
```