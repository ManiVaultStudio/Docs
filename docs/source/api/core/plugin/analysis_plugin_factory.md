# AnalysisPluginFactory

**Qualified name:** `mv::plugin::AnalysisPluginFactory`

`AnalysisPluginFactory` identifies a plugin kind as an analysis and narrows `produce()` to return an {doc}`AnalysisPlugin <analysis_plugin>`. A concrete factory supplies plugin metadata, supported data types, and any dataset-sensitive creation triggers through the inherited {doc}`PluginFactory <plugin_factory>` API.

The Core assigns validated input datasets through the managed request path. Do not call `produce()` directly. See {doc}`Factory and plugin instance <../../../development/building_plugins/fundamentals/factory_and_instance>` and {doc}`Plugin creation policy <../../../development/building_plugins/creation_policy/index>`.

```{doxygenclass} mv::plugin::AnalysisPluginFactory
:members:
:protected-members:
```
