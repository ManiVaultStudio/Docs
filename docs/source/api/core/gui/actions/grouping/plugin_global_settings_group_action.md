# PluginGlobalSettingsGroupAction

**Qualified name:** `mv::gui::PluginGlobalSettingsGroupAction`

`PluginGlobalSettingsGroupAction` groups application preferences belonging to one plugin kind. A plugin factory owns and registers a plugin-specific derived group; the settings dialog then presents its child actions.

Begin with {doc}`Global plugin settings <../../../../../development/building_plugins/global_settings/index>` for a complete definition, registration, consumption, and migration pattern.

```{doxygenclass} mv::gui::PluginGlobalSettingsGroupAction
:members:
:protected-members:
```
