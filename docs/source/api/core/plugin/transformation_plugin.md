# TransformationPlugin

**Qualified name:** `mv::plugin::TransformationPlugin`

A transformation plugin performs a focused transformation over one or more input datasets through `transform()`. The managed creation path assigns its input datasets before initialization.

Pair a transformation instance with a {doc}`TransformationPluginFactory <transformation_plugin_factory>`. See {doc}`Choosing a plugin type <../../../development/building_plugins/fundamentals/choosing_a_type>` for the boundary between transformations and larger analyses.

```{doxygenclass} mv::plugin::TransformationPlugin
:members:
:protected-members:
