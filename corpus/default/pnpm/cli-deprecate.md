




pnpm deprecate | pnpm






































pnpm deprecateAdded in: v11.0.0
Set a deprecation message on a published package version. Consumers running pnpm install will see this message when the matching version is installed.
pnpm deprecate <pkg>[@<version-range>] <message>

To clear a deprecation message, use pnpm undeprecate or pass an empty string:
pnpm deprecate foo@1.0.0 ""

Examples#
Deprecate a single version:
pnpm deprecate foo@1.0.0 "Use foo@2 instead"

Deprecate a range of versions:
pnpm deprecate "foo@<2" "Please upgrade to foo@2"

Deprecate all versions:
pnpm deprecate foo "This package is no longer maintained"

Options#
--registry <url>#
The registry to publish to. Defaults to the registry configured for the package.
--otp <code>#
When the registry requires two-factor authentication, supply the one-time password via this flag or the PNPM_CONFIG_OTP environment variable.
pnpm undeprecate#
Remove a deprecation message from a package version. Equivalent to running pnpm deprecate <pkg>[@<version-range>] "".
pnpm undeprecate <pkg>[@<version-range>]



