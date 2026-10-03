




package.json | pnpm






































package.jsonThe manifest file of a package. It contains all the package's metadata,
including dependencies, title, author, et cetera. This is a standard preserved
across all major Node.js package managers, including pnpm.
In addition to the traditional package.json format, pnpm also supports package.json5 (via json5) and package.yaml (via js-yaml).
Note
Since v11, pnpm no longer reads settings from the pnpm field of package.json. Settings must be defined in pnpm-workspace.yaml instead. See Configuring.

engines#
You can specify the version of Node and pnpm that your software works on:
{
    "engines": {
        "node": ">=10",
        "pnpm": ">=3"
    }
}

During local development, pnpm will always fail with an error message
if its version does not match the one specified in the engines field.
Unless the user has set the engineStrict config flag (see settings), this
field is advisory only and will only produce warnings when your package is
installed as a dependency.
engines.runtime#
Added in: v10.21.0
Specifies the Node.js runtime required by a dependency. When declared, pnpm will automatically install the specified Node.js version.
{
  "engines": {
    "runtime": {
      "name": "node",
      "version": "^24.11.0",
      "onFail": "download"
    }
  }
}

When a package declares a runtime:

For CLI apps: pnpm binds the CLI to the required Node.js version, ensuring it uses the correct runtime regardless of the globally installed Node.js instance.
For packages with postinstall scripts: The script executes using the specified Node.js version.

This is particularly useful for dependencies that require specific Node.js versions to function correctly.
devEngines.runtime#
Added in: v10.14
Allows to specify one or more JavaScript runtime engines used by the project. Supported runtimes are Node.js, Deno, and Bun.
For instance, here is how to add node@^24.4.0 to your dependencies:
{
  "devEngines": {
    "runtime": {
      "name": "node",
      "version": "^24.4.0",
      "onFail": "download"
    }
  }
}

You can also add multiple runtimes to the same package.json:
{
  "devEngines": {
    "runtime": [
      {
        "name": "node",
        "version": "^24.4.0",
        "onFail": "download"
      },
      {
        "name": "deno",
        "version": "^2.4.3",
        "onFail": "download"
      }
    ]
  }
}

How it works:

pnpm install resolves your specified range to the latest matching runtime version.
The exact version (and checksum) is saved in the lockfile.
Scripts use the local runtime, ensuring consistency across environments.

To override the declared onFail behavior without editing the manifest, use the runtimeOnFail setting.
Since v12.0.0-rc.2, a bare node (or deno/bun) run from inside the project also follows this pin, not just scripts. This can be turned off with the globalShims setting, or skipped for a single command with PNPM_SHIM_BYPASS=1. See project-aware global bins.
devEngines.packageManager#
Added in: v11.0.0
Allows specifying the pnpm version via devEngines.packageManager in package.json. Unlike the packageManager field, this supports version ranges. The resolved version is stored in pnpm-lock.yaml under packageManagerDependencies and reused if it still satisfies the range.
When the lockfile records no version yet, pnpm records the running pnpm if it satisfies the range and was published at least minimumReleaseAge ago. Otherwise pnpm records the newest version in the range that is old enough. If no version in the range is old enough, pnpm records the running pnpm.
{
  "devEngines": {
    "packageManager": {
      "name": "pnpm",
      "version": ">=12.0.0 <13.0.0",
      "onFail": "download"
    }
  }
}

Note
When pnpm 12 is declared via the legacy packageManager field and pmOnFail is not set to ignore, its resolution info is written to pnpm-lock.yaml. The lockfile then gains a leading env lockfile document.

