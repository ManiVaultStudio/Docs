# ViewPluginFactory

**Qualified name:** `mv::plugin::ViewPluginFactory`

`ViewPluginFactory` identifies a plugin kind as a view, narrows `produce()` to return a {doc}`ViewPlugin <view_plugin>`, and describes initial workspace placement.

The constructor records whether instances are system views and whether they initially float. System-view factories are limited to one live instance by default. A concrete factory may also choose the preferred dock area; the default is the right dock area. These are factory-level policies shared by every instance of the plugin kind.

Request views through the plugin manager so creation policy, input assignment, workspace placement, initialization, and instance accounting remain intact. See {doc}`Plugin creation policy <../../../development/building_plugins/creation_policy/index>`.

```{doxygenclass} mv::plugin::ViewPluginFactory
:members:
:protected-members:
```
