# Persistence and compatibility

Global preferences are stored by the application and are independent of project serialization. Two mechanisms use separate namespaces:

| Mechanism | Current settings namespace |
| --- | --- |
| Child of `PluginGlobalSettingsGroupAction` | `GlobalSettings/<plugin kind>/<action serialization name>` |
| `Plugin::getSetting()` and `setSetting()` | `Plugins/<plugin kind>/<relative path>` |

Treat these generated paths as identifiers, not as locations that plugin code should concatenate itself. Use the supplied group and plugin APIs so naming remains consistent.

## Stable identifiers

The following values affect lookup and should be treated as persistent compatibility contracts:

- the plugin kind;
- each global child action's serialization name;
- every relative path passed to `getSetting()` and `setSetting()`;
- the serialized shape and value type of custom actions.

Titles, tooltips, icons, ranges, and layout can normally change without moving the setting, provided the serialization name remains stable.

## Renaming and migration

Prefer retaining an established key even when its display text changes. If a UI-less path must move, read the new path with an invalid `QVariant` sentinel, fall back to the old path, validate it, and write the converted value to the new path. The old value may remain in the application store; do not repeatedly let it override the new authoritative key.

Action-backed migration requires deliberate loading of the previous serialized action map before adopting the new path. Keep that compatibility code bounded to the versions that wrote the old representation and test it with a real settings store from those versions.

When changing a value type or range, validate restored data before applying it. Define a safe fallback for missing, malformed, non-finite, or out-of-range values. Custom action deserializers should reject structurally invalid maps clearly rather than leaving partially restored state.

## Interaction with projects

Do not write global settings into the plugin's project variant map. Conversely, do not use `setSetting()` as a shortcut for saving instance state.

A common and safe pattern is:

1. A new instance copies a global default into an instance action.
2. The instance action is then authoritative for that instance.
3. Project serialization saves and restores the instance action.
4. Changing the global default affects instances created later, not restored project state.

For a true live policy, omit the project-owned copy and let every instance observe the shared global action.
