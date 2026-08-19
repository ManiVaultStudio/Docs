# Plugin lifecycle

The core controls factory and instance lifetimes. Understanding the order prevents initialization that accidentally depends on services or datasets that are not available yet.

## Factory lifecycle

1. Qt loads the plugin library and constructs its exported factory.
2. ManiVault supplies the plugin kind and version obtained from the library metadata.
3. The core calls `PluginFactory::initialize()` to initialize standard factory actions and metadata help integration.
4. The factory remains available for creation requests until application shutdown.

Use the factory constructor for declarative setup such as metadata, icons, supported creation policy, global settings, and status-bar actions. If a custom factory overrides `initialize()`, call the base implementation and reserve the override for work that truly requires completed factory registration.

## Instance lifecycle

1. A creation request identifies a factory by plugin kind.
2. The factory's `produce()` allocates an instance.
3. The core checks the instance limit and updates the factory counters.
4. Type-specific input and output datasets are assigned where applicable.
5. The instance is registered with the appropriate core managers.
6. The core calls the instance's `init()` method.
7. Type-specific UI and notifications are completed and the instance enters normal use.
8. Project save and restore call the serialization hooks when applicable.
9. Destruction removes the instance and decrements the factory's live-instance count.

## Constructor versus `init()`

In the constructor, establish object invariants and create QObject-owned actions, models, and other members. Avoid assuming that the plugin is already registered or that type-specific datasets have been assigned.

In `init()`, connect the instance to application services, assemble UI that depends on a registered plugin, and react to assigned datasets. Keep initialization responsive. Start substantial work through the {doc}`workflow engine or task integration <../tasks/index>` rather than blocking the GUI thread.

If overriding `init()` in a derived class whose base has an implementation, preserve the base-class contract by calling it unless that base explicitly documents otherwise.

## Destruction and references

Use the core-managed destruction path exposed by `Plugin::destroy()` rather than deleting an instance owned by the plugin manager. Treat pointers to plugins, datasets, widgets, and actions according to their documented ownership. When an object can disappear independently of the observer, prefer guarded Qt references such as `QPointer` and disconnect or invalidate cached state on destruction.

For restoring instance state, ordering, and action serialization, see {doc}`Project persistence <../persistence/index>`.
