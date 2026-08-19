# Implementation checklist

Use this checklist when introducing a plugin or reviewing its lifecycle integration.

## Factory

- Derive from the factory matching the instance type.
- Export the Qt interfaces and a stable plugin IID.
- Implement `produce()` as a small allocation step that passes `this` to the instance.
- Declare broad support with `supportedDataTypes()` and exact creation rules with trigger actions.
- Populate user-facing metadata and help links.
- Configure global settings, status-bar integration, standard-GUI visibility, and maximum instances only when needed.

## Instance

- Derive from the matching plugin base class.
- Establish QObject ownership and invariants in the constructor.
- Use `init()` for work that requires registration or assigned inputs.
- Revalidate inputs at execution time.
- Put project state in actions or explicit `toVariantMap()`/`fromVariantMap()` serialization.
- Use workflows for long-running operations; use tasks for progress when workflow execution is not appropriate.
- Request destruction through the core-managed plugin path.

## Build and verification

- Keep `PluginInfo.json`, the Qt IID, factory kind, and target naming deliberate and stable.
- Call `mv_handle_plugin_config()` and do not manually maintain the embedded core version.
- Verify creation from every advertised trigger, not only the main menu.
- Test project save and restore with missing, reordered, and linked datasets.
- Test cancellation, failure reporting, and plugin destruction while work is active.

## Common mistakes

Do not call `produce()` as an application-level creation API: it bypasses manager registration and lifecycle integration. Do not place per-instance state on the factory, because it will be shared across all instances. Do not rely solely on trigger validation, because inputs can also arrive through projects and programmatic requests. Finally, do not start expensive synchronous work in a constructor or `init()`; follow the {doc}`execution model guidance <../tasks/choosing_an_execution_model>`.
