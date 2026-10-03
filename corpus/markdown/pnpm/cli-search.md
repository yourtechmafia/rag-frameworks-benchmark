pnpm search
===========

Added in: v11.0.0

Aliases: `s`, `se`, `find`

Search the registry for packages matching the given keywords.

```
pnpm search <keyword> [<keyword> ...]
```

Examples[#](#examples)
----------------------

```
pnpm search webpack plugin
pnpm search @types/node
```

Options[#](#options)
--------------------

### --json[#](#--json)

Output search results in JSON format.

### --search-limit <number>[#](#--search-limit-number)

* Default: **20**

Maximum number of results to show.