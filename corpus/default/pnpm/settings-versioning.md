




Versioning Settings | pnpm






































Versioning SettingsAdded in: v11.13.0
These settings configure pnpm's native workspace release management, driven by pnpm change and the bare pnpm version -r. See Release management for the workflow they belong to.
Where two workspace projects publish the same name, a project may be referenced by its ./-prefixed workspace-relative directory instead of its name in versioning.fixed, versioning.ignore, and the keys of versioning.lanes.
versioning.fixed#

Default: []
Type: string[][]

Groups of packages that always release together at one shared version. The shared version is the highest current version in the group, bumped by the largest bump any member needs.
pnpm-workspace.yamlversioning:
  fixed:
    - ['@example/cli', '@example/napi']

A fixed group must move between lanes together, and must sit entirely inside or entirely outside an epic.
versioning.ignore#

Default: []
Type: string[]

Packages permanently excluded from versioning and dependent propagation. A change intent that requests a real bump for an ignored package fails.
pnpm-workspace.yamlversioning:
  ignore:
    - '@example/internal'

versioning.maxBump#

Default: undefined (no cap)
Type: 'patch', 'minor', 'major'

Caps the bump a release from the current checkout may apply. It is enforced on the final assembled release plan, after dependent propagation and fixed-group resolution, so a patch-only maintenance branch cannot accidentally ship a minor.
pnpm-workspace.yamlversioning:
  maxBump: patch

versioning.lanes#

Default: {}
Type: Record<string, string>

Maps a package to the release lane it is on. A lane is a parallel release track that emits X.Y.Z-<lane>.N prereleases; every unlisted package is on the reserved default lane, main, and releases stable versions.
pnpm-workspace.yamlversioning:
  lanes:
    '@example/cli': alpha

Lane names may contain only alphanumerics and hyphens, and cannot be purely numeric. main is reserved and cannot be assigned — remove the entry instead, or use pnpm lane main --filter <pkg>.
versioning.epics#

Default: []
Type: Array<{ lead: string, packages: string[] }>

Ties a group of member packages to a lead package, constraining every member's major version to a band derived from the lead's major: while the lead is on major M, members live in M*100 … M*100+99.
pnpm-workspace.yamlversioning:
  epics:
    - lead: '@example/app'
      packages:
        - './packages/**'
        - '!./packages/private-*'

lead is a package name or a ./-prefixed workspace directory. packages is matched with pnpm's package selectors — name globs, ./-prefixed directory globs, and !-prefixed negations — evaluated in order, last match wins. A package can belong to at most one epic.
See Epics for how the band is enforced and re-based.
versioning.changelog.storage#

Default: 'registry'
Type: 'registry', 'repository'

Where release changelogs live.
With registry, no CHANGELOG.md is committed: each release's section is composed at publish time and packed into the published tarball on top of the previously published version's changelog.
With repository, a CHANGELOG.md is committed in every package.
Private packages always use repository storage, as they are never published.
pnpm-workspace.yamlversioning:
  changelog:
    storage: repository



