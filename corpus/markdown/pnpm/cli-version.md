pnpm version
============

Added in: v11.0.0

Bump the package version.

```
pnpm version <newversion>
pnpm version <major|minor|patch|premajor|preminor|prepatch|prerelease|from-git>
pnpm version -r [--dry-run]
```

`<newversion>` can be any of the bump types above or an explicit semver version (e.g. `1.2.3`). Workspaces and the `workspace:` protocol are supported, so cross-references between workspace packages are updated correctly.

When run inside a git repository, `pnpm version` creates a git commit and an annotated tag for the bump. The working tree must be clean (see `--no-git-checks` below) and commits/tags can be disabled with `--no-git-tag-version`. Git commits and tags are always skipped in recursive mode because multiple packages may be bumped to different versions in a single run.

Usage[#](#usage)
----------------

```
pnpm version patch
pnpm version minor
pnpm version major
pnpm version 2.0.0
pnpm version prerelease --preid beta
```

Recursive releases[#](#recursive-releases)
------------------------------------------

Added in: v11.13.0

Run with `-r` and **no version argument** to consume the pending change intents recorded by [`pnpm change`](/cli/change):

```
pnpm version -r
```

This assembles a release plan from the `.changeset/*.md` intent files and applies it: every package named by an intent is bumped, and so is every package that depends on it through a `workspace:` range. It then writes changelogs and records the consumed intents in `.changeset/ledger.yaml`.

Private packages (`"private": true`) are bumped without checking the registry for their [first release](/versioning#first-releases), and their changelog is always written to the committed `CHANGELOG.md`, even when [`versioning.changelog.storage`](/settings/versioning#versioningchangelogstorage) is `registry`.

Preview the plan without touching anything:

```
pnpm version -r --dry-run
```

Narrow it to part of the workspace with `--filter`. The selection is expanded until it settles, so fixed-group companions and dependents whose ranges the bump invalidates are pulled in automatically.

The working tree must be clean unless `--dry-run` or `--no-git-checks` is passed. See [Release management](/versioning) for the full workflow.

Options[#](#options)
--------------------

### --preid <prerelease-id>[#](#--preid-prerelease-id)

The "prerelease identifier" to use as a prefix for the prerelease part of a semver.

```
pnpm version prerelease --preid beta
```

### --message, -m <message>[#](#--message--m-message)

Commit message. Any `%s` in the message is replaced with the new version. Defaults to `%s`.

```
pnpm version patch --message "chore: release v%s"
```

### --tag-version-prefix <prefix>[#](#--tag-version-prefix-prefix)

Prefix used when creating the git tag. Defaults to `v` (e.g. `v1.2.3`). Set to an empty string to drop the prefix entirely.

### --no-git-tag-version[#](#--no-git-tag-version)

Do not create a git commit or tag for the version change.

### --no-commit-hooks[#](#--no-commit-hooks)

Skip git commit hooks (`--no-verify`) when committing the version bump.

### --sign-git-tag[#](#--sign-git-tag)

Sign the generated git tag with GPG (`git tag -s`).

### --no-git-checks[#](#--no-git-checks)

Do not check whether the working tree is clean before bumping the version.

### --allow-same-version[#](#--allow-same-version)

Allow setting the version to the current version. This can be useful for CI pipelines.

### --recursive, -r[#](#--recursive--r)

Apply the version bump to every package in the workspace (optionally narrowed with `--filter`). Git commit and tag creation are skipped in recursive mode.

### --json[#](#--json)

Output the list of bumped packages in JSON format.