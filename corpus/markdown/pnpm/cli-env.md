pnpm env <cmd>
==============

Deprecated

`pnpm env` is deprecated. Use [`pnpm runtime`](/cli/runtime) instead. For example, `pnpm env use --global lts` becomes `pnpm runtime set node lts -g`.

Manages the Node.js environment.

Commands[#](#commands)
----------------------

### use[#](#use)

Install and use the specified version of Node.js

Install the LTS version of Node.js:

```
pnpm env use --global lts
```

Install Node.js v16:

```
pnpm env use --global 16
```

Install a prerelease version of Node.js:

```
pnpm env use --global nightly
pnpm env use --global rc
pnpm env use --global 16.0.0-rc.0
pnpm env use --global rc/14
```

Install the latest version of Node.js:

```
pnpm env use --global latest
```

Install an LTS version of Node.js using its [codename](https://github.com/nodejs/Release/blob/main/CODENAMES.md):

```
pnpm env use --global argon
```

### add[#](#add)

Installs the specified version(s) of Node.js without activating them as the current version.

Example:

```
pnpm env add --global lts 18 20.0.1
```

### remove, rm[#](#remove-rm)

Removes the specified version(s) of Node.js.

Usage example:

```
pnpm env remove --global 14.0.0
pnpm env remove --global 14.0.0 16.2.3
```

### list, ls[#](#list-ls)

List Node.js versions available locally or remotely.

Print locally installed versions:

```
pnpm env list
```

Print remotely available Node.js versions:

```
pnpm env list --remote
```

Print remotely available Node.js v16 versions:

```
pnpm env list --remote 16
```

Options[#](#options)
--------------------

### --global, -g[#](#--global--g)

The changes are made systemwide.