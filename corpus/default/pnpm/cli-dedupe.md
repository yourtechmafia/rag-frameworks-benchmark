




pnpm dedupe | pnpm






































pnpm dedupePerform an install removing older dependencies in the lockfile if a newer version can be used.
Workspace selection#
Since v12.4.1, pnpm dedupe processes every project in the workspace by default, including workspaces that keep a lockfile per project. Narrow the run with the usual filters, for example pnpm dedupe --filter ./packages/app.
Options#
--check#
Check if running dedupe would result in changes without installing packages or editing the lockfile. Exits with a non-zero status code if changes are possible.
--filter <package_selector>#
Restrict the command to the selected projects. Read more about filtering.
--fail-if-no-match#
Exit with an error when no project matches the given filters, instead of doing nothing.


