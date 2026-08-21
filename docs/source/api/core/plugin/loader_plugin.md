# LoaderPlugin

**Qualified name:** `mv::plugin::LoaderPlugin`

A loader plugin imports an external source into ManiVault. Implement `loadData()` as the loader's entry point; `AskForFileName()` is available when the loader uses an interactive file choice and remembers the last directory for that plugin kind.

Pair a loader instance with a {doc}`LoaderPluginFactory <loader_plugin_factory>`. A loader that cannot parse or read a chosen file may report a {doc}`DataLoadException <data_load_exception>` through the appropriate user-facing failure boundary.

```{doxygenclass} mv::plugin::LoaderPlugin
:members:
:protected-members:
