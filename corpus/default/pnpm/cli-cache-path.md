




pnpm cache path | pnpm






































pnpm cache pathAdded in: v11.22.0
Prints the directory pnpm uses for its metadata cache, mirroring pnpm store path. The path is printed absolute and lexically cleaned, so a relative cacheDir yields a path other tools can consume.
pnpm cache path

pnpm derives this directory from the platform and the cacheDir setting, so a CI setup that wants to cache it no longer has to mirror that resolution by hand:
.github/workflows/ci.yaml- name: Get the cache directory
  run: echo "PNPM_CACHE_DIR=$(pnpm cache path)" >> $GITHUB_ENV

Besides registry metadata and the pnpm dlx cache, that directory holds the lockfile verification log — the record of which lockfile passed which supply-chain policies. Restoring it lets a job skip re-verifying a lockfile the log already covers under the policies currently configured — the dominant cost of an install in CI once the store is warm. Since v11.22.0, pnpm store prune no longer deletes that log.
Important
Only cache this directory in locations writable by trusted jobs. See the cacheDir setting for details.



