# PluginFactory

The plugin factory is responsible for creating plugins of a certain type. Each plugin must be accompanied by a factory, the [example plugins](https://github.com/ManiVaultStudio/ExamplePlugins/tree/master) repository contains several examples that show how to achieve this.

Factories also advertise supported data and provide default or dataset-sensitive creation triggers. For implementation patterns, see {doc}`Dataset-sensitive plugin triggers <../../../development/building_plugins/communication/dataset_triggers>`.

**Qualified name:** `mv::plugin::PluginFactory`

```{doxygenclass} mv::plugin::PluginFactory
:members:
:protected-members:
