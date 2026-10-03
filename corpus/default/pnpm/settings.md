




Settings (pnpm-workspace.yaml) | pnpm






































Settings (pnpm-workspace.yaml)pnpm gets its configuration from the command line, environment variables, and pnpm-workspace.yaml.
Only auth and registry settings are read from .npmrc files. All other settings are configured in pnpm-workspace.yaml or the global config.yaml. Some settings are limited to one of them: settings that define the structure of node_modules (like hoistPattern, publicHoistPattern, nodeLinker, or shamefullyHoist) can only be set in pnpm-workspace.yaml, while settings that name machine-level state (like stateDir or pnpmHomeDir) are not read from pnpm-workspace.yaml.
The pnpm config command can be used to read and edit the contents of the project and global configuration files.
The relevant configuration files are:

Per-project configuration file: /path/to/my/project/pnpm-workspace.yaml
Global configuration file

Note
Authorization-related settings are handled via .npmrc.

Values in the configuration files may contain env variables using the ${NAME} syntax. The env variables may also be specified with default values. Using ${NAME-fallback} will return fallback if NAME isn't set. ${NAME:-fallback} will return fallback if NAME isn't set, or is an empty string. Since v12.7.0, ${NAME?} expands to an empty string without a warning when NAME isn't set, as in npm.
Warning
Since v11.5.3, env variables are not expanded in settings of pnpm-workspace.yaml that define registry URLs: registry and the URL values of registries and namedRegistries. Values containing a ${...} placeholder in these settings are ignored. In the registry declaration shape of registries (since v11.23.0), the URL is the key rather than the value, and the same rule applies to the keys. Because pnpm-workspace.yaml is committed to the repository, expanding env variables in registry URLs could be exploited by a malicious repository to leak secrets from the environment to an attacker-controlled registry. Configure dynamic registry URLs in a trusted location instead: the global configuration file or CLI options.
Since v12.7.0, the same applies to userAgent: a userAgent in pnpm-workspace.yaml that contains a ${...} placeholder is ignored, because the user agent is sent to the configured registry with every request.

Note
Since v11.22.0, a project's pnpm-workspace.yaml cannot choose where pnpm keeps its credentials, its own installation, or other machine-level state: bin, configDir, dir, globalBinDir, globalDir, npmrcAuthFile, pnpmHomeDir, stateDir, userconfig, and workspaceDir are ignored there, with a warning. Set them in the global configuration file or on the command line instead. cacheDir and storeDir are unaffected.

packages#
Besides settings, pnpm-workspace.yaml defines the root of the workspace and
enables you to include / exclude directories from the workspace. If the
packages field is omitted, only the root package is included in the workspace.
For example:
pnpm-workspace.yamlpackages:
  # specify a package in a direct subdir of the root
  - 'my-app'
  # all packages in direct subdirs of packages/
  - 'packages/*'
  # all packages in subdirs of components/
  - 'components/**'
  # exclude packages that are inside test directories
  - '!**/test/**'

