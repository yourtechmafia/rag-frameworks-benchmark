pnpm CLI
========

Short aliases[#](#short-aliases)
--------------------------------

Added in: v11.0.0

`pn` is available as a short alias for `pnpm`, and [`pnx`](/cli/pnx) as a short alias for `pnpm dlx`. You can use them anywhere you'd use `pnpm` or `pnpx`:

```
pn install
pn add express
pn build
pn test
pnx create-vue my-app
```

Differences vs npm[#](#differences-vs-npm)
------------------------------------------

Unlike npm, pnpm validates all options. For example, `pnpm install --target_arch x64` will
fail as `--target_arch` is not a valid option for `pnpm install`.

However, some dependencies may use the `npm_config_` environment variable, which
is populated from the CLI options. In this case, you have the following options:

1. explicitly set the env variable: `npm_config_target_arch=x64 pnpm install`
2. force the unknown option with `--config.`: `pnpm install --config.target_arch=x64`

Boolean flags[#](#boolean-flags)
--------------------------------

A boolean flag can be written on its own, negated with a `no-` prefix, or given an explicit value:

```
pnpm install --prod            # devDependencies are skipped
pnpm install --no-prod         # devDependencies are installed
pnpm install --prod=false      # the same, since v12.4.0
pnpm install --prod=true       # the same as --prod
```

The `--config.` escape hatch takes a value the same way: `--config.trust-lockfile=false`.

Options[#](#options)
--------------------

### -C <path>, --dir <path>[#](#-c-path---dir-path)

Run as if pnpm was started in `<path>` instead of the current working directory.

### Which project a command acts on[#](#which-project-a-command-acts-on)

Run from a subdirectory of a project, a command acts on the nearest ancestor
directory that has a manifest, so `pnpm bin` from `packages/app/src` reports
paths under `packages/app`. Two commands stay where you are: `pnpm init`
creates its manifest in the current directory, and `pnpm exec` runs the command
there.

### -w, --workspace-root[#](#-w---workspace-root)

Run as if pnpm was started in the root of the [workspace](/workspaces)
instead of the current working directory.

### --ignore-workspace[#](#--ignore-workspace)

Added in: v6.25.0

Run as if the current project were standalone. pnpm does not discover a
`pnpm-workspace.yaml` in a parent directory, so the workspace's settings and
other projects do not apply to the command.

For example, this installs only the project in the current directory, even if
it is located inside a workspace:

```
pnpm install --ignore-workspace
```

Commands[#](#commands)
----------------------

For more information, see the documentation for individual CLI commands. Here is
a list of handy npm equivalents to get you started:

| npm command | pnpm equivalent |
| --- | --- |
| `npm install` | [`pnpm install`](/cli/install) |
| `npm i <pkg>` | [`pnpm add <pkg>`](/cli/add) |
| `npm run <cmd>` | [`pnpm <cmd>`](/cli/run) |
| `npx <pkg>` | [`pnx <pkg>`](/cli/pnx) |

When an unknown command is used, pnpm will search for a script with the given name,
so `pnpm run lint` is the same as `pnpm lint`. If there is no script with the specified name,
then pnpm will execute the command as a shell script, so you can do things like `pnpm eslint` (see [`pnpm exec`](/cli/exec)).

Environment variables[#](#environment-variables)
------------------------------------------------

Some environment variables that are not pnpm related might change the behaviour of pnpm:

* [`CI`](/cli/install#--frozen-lockfile)

These environment variables may influence what directories pnpm will use for storing global information:

* `XDG_CACHE_HOME`
* `XDG_CONFIG_HOME`
* `XDG_DATA_HOME`
* `XDG_STATE_HOME`

You can search the docs to find the settings that leverage these environment variables.