# WriterPlugin

**Qualified name:** `mv::plugin::WriterPlugin`

A writer plugin exports one or more ManiVault datasets through `writeData()`. The managed creation path assigns its ordered input dataset selection before initialization.

Pair a writer instance with a {doc}`WriterPluginFactory <writer_plugin_factory>`. The factory advertises broad input support and contextual creation triggers through the common {doc}`PluginFactory <plugin_factory>` API.

```{doxygenclass} mv::plugin::WriterPlugin
:members:
:protected-members:
