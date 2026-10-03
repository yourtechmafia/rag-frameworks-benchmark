




pnpm lane | pnpm






































pnpm laneAdded in: v11.13.0
Manages per-package release lanes. A lane is a parallel release track: while a package is on one, the bare pnpm version -r releases it as X.Y.Z-<lane>.N prereleases while the rest of the workspace keeps releasing stable versions. Moving a package back to the main lane releases its accumulated stable version on the next run.
pnpm lane
pnpm lane <name> --filter <pattern>
pnpm lane main --filter <pattern>

Membership lives under the versioning.lanes key of pnpm-workspace.yaml; this command is a convenience editor for that key.
Usage#
Show lane membership#
pnpm lane

Lanes:
  alpha:
    @example/cli
    @example/napi

If no package has been assigned a lane, this prints All packages are on the main lane.
Move packages onto a lane#
pnpm lane alpha --filter @example/cli

--filter is required — it selects the packages to move. Lane names may contain only alphanumerics and hyphens, and cannot be purely numeric.
Move packages back to the main lane#
pnpm lane main --filter @example/cli

main is the reserved name of the default lane. Every package is on it unless assigned elsewhere, and packages on it release stable versions. Graduating a package releases the stable version its prereleases were building toward on the next pnpm version -r run.
Versions on a lane#
A package on a lane releases X.Y.Z-<lane>.N, where X.Y.Z is the stable version the lane is building toward and N counts up from 0:
Current versionPending intentLaneNew version2.0.0minoralpha2.1.0-alpha.02.1.0-alpha.0patchalpha2.1.0-alpha.12.1.0-alpha.1majoralpha3.0.0-alpha.03.0.0-alpha.0—main3.0.0
N restarts at 0 whenever the stable target changes. When a bump escalates the target — a major intent while the lane was building a minor — the target is recomputed and the counter resets.
Packages in the same fixed group must move between lanes together.
Options#
--filter <package_selector&gt;#
Select the packages to move between lanes. Required when assigning a lane.
Read more about filtering.


