[NewWhat’s different in pnpm 12→](/blog/whats-different-in-pnpm-12)

Save time. Save disk space. Supercharge your monorepos.
=======================================================

Get lightning-fast installation speeds and a smarter, safer way to manage dependencies.

$`curl -fsSL https://get.pnpm.io/install.sh | sh -`

[Getting started→](/installation)

[Star](https://github.com/pnpm/pnpm)[33,400](https://github.com/pnpm/pnpm/stargazers)

Watch the intro

~/my-monorepo

❯

⚡**0 bytes** downloadedevery package reused from the store

✓**1 copy** on diskshared by every project

OSS projects that use pnpm

* next.js
* n8n
* ![](/img/users/mui.svg)Material UI
* ![](/img/users/vitejs.svg)Vite
* ![](/img/users/nuxt_min.svg)Nuxt
* ![](/img/users/vue.svg)Vue
* Astro
* Prisma
* Novu
* ![](/img/users/slidev_min.svg)Slidev
* ![](/img/users/turborepo_min.svg)Turborepo
* ![](/img/users/quasar_min.svg)Quasar Framework
* ![](/img/users/element-plus_min.svg)Element Plus
* ![](/img/users/next-auth_min.svg)NextAuth.js
* ![](/img/users/emberjs.svg)Ember.js
* ![](/img/users/qwik_min.svg)Qwik
* ![](/img/users/vue-use_min.svg)VueUse
* ![](/img/users/sveltekit_min.svg)SvelteKit
* ![](/img/users/verdaccio_min.svg)Verdaccio
* Vercel
* ![](/img/users/nx.svg)Nx
* ![](/img/users/angular.svg)Angular

* next.js
* n8n
* ![](/img/users/mui.svg)Material UI
* ![](/img/users/vitejs.svg)Vite
* ![](/img/users/nuxt_min.svg)Nuxt
* ![](/img/users/vue.svg)Vue
* Astro
* Prisma
* Novu
* ![](/img/users/slidev_min.svg)Slidev
* ![](/img/users/turborepo_min.svg)Turborepo
* ![](/img/users/quasar_min.svg)Quasar Framework
* ![](/img/users/element-plus_min.svg)Element Plus
* ![](/img/users/next-auth_min.svg)NextAuth.js
* ![](/img/users/emberjs.svg)Ember.js
* ![](/img/users/qwik_min.svg)Qwik
* ![](/img/users/vue-use_min.svg)VueUse
* ![](/img/users/sveltekit_min.svg)SvelteKit
* ![](/img/users/verdaccio_min.svg)Verdaccio
* Vercel
* ![](/img/users/nx.svg)Nx
* ![](/img/users/angular.svg)Angular

Benchmarks

Up to 69× faster than npm
-------------------------

Measured on a real project, across the states an install actually happens in — from a fresh clone to a warm re-run. Reproducible, and rebuilt on every deploy.

8.2×faster in total, across all 6 scenarios

10.8svs ~~1m 28s~~ with npm

[Explore the full benchmarks →](/benchmarks)

alotta-filespnpm 12npm

* cleanA fresh clone. Nothing cached.9.6× faster

  4.97s

  47.8s
* cacheReinstalling without a lockfile.14× faster

  952ms

  13.4s
* lockfileCI, first install.3.8× faster

  3.31s

  12.7s
* cache + lockfileReinstalling a project you already have.14× faster

  595ms

  8.61s
* everything warmRunning install when nothing changed.69× faster

  19ms

  1.32s
* updateA dependency was bumped in package.json.4.6× faster

  968ms

  4.43s

Everything you expect, and the things you didn’t know to ask for
----------------------------------------------------------------

pnpm is a drop-in replacement for npm — and then keeps going, with the features large repos actually need.

pnpm

npm

### Blazing fast installs

Resolution, fetching and linking happen in parallel instead of one stage at a time. On a warm store, an install is mostly just creating links.

[See the benchmarks →](/benchmarks)

appdocsapiweb

~/.pnpm-store **1 copy**

### Saving disk space

Files inside node\_modules are hard-linked from a single content-addressable store. A hundred projects on the same version cost you one copy on disk.

[Learn more →](/motivation)

### Workspace support

First-class monorepos: the workspace protocol for local packages, filtering to run tasks on just the projects you touched, and a single lockfile for everything.

[Learn more →](/workspaces)

### Catalogs

Define a dependency version once in pnpm-workspace.yaml and reference it as "catalog:" everywhere. One line to upgrade, and no more version-drift merge conflicts.

[Learn more →](/catalogs)

### Strict by default

Only your declared dependencies land in the root of node\_modules, so your code can never quietly import a package you never installed.

[Learn more →](/symlinked-node-modules-structure)

### Safer builds

Install scripts don’t run for arbitrary dependencies. You approve which packages may execute build scripts — supply-chain safety without extra tooling.

[Learn more →](/supply-chain-security)

### Patch dependencies

Fix a bug in a package without waiting for upstream — "pn patch" writes a persistent patch that is reapplied on every install.

[Learn more →](/cli/patch)

### Managing runtimes

Install and pin Node.js per project straight from pnpm — no nvm, no shell hooks, no “works on my machine” version mismatches.

[Learn more →](/cli/runtime)

How it works

A single store on disk, linked everywhere
-----------------------------------------

Other package managers copy the same files into every project. pnpm keeps one copy and links to it — that single design decision is where the speed and the disk savings come from.

* One copy per file, not per project

  With npm, 100 projects using the same dependency means 100 copies on disk. pnpm stores every file once in a content-addressable store and hard-links it into each node\_modules.
* Updates only store what changed

  If a new version of a package changes one file out of a hundred, pnpm adds exactly one file to the store instead of cloning the whole package again.
* A node\_modules you can trust

  pnpm symlinks only your declared dependencies into the root of node\_modules, so your code can never quietly import a package you never installed.
* Resolve, fetch and link in parallel

  Instead of finishing each stage before starting the next, pnpm links every package as soon as it is available — which is why installs feel instant on a warm store.

Content-addressable storea1f3…9c×4b7e2…41×3e94d…7a×45c08…d2×42f6b…e08d1c…3b×2c4a9…f6×271e5…08×4app/node\_modulesreact/index.jsreact-dom/index.jslodash/lodash.jszod/index.jsweb/node\_modulesreact/index.jsreact-dom/index.jsms/index.jszod/index.jsdocs/node\_modulesreact/index.jsreact-dom/index.jsms/index.jstypescript/tsc.jsapi/node\_modulesexpress/index.jslodash/lodash.jsms/index.jszod/index.jsadmin/node\_modulesreact/index.jslodash/lodash.jschalk/index.jszod/index.jscli/node\_moduleschalk/index.jstypescript/tsc.jsms/index.jslodash/lodash.js24 files in node\_modules → 8 on disk

1 copy

of every file on your disk, shared across all projects

0 bytes

extra disk space when a project reuses a version you already have

Strict

no access to undeclared dependencies, by default

Supply-chain security

Secure by default
-----------------

Compromised packages get published. pnpm makes sure they don’t get to run on your machine — no extra tools, no configuration.

~/my-app

↻ Replay

**3** of 4 protections are on out of the box

* [### Install scripts are blocked

  On by default

  Dependencies can’t run postinstall scripts unless you approve them. A compromised release can’t execute code the moment it’s installed.

  `allowBuilds`](/settings/build#allowbuilds)
* [### Fresh releases wait a day

  1 day by default

  Versions published less than 24 hours ago are skipped. Malware is usually caught and pulled within hours, before it ever reaches you.

  `minimumReleaseAge`](/settings/dependency-resolution#minimumreleaseage)
* [### No exotic transitive sources

  On by default

  Transitive dependencies can’t pull code from git repositories or raw tarball URLs, only from your trusted registries.

  `blockExoticSubdeps`](/settings/dependency-resolution#blockexoticsubdeps)
* [### Trust can’t silently drop

  One line to enable

  Refuse a version whose publishing trust got weaker, like a package that used trusted publishing and suddenly doesn’t.

  `trustPolicy: no-downgrade`](/settings/dependency-resolution#trustpolicy)

Learn more in [Mitigating supply chain attacks](/supply-chain-security).

pnpm vs npm
-----------

Everything npm does, plus the features that make large repos manageable.

| Feature | pnpm | npm |
| --- | --- | --- |
| Content-addressable storage | ✓ | — |
| CatalogsShared version ranges across a workspace. | ✓ | — |
| Managing runtimesInstall Node.js without nvm. | ✓ | — |
| Patching dependencies | ✓ | — |
| Side-effects cache | ✓ | — |
| Build script securityScripts only run for packages you allow. | ✓ | — |

Show all 12 features↓

See the [full feature comparison](/feature-comparison) in the documentation.

Releases

Shipping every week
-------------------

New features, fixes and security updates land continuously. Follow every release on the timeline.

Releases in the last 12 months
:   –

Average time between releases
:   – days

[Explore the release timeline →](/blog?type=releases)

@pnpmjs is a strong option for protecting against supply chain attacks, and the DX is excellent too they removed postinstall scripts a while back, cutting one big attack path now they’ve introduced minimumReleaseAge which lets you hold off on new versions for a day or more

![Feross](https://pbs.twimg.com/profile_images/1499215593089556483/VtxQLy6L_400x400.jpg)

###### Feross

@feross

Its not even been a day but I suddenly feel that @pnpmjs has improved my overall dev experience 🤯

![Sayantan Ghosh](https://pbs.twimg.com/profile_images/1952025282560569345/aNNNtaXm_400x400.jpg)

###### Sayantan Ghosh

@sayantan\_\_ghosh

This whole time I've stuck with npm out of habit and because it "just works". But then I had to override a subdependency via package.json, and npm just wouldn't do it. I spent hours fiddling. So @darcy recommends I use @pnpmjs , and w/ the same package.json, it "just works".

![Ben Vinegar](https://pbs.twimg.com/profile_images/1765244446650568704/zgjmJiTX_400x400.jpg)

###### Ben Vinegar

@bentlegen

Gotta say @pnpmjs has never let me down. Great piece of software.

![Guillermo Rauch](https://pbs.twimg.com/profile_images/1783856060249595904/8TfcCN0r_400x400.jpg)

###### Guillermo Rauch

@rauchg

By adopting the latest changes from @pnpmjs we got huge performance benefits in @bitdev\_ ! still early to call true numbers, but i'm seeing decreases of 40% in some flows! incredible work by @ZoltanKochan and the team behind pnpm!

![Itay Mendelawy](https://pbs.twimg.com/profile_images/657699734673485824/0UIcBpjO_400x400.jpg)

###### Itay Mendelawy

@itaymendel

I ❤️ pnpm. Just radically sped up a CI build by switching to pnpm and parallelizing tasks (which pnpm supports built-in) Before: 12 minutes After: 2 minutes 😀

![Cory House](https://pbs.twimg.com/profile_images/1963593369306750976/7gPWqEa8_400x400.jpg)

###### Cory House

@housecor

Zero-bug policy

Zero open bugs. Always.
-----------------------

Our goal is zero open bug reports at all times. A bug with steps to reproduce is picked up quickly and fixed as soon as possible.

[Live from GitHub0open bug reports is the goal](https://github.com/pnpm/pnpm/issues)

1. 1

   ### Report it with a reproduction

   Open an issue with the steps, or a small repository, that reproduce the bug.
2. 2

   ### It gets picked up fast

   Reproducible bugs go to the top of the queue. The issue list is kept at zero.
3. 3

   ### Fixed in the next release

   Fixes ship quickly, usually in the next patch or minor release.
4. [Report a bug](https://github.com/pnpm/pnpm/issues/new/choose)[Suggest a feature](https://github.com/pnpm/pnpm/discussions)

Issues are for bugs only. Feature requests and questions live in [GitHub Discussions](https://github.com/pnpm/pnpm/discussions).

These are the sponsors
----------------------

PLATINUM SPONSORS

[![Bit](/img/users/bit.svg)

Bit Cloud](https://bit.cloud/?utm_source=pnpm&utm_medium=home_page)[![OpenAI](/img/users/openai.svg)

OpenAI](https://openai.com/?utm_source=pnpm&utm_medium=home_page)[![Notion](/img/users/notion.svg)

Notion](https://notion.com/?utm_source=pnpm&utm_medium=home_page)[![CodeRabbit](/img/users/coderabbit_min.svg)

Code Rabbit](https://coderabbit.ai/?utm_source=pnpm&utm_medium=home_page)

GOLD SPONSORS

[![Sanity](/img/users/sanity.svg)

Sanity](https://sanity.io/?utm_source=pnpm&utm_medium=home_page)[![Discord](/img/users/discord_min.svg)

Discord](https://discord.com/?utm_source=pnpm&utm_medium=home_page)[![Vite](/img/users/vitejs.svg)

Vitejs](https://vite.dev/?utm_source=pnpm&utm_medium=home_page)[![SerpApi](/img/users/serpapi.svg)

SerpApi](https://serpapi.com/?utm_source=pnpm&utm_medium=home_page)[![Stackblitz](/img/users/stackblitz_min.svg)

StackBlitz](https://stackblitz.com/?utm_source=pnpm&utm_medium=home_page)[![Workleap](/img/users/workleap.svg)

Workleap](https://workleap.com/?utm_source=pnpm&utm_medium=home_page)[![Nx](/img/users/nx.svg)

Nx](https://nx.dev/?utm_source=pnpm&utm_medium=home_page)[![Latitude](/img/users/latitude_min.svg)

Latitude](https://latitude.so/?utm_source=pnpm&utm_medium=home_page)

SILVER SPONSORS

[![Replit](/img/users/replit_min.svg)

Replit](https://replit.com/?utm_source=pnpm&utm_medium=home_page)[![Cybozu](/img/users/cybozu_min.svg)

Cybozu](https://cybozu.co.jp/?utm_source=pnpm&utm_medium=home_page)[![BairesDev](/img/users/bairesdev_min.svg)

BairesDev](https://www.bairesdev.com/?utm_source=pnpm&utm_medium=home_page)[![Thesys](/img/users/thesys.svg)

Thesys](https://www.thesys.dev/?utm_source=pnpm&utm_medium=home_page)[![devowl.io](/img/users/devowlio_min.svg)

Devowlio](https://devowl.io/?utm_source=pnpm&utm_medium=home_page)[![u|screen](/img/users/uscreen.svg)

Uscreen](https://uscreen.de/?utm_source=pnpm&utm_medium=home_page)[![Leniolabs_](/img/users/leniolabs.jpg)

Leniolabs](https://www.leniolabs.com/?utm_source=pnpm&utm_medium=home_page)[Depot](https://depot.dev/?utm_source=pnpm&utm_medium=home_page)[Cerbos](https://cerbos.dev/?utm_source=pnpm&utm_medium=home_page)[⏱️

Time.now](https://time.now/?utm_source=pnpm&utm_medium=home_page)

Ready to reclaim your disk and your time?
-----------------------------------------

pnpm is a drop-in replacement for npm. Install it once, run pnpm install in any project — your package.json works as-is.

[Read the docs →](/installation)[Why pnpm?](/motivation)

macOS & LinuxWindows

```
$curl -fsSL https://get.pnpm.io/install.sh | sh -
```

Copy