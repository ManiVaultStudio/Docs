# Plugin
 
Plugins are the primary extension mechanism in ManiVault. They allow new functionality to be added to the platform without modifying the core application, enabling features such as data loading, analysis, transformation, visualization, and export to be developed and deployed independently.

Each plugin follows a common lifecycle defined by the plugin base class and is instantiated through a plugin factory. Depending on their role, plugins are categorized into specific types that determine how they integrate with the application and interact with data and user workflows.

The sections below describe the core building blocks of the plugin system, the available plugin types, and supporting classes used for metadata and shortcut configuration.

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