The root package is always included, even when custom location wildcards are
used.
A pattern may be written with a ./ prefix, may contain . and .. segments,
and may repeat slashes: ./packages/* and packages//* select the same
projects, and !./packages/legacy excludes the same directory that
!packages/legacy does. A * never matches a name beginning with a dot, so
packages/* skips packages/.cache; name such a directory explicitly to
include it.
Note
pnpm reads the workspace from pnpm-workspace.yaml, not from the workspaces
field of the root package.json. Since v12.4.1, a root manifest that declares a
non-empty workspaces array in a project with no pnpm-workspace.yaml gets a
warning, because such an install silently links no project at all.

Catalogs are also defined in the pnpm-workspace.yaml file. See Catalogs for details.
pnpm-workspace.yamlpackages:
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

packageConfigs#
Added in: v11.0.0
Allows setting project-specific configuration for individual workspace packages. This replaces workspace project-specific .npmrc files.
packageConfigs can be specified as a map of package names to config objects:
pnpm-workspace.yamlpackages:
  - "packages/project-1"
  - "packages/project-2"
packageConfigs:
  "project-1":
    saveExact: true
  "project-2":
    savePrefix: "~"

Or as an array of pattern-matched rules:
pnpm-workspace.yamlpackages:
  - "packages/project-1"
  - "packages/project-2"
packageConfigs:
  - match: ["project-1", "project-2"]
    modulesDir: "node_modules"
    saveExact: true

Settings that shape resolution or the layout of node_modules (overrides,
hoist, modulesDir, saveExact, savePrefix, and their neighbours) take
effect per project only where each project has its own lockfile, that is with
sharedWorkspaceLockfile: false. A
workspace on the default shared lockfile has one resolution for every project,
so pnpm reports which entries it ignored instead of applying them silently.
Settings#
Every setting is listed below, grouped by topic. Follow a setting to read its documentation, or open the full reference of a group.
Dependency Resolution#
Full reference →

overrides

Convergence overrides
Overriding peer dependencies


packageExtensions
allowedDeprecatedVersions
update

update.ignoreDeps
update.changeset
update.githubActions
update.githubActionsServer


supportedArchitectures
optional
ignoredOptionalDependencies
forceIgnoresPlatform
minimumReleaseAge
minimumReleaseAgeExclude
minimumReleaseAgeExcludePrune
minimumReleaseAgeIgnoreMissingTime
minimumReleaseAgeStrict
trustPolicy
trustPolicyExclude
trustPolicyIgnoreAfter
trustPolicyExcludePrune
trustLockfile
blockExoticSubdeps
registries
namedRegistries

Node-Modules Settings#
Full reference →

modulesDir
nodeLinker
nodeExperimentalPackageMap
nodePackageMapType
symlink
enableModulesDir
virtualStoreDir
virtualStoreDirMaxLength
virtualStoreOnly
packageImportMethod
modulesCacheMaxAge
dlxCacheMaxAge
virtualStoreType
enableGlobalVirtualStore

Dependency Hoisting Settings#
Full reference →

hoist
hoistPattern
publicHoistPattern
hoistWorkspacePackages
shamefullyHoist
hoistingLimits

Store Settings#
Full reference →

storeDir
verifyStoreIntegrity
useRunningStoreServer
strictStorePkgContentCheck
frozenStore

Lockfile Settings#
Full reference →

lockfile
frozenLockfile
preferFrozenLockfile
lockfileIncludeTarballUrl
gitBranchLockfile
mergeGitBranchLockfilesBranchPattern
peersSuffixMaxLength

Network Settings#
Full reference →

httpsProxy
httpProxy
noProxy
localAddress
maxsockets
strictSsl

Request Settings#
Full reference →

gitShallowHosts
networkConcurrency
fetchRetries
fetchRetryFactor
fetchRetryMintimeout
fetchRetryMaxtimeout
fetchTimeout
fetchWarnTimeoutMs
fetchMinSpeedKiBps

Peer Dependency Settings#
Full reference →

autoInstallPeers

Version Conflicts
Conflict Resolution


dedupePeerDependents
dedupePeers
strictPeerDependencies
resolvePeersFromWorkspaceRoot
peerDependencyRules

peerDependencyRules.ignoreMissing
peerDependencyRules.allowedVersions
peerDependencyRules.allowAny



CLI Settings#
Full reference →

[no-]color
loglevel
reporter
useBetaCli
recursiveInstall
engineStrict
npmPath
pmOnFail
ignoreWorkspaceRootCheck

Node.js Settings#
Full reference →

nodeVersion
runtimeOnFail
nodeDownloadMirrors
tools

Build Settings#
Full reference →

ignoreScripts
childConcurrency
sideEffectsCache
sideEffectsCacheReadonly
sideEffectsCache.remote
unsafePerm
nodeOptions
verifyDepsBeforeRun
strictDepBuilds
allowBuilds
dangerouslyAllowAllBuilds

Versioning Settings#
Full reference →

versioning.fixed
versioning.ignore
versioning.maxBump
versioning.lanes
versioning.epics
versioning.changelog.storage

Other Settings#
Full reference →

savePrefix
tag
globalDir
globalBinDir
npmrcAuthFile
stateDir
cacheDir
useStderr
updateNotifier
globalShims
preferSymlinkedExecutables
ignoreCompatibilityDb
resolutionMode
registrySupportsTimeField
extendNodePath

Why this is needed
When to disable


deployAllFiles
dedupeDirectDeps
optimisticRepeatInstall
requiredScripts
enablePrePostScripts
scriptShell
shellEmulator
catalogMode
ci
catalogPrune

Workspace Settings#
These settings are configured in pnpm-workspace.yaml as well, but are documented together with the workspace feature they belong to.
Full reference →

linkWorkspacePackages
injectWorkspacePackages
dedupeInjectedDeps
syncInjectedDepsAfterScripts
preferWorkspacePackages
sharedWorkspaceLockfile
saveWorkspaceProtocol
includeWorkspaceRoot
ignoreWorkspaceCycles
disallowWorkspaceCycles
workspaceConcurrency
ignoreWorkspaceRootCheck
failIfNoMatch

Settings documented elsewhere#

publishWaitTimeout
patchedDependencies
pnpmfile, globalPnpmfile and ignorePnpmfile
audit.level, audit.ignore and audit.ignorePrune
initVersion, initLicense and initAuthorName / initAuthorEmail / initAuthorUrl
legacyDirFiltering
concurrencyGroups
tasks, pipelines and pipelineBase
cargo.enabled and Cargo index
python.enabled, python.executable, Python indexes, python.extras and python.groups
python.versions, python.overrides and python.constraints
Authorization settings, which are read from .npmrc



