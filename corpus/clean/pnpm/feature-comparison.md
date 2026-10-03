Feature Comparison
==================

| Feature | pnpm | npm | Notes |
| --- | --- | --- | --- |
| [Workspace support](/workspaces) | ✅ | ✅ |  |
| Isolated `node_modules` | ✅ | ✅ | Default in pnpm. |
| [Hoisted `node_modules`](/settings/node-modules#nodelinker) | ✅ | ✅ | Default in npm. |
| Plug'n'Play | ✅ | ❌ |  |
| [Autoinstalling peers](/settings/peer-dependencies#autoinstallpeers) | ✅ | ✅ |  |
| [Patching dependencies](/cli/patch) | ✅ | ❌ |  |
| [Managing runtimes](/cli/runtime) | ✅ | ❌ |  |
| [Managing versions of itself](/settings/cli#pmonfail) | ✅ | ❌ |  |
| Has a lockfile | ✅ | ✅ | `pnpm-lock.yaml`, `package-lock.json`. |
| [Overrides support](/settings/dependency-resolution#overrides) | ✅ | ✅ |  |
| Content-addressable storage | ✅ | ❌ |  |
| [Dynamic package execution](/cli/pnx) | ✅ | ✅ | `pnx`, `npx`. |
| [Side-effects cache](/settings/build#sideeffectscache) | ✅ | ❌ |  |
| [Catalogs](/catalogs) | ✅ | ❌ |  |
| [Config dependencies](/config-dependencies) | ✅ | ❌ |  |
| [JSR registry support](/cli/add#install-from-the-jsr-registry) | ✅ | ❌ |  |
| [Auto-install before script run](/settings/build#verifydepsbeforerun) | ✅ | ❌ |  |
| [Hooks](/pnpmfile) | ✅ | ❌ |  |
| [Build script security](/settings/build#allowbuilds) | ✅ | ❌ |  |
| [SBOM generation](/cli/sbom) | ✅ | ✅ | `pnpm sbom`, `npm sbom`. |
| [Listing licenses](/cli/licenses) | ✅ | ❌ | pnpm supports it via `pnpm licenses list`. |

**Note:** To keep the comparison concise, we include only features likely to be used frequently.
