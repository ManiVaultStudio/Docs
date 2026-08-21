# WriterPluginFactory

**Qualified name:** `mv::plugin::WriterPluginFactory`

`WriterPluginFactory` identifies a plugin kind as a writer and narrows `produce()` to return a {doc}`WriterPlugin <writer_plugin>`. Concrete factories use the common {doc}`PluginFactory <plugin_factory>` input declarations and dataset-sensitive triggers to offer export operations for valid selections.

The managed request path assigns the selected datasets and initializes the instance. `produce()` should only allocate the matching writer and must not be called directly by plugin code.

```{doxygenclass} mv::plugin::WriterPluginFactory
:members:
:protected-members:
```
