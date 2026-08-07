# Choosing a settings scope

ManiVault has several persistence mechanisms. Choose based on who owns the value and how long it should live.

| State | Scope | Mechanism |
| --- | --- | --- |
| Point size for one view instance | Plugin instance and project | Plugin `toVariantMap()` / `fromVariantMap()` |
| Default point size for every instance | Plugin kind and application installation | Plugin global settings action |
| Internal preference without a UI | Plugin kind and application installation | `Plugin::setSetting()` / `getSetting()` |
| Temporary rollback within one interaction | Current action object | `cacheState()` / `restoreState()` |

## Project-owned instance state

Most action values belong to one plugin instance and should travel with the project. Serialize them explicitly with the plugin, as shown in {doc}`Saving and restoring action state <serialization>`.

## Application settings for an action

`WidgetAction::setSettingsPrefix(...)` associates an action with the application settings store. The plugin overload namespaces the key as `Plugins/<plugin kind>/<settings prefix>`:

```cpp
_defaultPointSizeAction.setSettingsPrefix(
    this, "Rendering/DefaultPointSize");
```

By default, setting the prefix immediately attempts to load existing state. Call `saveToSettings()` when the value should be persisted, commonly from a value-change connection. This path is for preferences that should survive independently of projects, not for per-instance project state.

## Plugin-wide global settings

Use a `PluginGlobalSettingsGroupAction` when a preference should be shared by all instances and appear in ManiVault's settings interface. The group is normally owned and registered by the plugin factory, whose lifetime matches the plugin kind rather than one plugin instance.

See {doc}`Plugin-wide global settings <../global_settings>` for setup and registration.

## Avoid double persistence

Do not normally store the same authoritative value in both a project map and application settings. Restoration order would determine which copy wins, and opening a project could unexpectedly change a global preference. If an instance begins from a global default, copy the default when the instance is created and then serialize the instance value only with its project.
