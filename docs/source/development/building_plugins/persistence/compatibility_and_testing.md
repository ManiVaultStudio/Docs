# Compatibility and round-trip testing

Project files commonly outlive the plugin version that wrote them. Treat serialized keys and meanings as a compatibility surface.

## Evolve state safely

- Keep constructor defaults for fields absent from older projects.
- Check optional keys before restoring them.
- Preserve old keys long enough to migrate them to the new representation.
- Add an explicit schema version when interpretation cannot be inferred safely.
- Reject corrupt required state with a diagnostic that names the plugin and key.
- Ignore unknown fields so newer projects can retain forward-compatible metadata where feasible.

Do not catch every restoration exception and continue with a half-valid plugin. Catch only errors you can recover from, add useful context, and otherwise let project loading report the failure.

## Test the full lifecycle

At minimum, test:

1. Create a project and configure non-default state.
2. Save, close, and reopen it in a fresh process.
3. Verify datasets, relationships, action values, views, and plugin inputs.
4. Save the restored project again and reopen that result.
5. Load representative projects from older supported plugin versions.
6. Exercise missing optional plugins, missing optional keys, and malformed required values.
7. Cancel or fail workflow serialization and verify that no apparently successful partial project is presented.

Compare semantics rather than raw `QVariantMap` ordering. IDs that are intended to persist should match; transient caches and runtime-only objects should be reconstructed rather than compared.
