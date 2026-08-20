# Lifecycle, visibility, and persistence

## Conditional visibility

`PluginStatusBarAction` contains a toggle named **Only visible when instantiated**. It is checked by default:

- checked: the item is intended to be visible when at least one instance of its plugin kind exists;
- unchecked: the item is always visible, subject to the application status bar itself being visible.

The action listens for plugin addition and imminent destruction and reevaluates its factory's instance count. The plugin kind passed to the constructor must resolve to a loaded factory; an empty or unknown kind is not a safe way to create a generic status item. Use `StatusBarAction` for non-plugin application infrastructure.

```{note}
The destruction notification currently occurs before the plugin destructor decrements the factory's instance count. Test removal of the last instance carefully. If exact count-driven visibility is essential, a plugin-specific subclass can observe `PluginFactory::numberOfInstancesChanged()` and make that signal authoritative.
```

## Application status-bar visibility

The main window shows the status bar only while a project exists and the application-wide **Show status bar** setting is enabled. An individually visible plugin action therefore does not appear on the start or Learning Center pages, or while the complete status bar is disabled.

Per-project status-bar override actions are present in the project model and serialized, but their application to the main-window item set is currently disabled. Do not promise users project-specific status-bar composition until that integration is enabled in the core.

## Runtime updates

Update values on the GUI thread through their action setters. If state originates in a worker or workflow job, publish the result through its GUI-thread continuation or dispatcher before touching actions or widgets.

Factory ownership keeps the status-bar action alive across plugin-instance creation and destruction. Instance callbacks must disconnect automatically through QObject context or be removed explicitly; never leave a factory-owned status item capturing a destroyed instance pointer.

For multiple instances, recompute aggregate state from an authoritative collection when instances are added or removed. Incremental counters are easy to desynchronize during failed creation, project restore, or bulk teardown.

## Persistence

Status text, counts, severity, and progress are normally transient projections of other state. Do not serialize them independently. After project restore or application startup, rebuild the display from the factory, plugin manager, tasks, datasets, or service that owns the real state.

Persist an actual user preference—such as an always-enabled plugin-wide mode—through {doc}`global plugin settings <../global_settings/index>`, not by serializing the status-bar widget. Keep instance-specific choices with their plugin project state.
