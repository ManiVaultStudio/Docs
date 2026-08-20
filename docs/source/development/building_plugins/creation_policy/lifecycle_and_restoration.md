# Lifecycle and project restoration

Instance limits participate in the full managed lifecycle. They therefore affect more than the menu item that initially creates a plugin.

## Count transitions

On successful managed creation, the core increases both the live count and the cumulative produced count. When a managed instance is destroyed, the live count decreases; the cumulative count does not. The factory emits:

- `numberOfInstancesChanged(std::uint32_t)` when the live count changes;
- `numberOfInstancesProducedChanged(std::uint32_t)` when the cumulative count changes.

The live-count change also refreshes the enabled state of the factory's standard trigger. Code that observes these signals should use them for presentation or diagnostics, not to maintain a second authoritative count.

For pointer ownership and destruction notifications, see {doc}`Lifetime and error handling <../communication/lifetime_and_errors>`.

## Project restoration uses creation policy

Project restoration requests saved plugin instances through the plugin manager. The same maximum therefore applies while a project is opened, including instances that are not being created through visible UI.

This makes a new or reduced limit a project-format compatibility decision. A project saved with more instances than the new maximum cannot recreate all of them through the normal request path. Before shipping a stricter limit:

1. test projects saved by earlier plugin versions;
2. decide whether every saved instance is essential;
3. keep the maximum high enough for supported projects, or provide an explicit restoration strategy;
4. report partial restoration clearly rather than silently dropping state.

Do not temporarily mutate the counters to force restoration through. That breaks accounting and leaves later trigger state unreliable.

See {doc}`Project lifecycle <../persistence/project_lifecycle>` and {doc}`Compatibility and testing <../persistence/compatibility_and_testing>` for the surrounding persistence contract.

## Failed requests

Creation can fail because the kind is unavailable, the maximum has been reached, production returns no instance, initialization fails, or plugin-specific loading fails. Callers should regard the manager request as one fallible operation and avoid publishing dependent state until it succeeds.

Plugin initialization should also be exception-safe: acquire resources with RAII, parent QObjects deliberately, and avoid externally visible side effects that cannot be rolled back. See {doc}`Exceptions and failure boundaries <../diagnostics/exceptions>` and {doc}`QObject lifetime and ownership <../qt_considerations/qobject_ownership>`.

## Destruction restores capacity

Destroy managed plugins through the plugin system rather than deleting borrowed pointers. When destruction completes, factory accounting is updated and a previously saturated standard trigger becomes available again. Keep retained references lifecycle-aware, for example with `QPointer` where appropriate.
