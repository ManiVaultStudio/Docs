# Compatibility and round-trip testing

Project files commonly outlive the plugin version that wrote them. Treat serialized keys and meanings as a compatibility surface.

## Evolve state safely

- Keep constructor defaults for fields absent from older projects.
- Check optional keys before restoring them.
- Preserve old keys long enough to migrate them to the new representation.
- Add an explicit schema version when interpretation cannot be inferred safely.
- Reject corrupt required state with a diagnostic that names the plugin and key.
- Ignore unknown fields so newer projects can retain forward-compatible metadata where feasible.

Do not catch every restoration exception inside the plugin and continue with half-applied state. Catch only errors for which the plugin can establish a valid fallback, add useful context, and otherwise throw to the owning restoration boundary.

The boundary determines whether that exception fails the complete operation. In particular, current Core catches exceptions raised while restoring an individual **view plugin's state**, records a structured workflow warning with the plugin identity and exception evidence, and continues loading the remaining workspace. A view plugin should therefore restore transactionally where practical: validate before mutating, or return itself to a safe default before throwing. Other workflow serialization failures may still fail the project operation.

## Test the full lifecycle

At minimum, test:

1. Create a project and configure non-default state.
2. Save, close, and reopen it in a fresh process.
3. Verify datasets, relationships, action values, views, and plugin inputs.
4. Save the restored project again and reopen that result.
5. Load representative projects from older supported plugin versions.
6. Exercise missing optional plugins, missing optional keys, and malformed required values.
7. Cancel or fail an operation-level serialization workflow and verify that no apparently successful partial project is presented.
8. Make one view plugin reject malformed state and verify that project loading reports the structured warning, the plugin remains safe, and the remaining workspace can still be restored.

Compare semantics rather than raw `QVariantMap` ordering. IDs that are intended to persist should match; transient caches and runtime-only objects should be reconstructed rather than compared.
