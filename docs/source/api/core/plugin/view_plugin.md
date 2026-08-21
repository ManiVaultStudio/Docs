# ViewPlugin

**Qualified name:** `mv::plugin::ViewPlugin`

A view plugin owns an interactive widget and the actions integrated into its title bar, dock areas, and overlays. It can receive datasets during managed creation and later through `loadData()`.

Pair a view instance with a {doc}`ViewPluginFactory <view_plugin_factory>`, which supplies the view's system-view and initial-placement policy. See {doc}`Choosing a plugin type <../../../development/building_plugins/fundamentals/choosing_a_type>` for keeping reusable computation separate from presentation.

```{doxygenclass} mv::plugin::ViewPlugin
:members:
:protected-members:
