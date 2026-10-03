Settings (pnpm-workspace.yaml)
==============================

pnpm gets its configuration from the command line, environment variables, and `pnpm-workspace.yaml`.

Only auth and registry settings are read from `.npmrc` files. All other settings are configured in `pnpm-workspace.yaml` or the [global `config.yaml`](/configuring#global-configuration). Some settings are limited to one of them: settings that define the structure of `node_modules` (like `hoistPattern`, `publicHoistPattern`, `nodeLinker`, or `shamefullyHoist`) can only be set in `pnpm-workspace.yaml`, while settings that name machine-level state (like `stateDir` or `pnpmHomeDir`) are not read from `pnpm-workspace.yaml`.

The `pnpm config` command can be used to read and edit the contents of the project and global configuration files.

The relevant configuration files are:

* Per-project configuration file: `/path/to/my/project/pnpm-workspace.yaml`
* [Global configuration file](/cli/config)

Note

Authorization-related settings are handled via [`.npmrc`](/npmrc).

Values in the configuration files may contain env variables using the `${NAME}` syntax. The env variables may also be specified with default values. Using `${NAME-fallback}` will return `fallback` if `NAME` isn't set. `${NAME:-fallback}` will return `fallback` if `NAME` isn't set, or is an empty string. Since v12.7.0, `${NAME?}` expands to an empty string without a warning when `NAME` isn't set, as in npm.

Warning

Since v11.5.3, env variables are **not** expanded in settings of `pnpm-workspace.yaml` that define registry URLs: `registry` and the URL values of [`registries`](/settings/dependency-resolution#registries) and [`namedRegistries`](/settings/dependency-resolution#namedregistries). Values containing a `${...}` placeholder in these settings are ignored. In the [registry declaration shape](/registries) of `registries` (since v11.23.0), the URL is the key rather than the value, and the same rule applies to the keys. Because `pnpm-workspace.yaml` is committed to the repository, expanding env variables in registry URLs could be exploited by a malicious repository to leak secrets from the environment to an attacker-controlled registry. Configure dynamic registry URLs in a trusted location instead: the global configuration file or CLI options.

Since v12.7.0, the same applies to `userAgent`: a `userAgent` in `pnpm-workspace.yaml` that contains a `${...}` placeholder is ignored, because the user agent is sent to the configured registry with every request.

Note

Since v11.22.0, a project's `pnpm-workspace.yaml` cannot choose where pnpm keeps its credentials, its own installation, or other machine-level state: `bin`, `configDir`, `dir`, `globalBinDir`, `globalDir`, `npmrcAuthFile`, `pnpmHomeDir`, `stateDir`, `userconfig`, and `workspaceDir` are ignored there, with a warning. Set them in the [global configuration file](/cli/config) or on the command line instead. `cacheDir` and `storeDir` are unaffected.

packages
----------------------

Besides settings, `pnpm-workspace.yaml` defines the root of the [workspace](/workspaces) and
enables you to include / exclude directories from the workspace. If the
`packages` field is omitted, only the root package is included in the workspace.

For example:

pnpm-workspace.yaml

```
packages:
  # specify a package in a direct subdir of the root
  - 'my-app'
  # all packages in direct subdirs of packages/
  - 'packages/*'
  # all packages in subdirs of components/
  - 'components/**'
  # exclude packages that are inside test directories
  - '!**/test/**'
```

The root package is always included, even when custom location wildcards are
used.

A pattern may be written with a `./` prefix, may contain `.` and `..` segments,
and may repeat slashes: `./packages/*` and `packages//*` select the same
projects, and `!./packages/legacy` excludes the same directory that
`!packages/legacy` does. A `*` never matches a name beginning with a dot, so
`packages/*` skips `packages/.cache`; name such a directory explicitly to
include it.

Note

pnpm reads the workspace from `pnpm-workspace.yaml`, not from the `workspaces`
field of the root `package.json`. Since v12.4.1, a root manifest that declares a
non-empty `workspaces` array in a project with no `pnpm-workspace.yaml` gets a
warning, because such an install silently links no project at all.

Catalogs are also defined in the `pnpm-workspace.yaml` file. See [*Catalogs*](/catalogs) for details.

pnpm-workspace.yaml

```
packages:
  - 'packages/*'

catalog:
  chalk: ^4.1.2

catalogs:
  react16:
    react: ^16.7.0
    react-dom: ^16.7.0
  react17:
    react: ^17.10.0
    react-dom: ^17.10.0
```

packageConfigs
----------------------------------

Added in: v11.0.0

Allows setting project-specific configuration for individual workspace packages. This replaces workspace project-specific `.npmrc` files.

`packageConfigs` can be specified as a map of package names to config objects:

pnpm-workspace.yaml

```
packages:
  - "packages/project-1"
  - "packages/project-2"
packageConfigs:
  "project-1":
    saveExact: true
  "project-2":
    savePrefix: "~"
```

Or as an array of pattern-matched rules:

pnpm-workspace.yaml

```
packages:
  - "packages/project-1"
  - "packages/project-2"
packageConfigs:
  - match: ["project-1", "project-2"]
    modulesDir: "node_modules"
    saveExact: true
```

Settings that shape resolution or the layout of `node_modules` (`overrides`,
`hoist`, `modulesDir`, `saveExact`, `savePrefix`, and their neighbours) take
effect per project only where each project has its own lockfile, that is with
[`sharedWorkspaceLockfile: false`](/workspaces#sharedworkspacelockfile). A
workspace on the default shared lockfile has one resolution for every project,
so pnpm reports which entries it ignored instead of applying them silently.

Settings
----------------------

Every setting is listed below, grouped by topic. Follow a setting to read its documentation, or open the full reference of a group.

### Dependency Resolution

[Full reference →](/settings/dependency-resolution)

* [overrides](/settings/dependency-resolution#overrides)
  + [Convergence overrides](/settings/dependency-resolution#convergence-overrides)
  + [Overriding peer dependencies](/settings/dependency-resolution#overriding-peer-dependencies)
* [packageExtensions](/settings/dependency-resolution#packageextensions)
* [allowedDeprecatedVersions](/settings/dependency-resolution#alloweddeprecatedversions)
* [update](/settings/dependency-resolution#update)
  + [update.ignoreDeps](/settings/dependency-resolution#updateignoredeps)
  + [update.changeset](/settings/dependency-resolution#updatechangeset)
  + [update.githubActions](/settings/dependency-resolution#updategithubactions)
  + [update.githubActionsServer](/settings/dependency-resolution#updategithubactionsserver)
* [supportedArchitectures](/settings/dependency-resolution#supportedarchitectures)
* [optional](/settings/dependency-resolution#optional)
* [ignoredOptionalDependencies](/settings/dependency-resolution#ignoredoptionaldependencies)
* [forceIgnoresPlatform](/settings/dependency-resolution#forceignoresplatform)
* [minimumReleaseAge](/settings/dependency-resolution#minimumreleaseage)
* [minimumReleaseAgeExclude](/settings/dependency-resolution#minimumreleaseageexclude)
* [minimumReleaseAgeExcludePrune](/settings/dependency-resolution#minimumreleaseageexcludeprune)
* [minimumReleaseAgeIgnoreMissingTime](/settings/dependency-resolution#minimumreleaseageignoremissingtime)
* [minimumReleaseAgeStrict](/settings/dependency-resolution#minimumreleaseagestrict)
* [trustPolicy](/settings/dependency-resolution#trustpolicy)
* [trustPolicyExclude](/settings/dependency-resolution#trustpolicyexclude)
* [trustPolicyIgnoreAfter](/settings/dependency-resolution#trustpolicyignoreafter)
* [trustPolicyExcludePrune](/settings/dependency-resolution#trustpolicyexcludeprune)
* [trustLockfile](/settings/dependency-resolution#trustlockfile)
* [blockExoticSubdeps](/settings/dependency-resolution#blockexoticsubdeps)
* [registries](/settings/dependency-resolution#registries)
* [namedRegistries](/settings/dependency-resolution#namedregistries)

### Node-Modules Settings

[Full reference →](/settings/node-modules#node-modules-settings)

* [modulesDir](/settings/node-modules#modulesdir)
* [nodeLinker](/settings/node-modules#nodelinker)
* [nodeExperimentalPackageMap](/settings/node-modules#nodeexperimentalpackagemap)
* [nodePackageMapType](/settings/node-modules#nodepackagemaptype)
* [symlink](/settings/node-modules#symlink)
* [enableModulesDir](/settings/node-modules#enablemodulesdir)
* [virtualStoreDir](/settings/node-modules#virtualstoredir)
* [virtualStoreDirMaxLength](/settings/node-modules#virtualstoredirmaxlength)
* [virtualStoreOnly](/settings/node-modules#virtualstoreonly)
* [packageImportMethod](/settings/node-modules#packageimportmethod)
* [modulesCacheMaxAge](/settings/node-modules#modulescachemaxage)
* [dlxCacheMaxAge](/settings/node-modules#dlxcachemaxage)
* [virtualStoreType](/settings/node-modules#virtualstoretype)
* [enableGlobalVirtualStore](/settings/node-modules#enableglobalvirtualstore)

### Dependency Hoisting Settings

[Full reference →](/settings/node-modules#dependency-hoisting-settings)

* [hoist](/settings/node-modules#hoist)
* [hoistPattern](/settings/node-modules#hoistpattern)
* [publicHoistPattern](/settings/node-modules#publichoistpattern)
* [hoistWorkspacePackages](/settings/node-modules#hoistworkspacepackages)
* [shamefullyHoist](/settings/node-modules#shamefullyhoist)
* [hoistingLimits](/settings/node-modules#hoistinglimits)

### Store Settings

[Full reference →](/settings/store#store-settings)

* [storeDir](/settings/store#storedir)
* [verifyStoreIntegrity](/settings/store#verifystoreintegrity)
* [useRunningStoreServer](/settings/store#userunningstoreserver)
* [strictStorePkgContentCheck](/settings/store#strictstorepkgcontentcheck)
* [frozenStore](/settings/store#frozenstore)

### Lockfile Settings

[Full reference →](/settings/store#lockfile-settings)

* [lockfile](/settings/store#lockfile)
* [frozenLockfile](/settings/store#frozenlockfile)
* [preferFrozenLockfile](/settings/store#preferfrozenlockfile)
* [lockfileIncludeTarballUrl](/settings/store#lockfileincludetarballurl)
* [gitBranchLockfile](/settings/store#gitbranchlockfile)
* [mergeGitBranchLockfilesBranchPattern](/settings/store#mergegitbranchlockfilesbranchpattern)
* [peersSuffixMaxLength](/settings/store#peerssuffixmaxlength)

### Network Settings

[Full reference →](/settings/network#network-settings)

* [httpsProxy](/settings/network#httpsproxy)
* [httpProxy](/settings/network#httpproxy)
* [noProxy](/settings/network#noproxy)
* [localAddress](/settings/network#localaddress)
* [maxsockets](/settings/network#maxsockets)
* [strictSsl](/settings/network#strictssl)

### Request Settings

[Full reference →](/settings/network#request-settings)

* [gitShallowHosts](/settings/network#gitshallowhosts)
* [networkConcurrency](/settings/network#networkconcurrency)
* [fetchRetries](/settings/network#fetchretries)
* [fetchRetryFactor](/settings/network#fetchretryfactor)
* [fetchRetryMintimeout](/settings/network#fetchretrymintimeout)
* [fetchRetryMaxtimeout](/settings/network#fetchretrymaxtimeout)
* [fetchTimeout](/settings/network#fetchtimeout)
* [fetchWarnTimeoutMs](/settings/network#fetchwarntimeoutms)
* [fetchMinSpeedKiBps](/settings/network#fetchminspeedkibps)

### Peer Dependency Settings

[Full reference →](/settings/peer-dependencies)

* [autoInstallPeers](/settings/peer-dependencies#autoinstallpeers)
  + [Version Conflicts](/settings/peer-dependencies#version-conflicts)
  + [Conflict Resolution](/settings/peer-dependencies#conflict-resolution)
* [dedupePeerDependents](/settings/peer-dependencies#dedupepeerdependents)
* [dedupePeers](/settings/peer-dependencies#dedupepeers)
* [strictPeerDependencies](/settings/peer-dependencies#strictpeerdependencies)
* [resolvePeersFromWorkspaceRoot](/settings/peer-dependencies#resolvepeersfromworkspaceroot)
* [peerDependencyRules](/settings/peer-dependencies#peerdependencyrules)
  + [peerDependencyRules.ignoreMissing](/settings/peer-dependencies#peerdependencyrulesignoremissing)
  + [peerDependencyRules.allowedVersions](/settings/peer-dependencies#peerdependencyrulesallowedversions)
  + [peerDependencyRules.allowAny](/settings/peer-dependencies#peerdependencyrulesallowany)

### CLI Settings

[Full reference →](/settings/cli#cli-settings)

* [[no-]color](/settings/cli#no-color)
* [loglevel](/settings/cli#loglevel)
* [reporter](/settings/cli#reporter)
* [useBetaCli](/settings/cli#usebetacli)
* [recursiveInstall](/settings/cli#recursiveinstall)
* [engineStrict](/settings/cli#enginestrict)
* [npmPath](/settings/cli#npmpath)
* [pmOnFail](/settings/cli#pmonfail)
* [ignoreWorkspaceRootCheck](/settings/cli#ignoreworkspacerootcheck)

### Node.js Settings

[Full reference →](/settings/cli#nodejs-settings)

* [nodeVersion](/settings/cli#nodeversion)
* [runtimeOnFail](/settings/cli#runtimeonfail)
* [nodeDownloadMirrors](/settings/cli#nodedownloadmirrors)
* [tools](/settings/cli#tools)

### Build Settings

[Full reference →](/settings/build)

* [ignoreScripts](/settings/build#ignorescripts)
* [childConcurrency](/settings/build#childconcurrency)
* [sideEffectsCache](/settings/build#sideeffectscache)
* [sideEffectsCacheReadonly](/settings/build#sideeffectscachereadonly)
* [sideEffectsCache.remote](/settings/build#sideeffectscacheremote)
* [unsafePerm](/settings/build#unsafeperm)
* [nodeOptions](/settings/build#nodeoptions)
* [verifyDepsBeforeRun](/settings/build#verifydepsbeforerun)
* [strictDepBuilds](/settings/build#strictdepbuilds)
* [allowBuilds](/settings/build#allowbuilds)
* [dangerouslyAllowAllBuilds](/settings/build#dangerouslyallowallbuilds)

### Versioning Settings

[Full reference →](/settings/versioning)

* [versioning.fixed](/settings/versioning#versioningfixed)
* [versioning.ignore](/settings/versioning#versioningignore)
* [versioning.maxBump](/settings/versioning#versioningmaxbump)
* [versioning.lanes](/settings/versioning#versioninglanes)
* [versioning.epics](/settings/versioning#versioningepics)
* [versioning.changelog.storage](/settings/versioning#versioningchangelogstorage)

### Other Settings

[Full reference →](/settings/other)

* [savePrefix](/settings/other#saveprefix)
* [tag](/settings/other#tag)
* [globalDir](/settings/other#globaldir)
* [globalBinDir](/settings/other#globalbindir)
* [npmrcAuthFile](/settings/other#npmrcauthfile)
* [stateDir](/settings/other#statedir)
* [cacheDir](/settings/other#cachedir)
* [useStderr](/settings/other#usestderr)
* [updateNotifier](/settings/other#updatenotifier)
* [globalShims](/settings/other#globalshims)
* [preferSymlinkedExecutables](/settings/other#prefersymlinkedexecutables)
* [ignoreCompatibilityDb](/settings/other#ignorecompatibilitydb)
* [resolutionMode](/settings/other#resolutionmode)
* [registrySupportsTimeField](/settings/other#registrysupportstimefield)
* [extendNodePath](/settings/other#extendnodepath)
  + [Why this is needed](/settings/other#why-this-is-needed)
  + [When to disable](/settings/other#when-to-disable)
* [deployAllFiles](/settings/other#deployallfiles)
* [dedupeDirectDeps](/settings/other#dedupedirectdeps)
* [optimisticRepeatInstall](/settings/other#optimisticrepeatinstall)
* [requiredScripts](/settings/other#requiredscripts)
* [enablePrePostScripts](/settings/other#enableprepostscripts)
* [scriptShell](/settings/other#scriptshell)
* [shellEmulator](/settings/other#shellemulator)
* [catalogMode](/settings/other#catalogmode)
* [ci](/settings/other#ci)
* [catalogPrune](/settings/other#catalogprune)

### Workspace Settings

These settings are configured in `pnpm-workspace.yaml` as well, but are documented together with the workspace feature they belong to.

[Full reference →](/workspaces#configuration)

* [linkWorkspacePackages](/workspaces#linkworkspacepackages)
* [injectWorkspacePackages](/workspaces#injectworkspacepackages)
* [dedupeInjectedDeps](/workspaces#dedupeinjecteddeps)
* [syncInjectedDepsAfterScripts](/workspaces#syncinjecteddepsafterscripts)
* [preferWorkspacePackages](/workspaces#preferworkspacepackages)
* [sharedWorkspaceLockfile](/workspaces#sharedworkspacelockfile)
* [saveWorkspaceProtocol](/workspaces#saveworkspaceprotocol)
* [includeWorkspaceRoot](/workspaces#includeworkspaceroot)
* [ignoreWorkspaceCycles](/workspaces#ignoreworkspacecycles)
* [disallowWorkspaceCycles](/workspaces#disallowworkspacecycles)
* [workspaceConcurrency](/workspaces#workspaceconcurrency)
* [ignoreWorkspaceRootCheck](/workspaces#ignoreworkspacerootcheck)
* [failIfNoMatch](/workspaces#failifnomatch)

### Settings documented elsewhere

* [publishWaitTimeout](/cli/publish#publishwaittimeout)
* [patchedDependencies](/cli/patch#patcheddependencies)
* [pnpmfile](/pnpmfile#pnpmfile), [globalPnpmfile](/pnpmfile#globalpnpmfile) and [ignorePnpmfile](/pnpmfile#ignorepnpmfile)
* [audit.level](/cli/audit#auditlevel), [audit.ignore](/cli/audit#auditignore) and [audit.ignorePrune](/cli/audit#auditignoreprune)
* [initVersion](/cli/init#initversion), [initLicense](/cli/init#initlicense) and [initAuthorName / initAuthorEmail / initAuthorUrl](/cli/init#initauthorname-initauthoremail-initauthorurl)
* [legacyDirFiltering](/filtering#legacydirfiltering)
* [concurrencyGroups](/workspace-task-orchestration#concurrencygroups)
* [tasks](/workspace-task-orchestration#configure-task-dependencies), [pipelines](/cli/pipeline#pipelines) and [pipelineBase](/cli/pipeline#pipelinebase)
* [cargo.enabled](/cargo#cargoenabled) and [Cargo index](/cargo#cargo-index)
* [python.enabled](/python#pythonenabled), [python.executable](/python#pythonexecutable), [Python indexes](/python#python-indexes), [python.extras](/python#pythonextras) and [python.groups](/python#pythongroups)
* [python.versions](/python#pythonversions), [python.overrides](/python#pythonoverrides) and [python.constraints](/python#pythonconstraints)
* Authorization settings, which are read from [`.npmrc`](/npmrc)
