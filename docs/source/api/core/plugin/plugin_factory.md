# PluginFactory

The plugin factory describes and creates instances of one plugin kind. For an implementation skeleton and guidance on factory-owned versus instance-owned state, see {doc}`Factory and plugin instance <../../../development/building_plugins/fundamentals/factory_and_instance>`.

Factories also advertise supported data and provide default or dataset-sensitive creation triggers. For the relationship between the broad capability declaration and exact selection rules, see {doc}`Creation triggers and inputs <../../../development/building_plugins/fundamentals/triggers_and_inputs>`.

A factory may also own and register one settings group shared by every instance of its plugin kind. See {doc}`Global plugin settings <../../../development/building_plugins/global_settings/index>` for the lifetime and initialization pattern.

Factories can similarly register one plugin-kind status-bar action during startup. See {doc}`Status-bar integration <../../../development/building_plugins/status_bar/index>` for ownership, positioning, and multi-instance behavior.

Factories also define whether standard interfaces may offer a plugin and how many live instances may coexist. See {doc}`Plugin creation policy and instance limits <../../../development/building_plugins/creation_policy/index>` before using the instance counters or maximum directly.

**Qualified name:** `mv::plugin::PluginFactory`

```{doxygenclass} mv::plugin::PluginFactory
:members:
:protected-members:
