# Plugin
 
Plugins are the primary extension mechanism in ManiVault. They allow new functionality to be added to the platform without modifying the core application, enabling features such as data loading, analysis, transformation, visualization, and export to be developed and deployed independently.

Each plugin follows a common lifecycle defined by the plugin base class and is instantiated through a plugin factory. Depending on their role, plugins are categorized into specific types that determine how they integrate with the application and interact with data and user workflows.

The sections below describe the core building blocks of the plugin system, the available plugin types, and supporting classes used for metadata and shortcut configuration.

For lifecycle, ownership, input, and implementation guidance, start with {doc}`Plugin fundamentals <../../../development/building_plugins/fundamentals/index>`. The pages below are the accompanying API reference.

## Base class and factory

All **ManiVault** plugins are derived from a generic **plugin** base class and are created by a **plugin factory**.

```{toctree}
:maxdepth: 1

plugin
plugin_factory
```

## Types

ManiVault plugins are categorized by their primary role within the platform. There are plugins for reading, writing, analyzing, transforming and viewing data. The classes below are all derived from the [plugin base class](plugin).

Each runtime role has a matching factory specialization. Derive the instance and factory from the same pair, and return the matching instance type from `produce()`. Creation must still be requested through the plugin manager; `produce()` is the factory hook used by that managed path, not a public construction shortcut.

| Role | Instance | Factory |
| --- | --- | --- |
| Analysis | {doc}`AnalysisPlugin <analysis_plugin>` | {doc}`AnalysisPluginFactory <analysis_plugin_factory>` |
| Loader | {doc}`LoaderPlugin <loader_plugin>` | {doc}`LoaderPluginFactory <loader_plugin_factory>` |
| Transformation | {doc}`TransformationPlugin <transformation_plugin>` | {doc}`TransformationPluginFactory <transformation_plugin_factory>` |
| View | {doc}`ViewPlugin <view_plugin>` | {doc}`ViewPluginFactory <view_plugin_factory>` |
| Writer | {doc}`WriterPlugin <writer_plugin>` | {doc}`WriterPluginFactory <writer_plugin_factory>` |

The data-role pair, `RawData` and `RawDataFactory`, is documented with the {doc}`data API <../data/index>` because it defines dataset storage rather than an operation over existing datasets.

```{toctree}
:maxdepth: 1

analysis_plugin
analysis_plugin_factory
loader_plugin
loader_plugin_factory
data_load_exception
transformation_plugin
transformation_plugin_factory
view_plugin
view_plugin_factory
writer_plugin
writer_plugin_factory
```

## Miscellaneous

The class below are used to compose a plugin shortcut map and adding plugin metadata.

```{toctree}
:maxdepth: 1

plugin_shortcuts
plugin_metadata
```
