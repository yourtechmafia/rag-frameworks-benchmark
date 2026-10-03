Installation
============

pnpr is distributed on npm as [`@pnpm/pnpr`](https://www.npmjs.com/package/@pnpm/pnpr).
The npm wrapper requires Node.js 18 or newer. Install it globally:

```
pnpm add -g @pnpm/pnpr
```

The wrapper package resolves to the native binary published under
`@pnpm/pnpr.<platform>-<arch>` (e.g. `@pnpm/pnpr.linux-x64`). Prebuilt binaries
are available for:

* `linux-x64`, `linux-arm64`
* `linux-x64-musl`, `linux-arm64-musl`
* `darwin-x64`, `darwin-arm64`
* `win32-x64`, `win32-arm64`

Only the binary matching your platform is downloaded.

Verify the installation[#](#verify-the-installation)
----------------------------------------------------

```
pnpr --version
```

Next steps[#](#next-steps)
--------------------------

Continue to the [Quick start](/pnpr/quick-start) to run the server and point a
client at it.