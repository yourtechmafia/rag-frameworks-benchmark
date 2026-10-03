Package managers

Install Speed
-------------

Two projects installed six ways each — the cache and lockfile states you actually end up in, from a fresh clone to a warm re-run.

Tools

npmv12.2.0pnpm 11v11.28.2pnpm 12v12.8.2pnpm 12 + pnprv12.8.2pnpm 12 + global storev12.8.2pnpm 12 hoistedv12.8.2

Projects

alotta-filesalotta-packages

Consistent scaleFit each scenario

Group by toolRank slowest first

Every bar shares one scale, so scenarios are comparable with each other. Tools stay in the same order in every scenario.

### alotta-files

A wide dependency graph of small packages — lots of files to link, little to resolve.

6/6scenarios where pnpm beats npm

51xfaster than npm on “everything warm”

16mspnpm's best run — “everything warm”

cleanA fresh clone. Nothing cached.

npm

44.3s13x slower

pnpm 11

7.34s2.2x slower

pnpm 12

4.34s1.3x slower

pnpm 12 + pnpr

3.37s

pnpm 12 + global store

4.74s1.4x slower

pnpm 12 hoisted

4.53s1.3x slower

015s30s

lockfileCI, first install.

npm

10.6s3.3x slower

pnpm 11

4.45s1.4x slower

pnpm 12

3.19s

pnpm 12 + pnpr

3.35s

pnpm 12 + global store

3.41s1.1x slower

pnpm 12 hoisted

3.45s1.1x slower

015s30s

cacheReinstalling without a lockfile.

npm

7.95s16x slower

pnpm 11

3.44s6.7x slower

pnpm 12

974ms1.9x slower

pnpm 12 + pnpr

814ms1.6x slower

pnpm 12 + global store

511ms

pnpm 12 hoisted

889ms1.7x slower

015s30s

cache + lockfileReinstalling a project you already have.

npm

5.07s25x slower

pnpm 11

1.83s9.0x slower

pnpm 12

831ms4.1x slower

pnpm 12 + pnpr

817ms4.0x slower

pnpm 12 + global store

203ms

pnpm 12 hoisted

594ms2.9x slower

015s30s

everything warmRunning install when nothing changed.

npm

812ms51x slower

pnpm 11

412ms26x slower

pnpm 12

16ms

pnpm 12 + pnpr

16ms

pnpm 12 + global store

17ms1.1x slower

pnpm 12 hoisted

16ms

015s30s

updateA dependency was bumped in package.json.

npm

3.44s3.9x slower

pnpm 11

2.99s3.4x slower

pnpm 12

882ms

pnpm 12 + pnpr

950ms1.1x slower

pnpm 12 + global store

930ms1.1x slower

pnpm 12 hoisted

1.20s1.4x slower

015s30s

#### Total across all scenarios

1. pnpm 12 + pnpr9.31sfastest
2. pnpm 12 + global store9.82s1.1x slower
3. pnpm 1210.2s1.1x slower
4. pnpm 12 hoisted10.7s1.1x slower
5. pnpm 1120.5s2.2x slower
6. npm1m 12s7.8x slower

All 6 scenarios added up.

#### Exact numbers

Install Speed on alotta-files — fastest run per scenario.

| Scenario | npmv12.2.0 | pnpm 11v11.28.2 | pnpm 12v12.8.2 | pnpm 12 + pnprv12.8.2 | pnpm 12 + global storev12.8.2 | pnpm 12 hoistedv12.8.2 |
| --- | --- | --- | --- | --- | --- | --- |
| cleanA fresh clone. Nothing cached. | 44.3s | 7.34s | 4.34s | 3.37s | 4.74s | 4.53s |
| lockfileCI, first install. | 10.6s | 4.45s | 3.19s | 3.35s | 3.41s | 3.45s |
| cacheReinstalling without a lockfile. | 7.95s | 3.44s | 974ms | 814ms | 511ms | 889ms |
| cache + lockfileReinstalling a project you already have. | 5.07s | 1.83s | 831ms | 817ms | 203ms | 594ms |
| everything warmRunning install when nothing changed. | 812ms | 412ms | 16ms | 16ms | 17ms | 16ms |
| updateA dependency was bumped in package.json. | 3.44s | 2.99s | 882ms | 950ms | 930ms | 1.20s |