Since v12.0.0-rc.6, the field can also name another package manager — npm, yarn or bun — which is what pnpm add npm@11 writes. For those, nothing is recorded in pnpm-lock.yaml: packageManagerDependencies holds pnpm's own pin, and another package manager is pinned in an environment lockfile of its own under the pnpm home.
To override the onFail behavior without editing the manifest, see the pmOnFail setting.
dependenciesMeta#
Additional meta information used for dependencies declared inside dependencies, optionalDependencies, and devDependencies.
dependenciesMeta.*.injected#
If this is set to true for a dependency that is a local workspace package, that package will be installed by creating a hard linked copy in the virtual store (node_modules/.pnpm).
If this is set to false or not set, then the dependency will instead be installed by creating a node_modules symlink that points to the package's source directory in the workspace.  This is the default, as it is faster and ensures that any modifications to the dependency will be immediately visible to its consumers.
For example, suppose the following package.json is a local workspace package:
{
  "name": "card",
  "dependencies": {
    "button": "workspace:1.0.0"
  }
}

The button dependency will normally be installed by creating a symlink in the node_modules directory of card, pointing to the development directory for button.
But what if button specifies react in its peerDependencies? If all projects in the monorepo use the same version of react, then there is no problem. But what if button is required by card that uses react@16 and form that uses react@17? Normally you'd have to choose a single version of react and specify it using devDependencies of button. Symlinking does not provide a way for the react peer dependency to be satisfied differently by different consumers such as card and form.
The injected field solves this problem by installing a hard linked copies of button in the virtual store. To accomplish this, the package.json of card could be configured as follows:
{
  "name": "card",
  "dependencies": {
    "button": "workspace:1.0.0",
    "react": "16"
  },
  "dependenciesMeta": {
    "button": {
      "injected": true
    }
  }
}

Whereas the package.json of form could be configured as follows:
{
  "name": "form",
  "dependencies": {
    "button": "workspace:1.0.0",
    "react": "17"
  },
  "dependenciesMeta": {
    "button": {
      "injected": true
    }
  }
}

With these changes, we say that button is an "injected dependency" of card and form.  When button imports react, it will resolve to react@16 in the context of card, but resolve to react@17 in the context of form.
Because injected dependencies produce copies of their workspace source directory, these copies must be updated somehow whenever the code is modified; otherwise, the new state will not be reflected for consumers. When building multiple projects with a command such as pnpm --recursive run build, this update must occur after each injected package is rebuilt but before its consumers are rebuilt. For simple use cases, it can be accomplished by invoking pnpm install again, perhaps using a package.json lifecycle script such as "prepare": "pnpm run build" to rebuild that one project.  Third party tools such as pnpm-sync and pnpm-sync-dependencies-meta-injected provide a more robust and efficient solution for updating injected dependencies, as well as watch mode support.
peerDependencies#
Peer dependency values are normally semver ranges (^1.0.0), or a workspace: or catalog: specifier.
Since v11.14.0, a peer dependency may also be declared with a specifier that carries a scheme:
{
  "peerDependencies": {
    "lib-a": "work:5.x.x",
    "lib-b": "npm:other-lib@^5",
    "lib-c": "file:../lib-c",
    "lib-d": "git+https://example.com/lib-d.git"
  }
}

Accepted forms are a named-registry spec (<registry>:<version>), an npm: alias, and a file:, git, or URL spec.
Such a specifier is matched against the semver range it carries — work:5.x.x is checked as 5.x.x and npm:other-lib@^5 as ^5. A specifier that carries no version, such as file:../lib-c, is matched against *, so any version satisfies it. Meanwhile the original specifier is what selects the package when autoInstallPeers installs a missing peer, so the peer is fetched from the aliased name, registry, or source you named.
Bare name@version values are still rejected with ERR_PNPM_INVALID_PEER_DEPENDENCY_SPECIFICATION, as they are almost always a mistake:
{
  "peerDependencies": {
    "lib-a": "lib-a@1.2.3"
  }
}

peerDependenciesMeta#
This field lists some extra information related to the dependencies listed in
the peerDependencies field.
peerDependenciesMeta.*.optional#
If this is set to true, the selected peer dependency will be marked as optional
by the package manager. Therefore, the consumer omitting it will no longer be
reported as an error.
For example:
{
    "peerDependencies": {
        "foo": "1"
    },
    "peerDependenciesMeta": {
        "foo": {
            "optional": true
        },
        "bar": {
            "optional": true
        }
    }
}

