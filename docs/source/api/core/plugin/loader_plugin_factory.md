# LoaderPluginFactory

**Qualified name:** `mv::plugin::LoaderPluginFactory`

`LoaderPluginFactory` identifies a plugin kind as a loader and narrows `produce()` to return a {doc}`LoaderPlugin <loader_plugin>`. Its standard contextual trigger represents loading an external source and therefore does not depend on the currently selected datasets or data types.

A concrete loader factory still uses the inherited {doc}`PluginFactory <plugin_factory>` API for metadata, instance limits, and application integration. Request instances through the plugin manager instead of calling `produce()` directly.

```{doxygenclass} mv::plugin::LoaderPluginFactory
:members:
:protected-members:
```