Measured with npm 12.2.0 · pnpm 11 11.28.2 · pnpm 12 12.8.2 · pnpm 12 + pnpr 12.8.2 · pnpm 12 + global store 12.8.2 · pnpm 12 hoisted 12.8.2.

### alotta-packages

Fourteen modern toolchains — Angular, Nest, Vite, webpack, Storybook — resolving to about a gigabyte.

6/6scenarios where pnpm beats npm

125xfaster than npm on “everything warm”

19mspnpm's best run — “everything warm”

cleanA fresh clone. Nothing cached.

npm

1m 39s11x slower

pnpm 11

21.5s2.4x slower

pnpm 12

13.5s1.5x slower

pnpm 12 + pnpr

9.09s

pnpm 12 + global store

15.1s1.7x slower

pnpm 12 hoisted

14.6s1.6x slower

030s1m1m30s

lockfileCI, first install.

npm

28.9s3.3x slower

pnpm 11

11.6s1.3x slower

pnpm 12

8.79s

pnpm 12 + pnpr

8.88s

pnpm 12 + global store

9.03s

pnpm 12 hoisted

10.2s1.2x slower

030s1m1m30s

cacheReinstalling without a lockfile.

npm

27.8s17x slower

pnpm 11

13.5s8.4x slower

pnpm 12

2.98s1.9x slower

pnpm 12 + pnpr

2.51s1.6x slower

pnpm 12 + global store

1.60s

pnpm 12 hoisted

3.03s1.9x slower

030s1m1m30s

cache + lockfileReinstalling a project you already have.

npm

15.4s27x slower

pnpm 11

5.54s9.6x slower

pnpm 12

2.39s4.1x slower

pnpm 12 + pnpr

2.49s4.3x slower

pnpm 12 + global store

576ms

pnpm 12 hoisted

2.06s3.6x slower

030s1m1m30s

everything warmRunning install when nothing changed.

npm

2.37s132x slower

pnpm 11

384ms21x slower

pnpm 12

19ms1.1x slower

pnpm 12 + pnpr

19ms1.1x slower

pnpm 12 + global store

18ms

pnpm 12 hoisted

19ms1.1x slower

030s1m1m30s

updateA dependency was bumped in package.json.

npm

13.1s7.4x slower

pnpm 11

10.4s5.8x slower

pnpm 12

2.65s1.5x slower

pnpm 12 + pnpr

1.78s

pnpm 12 + global store

2.53s1.4x slower

pnpm 12 hoisted

3.65s2.0x slower

030s1m1m30s

#### Total across all scenarios

1. pnpm 12 + pnpr24.8sfastest
2. pnpm 12 + global store28.9s1.2x slower
3. pnpm 1230.3s1.2x slower
4. pnpm 12 hoisted33.6s1.4x slower
5. pnpm 111m 3s2.5x slower
6. npm3m 7s7.5x slower

All 6 scenarios added up.

#### Exact numbers

Install Speed on alotta-packages — fastest run per scenario.

| Scenario | npmv12.2.0 | pnpm 11v11.28.2 | pnpm 12v12.8.2 | pnpm 12 + pnprv12.8.2 | pnpm 12 + global storev12.8.2 | pnpm 12 hoistedv12.8.2 |
| --- | --- | --- | --- | --- | --- | --- |
| cleanA fresh clone. Nothing cached. | 1m 39s | 21.5s | 13.5s | 9.09s | 15.1s | 14.6s |
| lockfileCI, first install. | 28.9s | 11.6s | 8.79s | 8.88s | 9.03s | 10.2s |
| cacheReinstalling without a lockfile. | 27.8s | 13.5s | 2.98s | 2.51s | 1.60s | 3.03s |
| cache + lockfileReinstalling a project you already have. | 15.4s | 5.54s | 2.39s | 2.49s | 576ms | 2.06s |
| everything warmRunning install when nothing changed. | 2.37s | 384ms | 19ms | 19ms | 18ms | 19ms |
| updateA dependency was bumped in package.json. | 13.1s | 10.4s | 2.65s | 1.78s | 2.53s | 3.65s |

