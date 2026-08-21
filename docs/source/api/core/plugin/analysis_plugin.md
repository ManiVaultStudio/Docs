# AnalysisPlugin

**Qualified name:** `mv::plugin::AnalysisPlugin`

An analysis plugin consumes one or more input datasets and may publish one or more output datasets. Its input and output handles are assigned through the managed plugin lifecycle and are persisted by the base implementation.

Pair an analysis instance with an {doc}`AnalysisPluginFactory <analysis_plugin_factory>`. For choosing analysis rather than transformation or view, and for long-running execution guidance, see {doc}`Choosing a plugin type <../../../development/building_plugins/fundamentals/choosing_a_type>`.

```{doxygenclass} mv::plugin::AnalysisPlugin
:members:
:protected-members:
