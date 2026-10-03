




Catalogs | pnpm






































Catalogs"Catalogs" are a workspace feature for defining dependency version ranges as reusable constants. Constants defined in catalogs can later be referenced in package.json files.

The Catalog Protocol (catalog:)#
Once a catalog is defined in pnpm-workspace.yaml,
pnpm-workspace.yamlpackages:
  - packages/*

# Define a catalog of version ranges.
catalog:
  react: ^18.3.1
  redux: ^5.0.1

The catalog: protocol can be used instead of the version range itself.
packages/example-app/package.json{
  "name": "@example/app",
  "dependencies": {
    "react": "catalog:",
    "redux": "catalog:"
  }
}

This is equivalent to writing a version range (e.g. ^18.3.1) directly.
packages/example-app/package.json{
  "name": "@example/app",
  "dependencies": {
    "react": "^18.3.1",
    "redux": "^5.0.1"
  }
}

You may use the catalog: protocol in the next fields:

package.json:

dependencies
devDependencies
peerDependencies
optionalDependencies


pnpm-workspace.yaml

overrides



The catalog: protocol allows an optional name after the colon (ex: catalog:name) to specify which catalog should be used. When a name is omitted, the default catalog is used.
Depending on the scenario, the catalog: protocol offers a few advantages compared to writing version ranges directly that are detailed next.
Advantages#
In a workspace (i.e. monorepo or multi-package repo) it's common for the same dependency to be used by many packages. Catalogs reduce duplication when authoring package.json files and provide a few benefits in doing so:

Maintain unique versions — It's usually desirable to have only one version of a dependency in a workspace. Catalogs make this easier to maintain. Duplicated dependencies can conflict at runtime and cause bugs. Duplicates also increase size when using a bundler.
Easier upgrades — When upgrading a dependency, only the catalog entry in pnpm-workspace.yaml needs to be edited rather than all package.json files using that dependency. This saves time — only one line needs to be changed instead of many.
Fewer merge conflicts — Since package.json files do not need to be edited when upgrading a dependency, git merge conflicts no longer happen in these files.

Defining Catalogs#
Catalogs are defined in the pnpm-workspace.yaml file. There are two ways to define catalogs.

Using the (singular) catalog field to create a catalog named default.
Using the (plural) catalogs field to create arbitrarily named catalogs.

Tip
If you have an existing workspace that you want to migrate to using catalogs, you can use the following codemod:
pnpx codemod pnpm/catalog


Default Catalog#
The top-level catalog field allows users to define a catalog named default.
pnpm-workspace.yamlcatalog:
  react: ^18.2.0
  react-dom: ^18.2.0

These version ranges can be referenced through catalog:default. For the default catalog only, a special catalog: shorthand can also be used. Think of catalog: as a shorthand that expands to catalog:default.
Named Catalogs#
Multiple catalogs with arbitrarily chosen names can be configured under the catalogs key.
pnpm-workspace.yamlcatalogs:
  # Can be referenced through "catalog:react17"
  react17:
    react: ^17.0.2
    react-dom: ^17.0.2

  # Can be referenced through "catalog:react18"
  react18:
    react: ^18.2.0
    react-dom: ^18.2.0

A default catalog can be defined alongside multiple named catalogs. This might be useful in a large multi-package repo that's migrating to a newer version of a dependency piecemeal.
pnpm-workspace.yamlcatalog:
  react: ^16.14.0
  react-dom: ^16.14.0

catalogs:
  # Can be referenced through "catalog:react17"
  react17:
    react: ^17.0.2
    react-dom: ^17.0.2

  # Can be referenced through "catalog:react18"
  react18:
    react: ^18.2.0
    react-dom: ^18.2.0

Workspace dependencies in a catalog#
Added in: v12.2.0
A catalog entry may hold a workspace: range, so the version a workspace dependency is linked by is written once too:
pnpm-workspace.yamlcatalog:
  '@example/utils': workspace:^

packages/example-app/package.json{
  "name": "@example/app",
  "dependencies": {
    "@example/utils": "catalog:"
  }
}

pnpm expands the catalog: reference to workspace:^ and then links the workspace project, exactly as if the package.json had declared workspace:^ itself. On publish both protocols are replaced, so the example above ships as "^1.4.0" when @example/utils is at 1.4.0.
Local dependencies in a catalog#
Added in: v12.6.0
Catalog entries can use the file: and link: protocols (#8642). A relative path or bare path in an entry is measured from the directory holding pnpm-workspace.yaml:
pnpm-workspace.yamlcatalog:
  my-lib: link:./packages/my-lib
  my-tarball: file:./tarballs/foo.tgz

packages/example-app/package.json{
  "name": "@example/app",
  "dependencies": {
    "my-lib": "catalog:",
    "my-tarball": "catalog:"
  }
}

Publishing#
The catalog: protocol is removed when running pnpm publish or pnpm pack. This is similar to the workspace: protocol, which is also replaced on publish.
For example,
packages/example-components/package.json{
  "name": "@example/components",
  "dependencies": {
    "react": "catalog:react18",
  }
}

Will become the following on publish.
packages/example-components/package.json{
  "name": "@example/components",
  "dependencies": {
    "react": "^18.3.1",
  }
}

The catalog: protocol replacement process allows the @example/components package to be used by other workspaces or package managers.
Settings#
catalogMode#
Added in: v10.12.1

Default: manual
Type: manual, strict, prefer

Controls if and how dependencies are added to the default catalog, when running pnpm add. There are three modes:

strict - only allows dependency versions from the catalog. Adding a dependency outside the catalog's version range will cause an error.
prefer - prefers catalog versions, but will fall back to direct dependencies if no compatible version is found.
manual (default) - does not automatically add dependencies to the catalog.

Since v12.3.0, a specifier that names a location rather than a version is never moved into a catalog: local paths, local tarballs, tarball URLs, and workspace:<path> ranges stay in the package.json that declares them. Such a specifier is resolved relative to its own project, so one catalog entry could not mean the same directory for every project referencing it.

catalogPrune#
Added in: v11.22.0 (as cleanupUnusedCatalogs since v10.15.0)

Default: false
Type: Boolean

When set to true, pnpm will remove unused catalog entries during installation.
cleanupUnusedCatalogs is the deprecated spelling of this setting and continues to work; when both are set, catalogPrune wins.


