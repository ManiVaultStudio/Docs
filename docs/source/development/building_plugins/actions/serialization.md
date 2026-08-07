# Saving and restoring action state

Project serialization preserves settings belonging to one plugin instance. Although every action is serializable, a plugin must explicitly include its own actions in the plugin variant map.

## The standard pattern

Give each action a stable serialization name, call the base implementation, and use the parent-map helpers symmetrically:

```cpp
ExampleViewPlugin::ExampleViewPlugin(const PluginFactory* factory) :
    ViewPlugin(factory),
    _pointSizeAction(this, "Point size"),
    _showLabelsAction(this, "Show labels")
{
    _pointSizeAction.setSerializationName("PointSize");
    _showLabelsAction.setSerializationName("ShowLabels");
}

QVariantMap ExampleViewPlugin::toVariantMap() const
{
    auto variantMap = ViewPlugin::toVariantMap();

    _pointSizeAction.insertIntoVariantMap(variantMap);
    _showLabelsAction.insertIntoVariantMap(variantMap);

    return variantMap;
}

void ExampleViewPlugin::fromVariantMap(const QVariantMap& variantMap)
{
    ViewPlugin::fromVariantMap(variantMap);

    _pointSizeAction.fromParentVariantMap(variantMap);
    _showLabelsAction.fromParentVariantMap(variantMap);
}
```

The base calls preserve state owned by `Plugin`, `ViewPlugin`, or another superclass. Omitting them can silently lose framework-managed state.

## Serialization names are persistent keys

`WidgetAction` initially uses its title as its serialization name. Set an explicit, stable name when a displayed title might change, be translated, or contain presentation wording. Changing a serialization name later breaks lookup of state written under the old key unless migration code handles both names.

Every child inserted into the same parent map needs a unique serialization name. `insertIntoVariantMap()` detects collisions rather than silently overwriting an entry.

## Restoration compatibility

Projects can outlive a plugin release. When adding a new optional action, check whether its key exists or use the helper's loading-error option according to the compatibility policy. Preserve sensible constructor defaults when older projects have no value.

If state restoration is expensive, staged, or requires progress reporting, use the workflow serialization contract described by {doc}`Serializable <../../../api/core/util/serialization/serializable>` rather than starting background work inside synchronous `fromVariantMap()`.

```{important}
Do not serialize transient widget pointers, derived display state, or duplicate copies of values already held by actions. Serialize the authoritative action and rebuild transient UI from it.
```
