




Auth backends (shared SQL) | pnpm






































Auth backends (shared SQL)Auth state — the registered users and their bearer tokens — is per-instance disk
state. By default users live in an htpasswd file and tokens in a local SQLite
database (see auth), so two pnpr replicas don't see
each other's accounts.
Adding a backend: block moves both into one shared SQL database, so several
stateless replicas share a consistent set of logins and tokens — the auth half
of running pnpr horizontally scaled. Only one backend may be selected in a
config file.
Database drivers are Cargo-feature gated:
BackendConfig keyCargo featurelibsql / Tursobackend.libsqlbackend-libsql (enabled by default)PostgreSQLbackend.postgres or backend.postgresqlbackend-postgresMySQL-compatiblebackend.mysqlbackend-mysql
For PostgreSQL or MySQL support, build pnpr with the matching Cargo feature, for
example cargo build -p pnpr --features backend-postgres.
Tip
Token lookups happen on the request hot path, so the database should be
low-latency from the server.

libsql / Turso#
storage: ./storage

backend:
  libsql:
    # libsql/Turso database URL. `libsql://…` for Turso, or
    # `http://127.0.0.1:8080` for a local `sqld`.
    url: ${PNPR_LIBSQL_URL}
    # Bearer token for the database. Omit for an unauthenticated local `sqld`.
    authToken: ${PNPR_LIBSQL_TOKEN}

KeyRequiredDescriptionurlyesDatabase URL — libsql://<db>.turso.io (Turso) or http://<host>:<port> (self-hosted sqld).authTokennoBearer token for the database. Omit for an unauthenticated local sqld.replicaPathnoPath to a local embedded replica. When set, reads (token lookups) hit this local file instead of a network round-trip; writes still go to the primary. Absent ⇒ every read is a remote query.syncIntervalSecsnoHow often (seconds) the embedded replica pulls from the primary. Only meaningful with replicaPath; bounds how stale a read can be (token-revocation lag). 0 disables background sync. Defaults to 60.
For a remote primary (e.g. Turso), serve reads from a local replica:
backend:
  libsql:
    url: ${PNPR_LIBSQL_URL}
    authToken: ${PNPR_LIBSQL_TOKEN}
    replicaPath: ./auth-replica.db
    syncIntervalSecs: 60

The trade-off is read freshness: an embedded replica reflects another replica's
writes (a token issued or revoked elsewhere) only after the next background
sync, so a lower syncIntervalSecs means less revocation lag. Omit
replicaPath to always read the primary directly.
PostgreSQL#
backend:
  postgres:
    url: ${PNPR_POSTGRES_URL}
    maxConnections: 16
    timeout: 30s
    startupTimeout: 5m

MySQL#
backend:
  mysql:
    url: ${PNPR_MYSQL_URL}
    maxConnections: 16
    timeout: 30s
    startupTimeout: 5m

KeyRequiredDescriptionurlyesDriver connection URL, such as postgres://user:pass@host/db or mysql://user:pass@host/db.maxConnectionsnoMaximum connections in the backend pool. Omit to use the driver's default.timeoutnoRequest-path auth database deadline. Defaults to 30s.startupTimeoutnoStartup connection and schema setup deadline. Defaults to 5m.
When the backend: block is absent, auth stays on local disk and the
auth.htpasswd / auth.tokens settings apply as before. The
auth.htpasswd.max_users registration cap is honored either way. Omitted
max_users and max_users: -1 both disable self-registration; set a
non-negative cap to let new users register.