Measured with npm 12.2.0 · pnpm 11 11.28.2 · pnpm 12 12.8.2 · pnpm 12 + pnpr 12.8.2 · pnpm 12 + global store 12.8.2 · pnpm 12 hoisted 12.8.2.

* Two projects, run separately: "alotta-files" is a wide graph of small packages, "alotta-packages" is fourteen modern toolchains resolving to about a gigabyte. Both are shown because they do not agree — pnpm leads on each, but by different margins, and pnpr gains far more on the larger graph.
* Within a project the only thing that changes is the package manager, and every manager is measured with the same versions on both projects. Numbers are never combined across projects.
* Each number is the fastest of the three most recent runs.
* Everything installs through the same registry over the same emulated link (50ms, 200Mbps), so the times include the round trips a real install pays for.
* Six scenarios here. The suite measures three more that delete your cache or lockfile but keep node\_modules — nobody works that way, so they are left out.
* pnpm 12 + pnpr is the same version and the same command, with resolution handled by the registry instead of locally.
* The three columns after pnpm 12 are that same pnpm 12 configured differently — a global virtual store, a hoisted node\_modules, and registry-side resolution. They are shown to make the cost of each setting visible, and are left out of the headline numbers above, which describe pnpm as it installs by default.

Node.js version managers

Node.js Version Management
--------------------------

pnpm installs and switches Node.js versions itself, so you may not need a version manager at all. Here it is against fnm and nvm.

pnpmv12.8.2fnmv1.39.0nvmv0.40.8

Consistent scaleFit each scenario

Group by toolRank slowest first

Every bar shares one scale, so scenarios are comparable with each other. Tools stay in the same order in every scenario.

3/3scenarios where pnpm is fastest

15xfaster than nvm on “install (warm store)”

5mspnpm's best run — “run in project”

install (clean)Install Node.js 24, nothing cached.

pnpm

1.03s

fnm

2.98s2.9x slower

nvm

2.75s2.7x slower

01s2s

install (warm store)Install a version you had before.

pnpm

158ms

fnm

2.95s19x slower

nvm

2.38s15x slower

01s2s

run in projectRun node in a project pinned to Node.js 22.

pnpm

5ms

fnm

5ms

nvm

75ms16x slower

01s2s

#### Total across all scenarios

1. pnpm1.19sfastest
2. nvm5.21s4.4x slower
3. fnm5.94s5.0x slower

All 3 scenarios added up.

#### Exact numbers

Node.js Version Management — fastest run per scenario.

| Scenario | pnpmv12.8.2 | fnmv1.39.0 | nvmv0.40.8 |
| --- | --- | --- | --- |
| install (clean)Install Node.js 24, nothing cached. | 1.03s | 2.98s | 2.75s |
| install (warm store)Install a version you had before. | 158ms | 2.95s | 2.38s |
| run in projectRun node in a project pinned to Node.js 22. | 5ms | 5ms | 75ms |

Measured with pnpm 12.8.2 · fnm 1.39.0 · nvm 0.40.8.

* pnpm keeps Node.js in its store, so a version it has seen before needs no download.
* There is no switch command — the node on your PATH is whatever the project asks for.
* Timed inside a shell with $EPOCHREALTIME, because nvm is a shell function rather than a binary.

How these numbers are produced
------------------------------

Every tool runs on the same machine against the same project, and the timings are committed to [pnpm/benchmarks](https://github.com/pnpm/benchmarks). This page reads them at build time and picks the newest version of each tool.

This is one project on one machine — your numbers will differ. Run `pnpm run benchmark` to see your own.
