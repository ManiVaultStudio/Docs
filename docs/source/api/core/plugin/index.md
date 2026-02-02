# Plugin
 

## Base class and factory

All **ManiVault** plugins are derived from a generic **plugin** base class and are created by a **plugin factory**.

```{toctree}
:maxdepth: 1

plugin
plugin_factory
```

## Types

ManiVault plugins are categorized by their primary role within the platform. There are plugins for reading, writing, analyzing, transforming and viewing data. The classes below are all derived from the [plugin base class](plugin).

```{toctree}
:maxdepth: 1

analysis_plugin
loader_plugin
transformation_plugin
view_plugin
writer_plugin
```

## Miscellaneous

The class below are used to compose a plugin shortcut map and adding plugin metadata.

```{toctree}
:maxdepth: 1

plugin_shortcuts
plugin_metadata
```