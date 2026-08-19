# Choosing a plugin type

Choose the runtime type from the plugin's primary responsibility. This determines the base classes for both the factory and the produced instance, and which lifecycle hooks the core invokes.

| Type | Use it when the plugin primarily… | Main instance entry point |
| --- | --- | --- |
| `View` | presents interactive data or application UI | `loadData()` for datasets supplied after creation |
| `Analysis` | performs a computation from input datasets and may produce outputs | input and output dataset accessors |
| `Transformation` | applies a focused transformation to input data | `transform()` |
| `Loader` | imports an external source into ManiVault datasets | `loadData()` |
| `Writer` | exports ManiVault datasets to an external representation | `writeData()` |
| `Data` | implements storage for a data type and creates its `DatasetImpl` objects | `createDataSet()` |

The corresponding pairs are `ViewPlugin`/`ViewPluginFactory`, `AnalysisPlugin`/`AnalysisPluginFactory`, and so on. All pairs ultimately derive from {doc}`Plugin and PluginFactory <../../../api/core/plugin/index>`.

## Type boundaries

Prefer an existing data plugin unless the project genuinely needs a new storage representation. Most visualization and computation plugins consume existing datasets; they do not need to be data plugins.

Use an analysis plugin for a substantive computation and a transformation plugin for a focused data operation. Long-running work in either type should use the {doc}`workflow-backed execution guidance <../tasks/choosing_an_execution_model>` so progress, cancellation, results, and failures are handled consistently.

A view can initiate analysis, but the view should remain responsible for presentation. Put reusable computation in an analysis or transformation plugin, or in a shared library, rather than making it inseparable from one widget.

## Runtime type versus `PluginInfo.json` type

`mv::plugin::Type` is the runtime role listed above. The optional top-level `type` in `PluginInfo.json` is build metadata used by `mv_handle_plugin_config` to group the target in generated IDE projects. For example, a system-provided view may use `"type": "System"` in the JSON while its factory is still a `ViewPluginFactory`. Do not use the JSON value to infer runtime behavior.
