pnpm whoami
===========

Added in: v11.0.0

Print the username associated with the current registry credentials.

```
pnpm whoami [--registry <url>]
```

If you are not logged in, the command exits with an error. Use [`pnpm login`](/cli/login) to authenticate first.

Options[#](#options)
--------------------

### --registry <url>[#](#--registry-url)

The registry to check. Defaults to the configured default registry.