Note that even though bar was not specified in peerDependencies, it is
marked as optional. pnpm will therefore assume that any version of bar is fine.
However, foo is optional, but only to the required version specification.
publishConfig#
This field carries settings that change how a package is published:
registry, access,
directory,
linkDirectory, and
executableFiles. These are preserved in the
published package.json.
Additionally, publishConfig can be used to override several other fields in the
manifest before the package is packed. The following fields may be overridden:

bin
main
exports
types or typings
module
browser
esnext
es2015
unpkg
umd:main
typesVersions
cpu
os
engines (Added in v10.22.0)
name (Added in v11.18.0)

To override a field, add the publish version of the field to publishConfig.
For instance, the following package.json:
{
    "name": "foo",
    "version": "1.0.0",
    "main": "src/index.ts",
    "publishConfig": {
        "main": "lib/index.js",
        "typings": "lib/index.d.ts"
    }
}

Will be published as:
{
    "name": "foo",
    "version": "1.0.0",
    "main": "lib/index.js",
    "typings": "lib/index.d.ts"
}

publishConfig.registry#
Added in: v8.6.8
The registry this package publishes to. It overrides the registry setting, any
scope route in registries,
and pnpm publish --registry.
{
  "name": "foo",
  "version": "1.0.0",
  "publishConfig": {
    "registry": "https://registry.npmjs.org/"
  }
}

Only the URL belongs here. pnpm matches it against the auth settings in
.npmrc, so the example above publishes with
//registry.npmjs.org/:_authToken=....
Each package in a pnpm publish -r run goes to its own target registry, so one
command can release a workspace to several registries.
--batch then sends one request per registry.
Since v12.7.0, a scoped package can also set its registry under the
@<scope>:registry key. For a package in that scope, it takes precedence over
publishConfig.registry and over the registry set for the scope in .npmrc:
{
  "name": "@acme/foo",
  "version": "1.0.0",
  "publishConfig": {
    "@acme:registry": "https://npm.acme.example/"
  }
}

publishConfig.access#
Added in: v11.2.0
Tells the registry whether the published package should be public or
restricted. Same as
pnpm publish --access.
Left unset, pnpm sends no access level, so the registry applies its own default
and the level of an already published package is left alone. Unscoped packages
cannot be restricted.
{
  "name": "@acme/foo",
  "version": "1.0.0",
  "publishConfig": {
    "access": "public"
  }
}

publishConfig.name#
Added in: v11.18.0
Publishes the package under a different name than the one its manifest carries in the workspace. This is for a project whose published name is already taken by a sibling project, which otherwise has to be renamed by a build step just before publishing.
{
  "name": "foo-v2",
  "version": "2.0.0",
  "publishConfig": {
    "name": "foo"
  }
}

Only the published artifact is renamed — dependents, pnpm-lock.yaml, and release tooling keep addressing the project by its manifest name. The new name reaches the packed manifest, the tarball filename, and everything that addresses the package at the registry: the already-published check of pnpm publish -r, its registry selection, and the release-planning probes of pnpm change status and pnpm version -r.
publishConfig.executableFiles#
By default, for portability reasons, no files except those listed in the bin field will be marked as executable in the resulting package archive. The executableFiles field lets you declare additional files that must have the executable flag (+x) set even if they aren't directly accessible through the bin field.
{
  "publishConfig": {
    "executableFiles": [
      "./dist/shim.js"
    ]
  }
}

publishConfig.directory#
You also can use the field publishConfig.directory to customize the published subdirectory relative to the current package.json.
It is expected to have a modified version of the current package in the specified directory (usually using third party build tools).

In this example the "dist" folder must contain a package.json

{
  "name": "foo",
  "version": "1.0.0",
  "publishConfig": {
    "directory": "dist"
  }
}

publishConfig.linkDirectory#

Default: true
Type: Boolean

When set to true, the project will be symlinked from the publishConfig.directory location during local development.
For example:
{
  "name": "foo",
  "version": "1.0.0",
  "publishConfig": {
    "directory": "dist",
    "linkDirectory": true
  }
}



