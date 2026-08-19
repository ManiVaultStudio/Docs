# PluginFactory

The plugin factory describes and creates instances of one plugin kind. For an implementation skeleton and guidance on factory-owned versus instance-owned state, see {doc}`Factory and plugin instance <../../../development/building_plugins/fundamentals/factory_and_instance>`.

Factories also advertise supported data and provide default or dataset-sensitive creation triggers. For the relationship between the broad capability declaration and exact selection rules, see {doc}`Creation triggers and inputs <../../../development/building_plugins/fundamentals/triggers_and_inputs>`.

**Qualified name:** `mv::plugin::PluginFactory`

```{doxygenclass} mv::plugin::PluginFactory
:members:
:protected-members:
