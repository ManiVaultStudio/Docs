# GlobalSettingsGroupAction

**Qualified name:** `mv::gui::GlobalSettingsGroupAction`

`GlobalSettingsGroupAction` is the common action container for application-wide settings. When a child action belongs to its QObject hierarchy, `addAction()` assigns the child's persistent settings prefix and loads stored state.

Plugin developers normally use the specialized {doc}`PluginGlobalSettingsGroupAction <plugin_global_settings_group_action>` rather than deriving directly from this base. See {doc}`Global plugin settings <../../../../../development/building_plugins/global_settings/index>` for ownership, scope, and compatibility guidance.

```{doxygenclass} mv::gui::GlobalSettingsGroupAction
:members:
:protected-members:
```
