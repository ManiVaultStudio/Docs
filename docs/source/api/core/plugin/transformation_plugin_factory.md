# TransformationPluginFactory

**Qualified name:** `mv::plugin::TransformationPluginFactory`

`TransformationPluginFactory` identifies a plugin kind as a transformation and narrows `produce()` to return a {doc}`TransformationPlugin <transformation_plugin>`. Use the inherited {doc}`PluginFactory <plugin_factory>` capabilities to declare supported data, construct contextual triggers, and configure creation policy.

Inputs are assigned by the managed plugin request path before instance initialization. `produce()` should only allocate the matching concrete instance; it should not perform the transformation or bypass manager ownership.

```{doxygenclass} mv::plugin::TransformationPluginFactory
:members:
:protected-members:
```
