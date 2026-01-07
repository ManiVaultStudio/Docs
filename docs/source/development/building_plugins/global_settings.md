# Plugin-wide global settings

Some plugins expose **global settings** that apply to the plugin as a whole, rather than to a specific plugin instance. **ManiVault** provides a dedicated mechanism to define, register, and persist such settings in a consistent way.

This page explains how plugin-wide global settings work, how they are registered, and how they are stored.

![Global settings](../../assets/global_settings.png)

*The Example View plugin exposes a global default point size and opacity for all Example View instances.*

---

## What are plugin-wide global settings?

Plugin-wide global settings are:

- Shared by **all instances** of a plugin.
- Independent of any particular project or view.
- Persisted in the application’s **settings store**.
- Exposed automatically in ManiVault’s **global settings UI**.

Typical use cases include:
- Default rendering or behavior options
- Feature toggles
- Paths, thresholds, or limits that apply to all instances
- Plugin-wide preferences that should survive application restarts

The API for plugin global settings is in the `mv::plugin::PluginFactory`, or a derived factory.
---

## Global settings group action

Global settings are exposed through a **group action** of type:

```cpp
mv::gui::PluginGlobalSettingsGroupAction
```

This group action contains the actions (checkboxes, numeric fields, selectors, etc.) that make up the plugin’s global settings UI.

### Querying the global settings group action

```cpp
mv::gui::PluginGlobalSettingsGroupAction* mv::plugin::PluginFactory::getGlobalSettingsGroupAction() const;
```

Returns a pointer to the plugin’s global settings group action, or `nullptr` if the plugin does not define global settings.

### Registering the global settings group action

```cpp
void mv::plugin::PluginFactory::setGlobalSettingsGroupAction(gui::PluginGlobalSettingsGroupAction* pluginGlobalSettingsGroupAction);
```

When this function is called:

- The group action is **registered with the ManiVault core**.
- Its contents automatically appear in ManiVault’s **global settings UI**.
- The settings are connected to the persistent settings store.

Passing `nullptr` removes the plugin’s global settings from the global settings UI.

> **Important**  
> Plugin developers do not need to manually add the group action to any UI. Registration via `setGlobalSettingsGroupAction()` is sufficient.

---

## Settings storage and prefixes

Each plugin’s global settings are stored under a **plugin-specific prefix** in the settings store.

### Global settings prefix

```cpp
QString mv::plugin::PluginFactory::getGlobalSettingsPrefix() const final;
```

This function returns the prefix used to namespace the plugin’s global settings.

The prefix determines:
- Where the settings are stored on disk
- How settings are isolated between plugins
- How naming conflicts are avoided

All actions contained in the plugin’s global settings group automatically store and retrieve their values under this prefix.

> **Note**  
> Plugin developers should treat the global settings prefix as **stable API**. Changing it will cause existing user settings to be lost or ignored.

---

## Typical setup pattern

Global settings are usually created and registered during plugin or factory initialization.

```cpp
auto globalSettings = new gui::PluginGlobalSettingsGroupAction(
    this,
    "My Plugin Settings"
);

// Add actions to the group
globalSettings->addAction(new gui::BoolAction(this, "Enable feature"));
globalSettings->addAction(new gui::DecimalAction(this, "Global threshold"));

// Register the group action
setGlobalSettingsGroupAction(globalSettings);
```

Once registered:
- The settings appear in ManiVault’s global settings UI.
- Values are loaded automatically at startup.
- Changes are persisted automatically.

---

## Design guidelines

When defining plugin-wide global settings, keep the following in mind:

- Use global settings **sparingly**; prefer instance-level settings where appropriate.
- Avoid storing project-specific or view-specific state globally.
- Choose clear, stable setting names.
- Group related settings logically within the group action.
- Assume settings may be edited while plugin instances are active.

---

## Lifecycle considerations

- Global settings typically live for the lifetime of the plugin factory.
- The core owns integration into the settings system; plugins own the actions.
- Removing or renaming settings keys may invalidate existing user preferences.

---

## Summary

- Plugin-wide global settings are exposed via a `PluginGlobalSettingsGroupAction`.
- Registering the group action automatically integrates it into ManiVault’s global settings UI.
- The settings prefix determines where values are stored and must remain stable.
- Persistence and UI integration are handled by the core.

This mechanism allows plugins to expose consistent, discoverable, and persistent global configuration without custom UI or storage logic.
