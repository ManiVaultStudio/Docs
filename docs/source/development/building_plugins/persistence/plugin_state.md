# Defining plugin-owned state

Serialize the minimum authoritative state required to reconstruct a plugin instance. Typical state includes action values, selected dimensions, rendering configuration, and stable references to datasets or other persistent objects.

Override `toVariantMap()` and `fromVariantMap()` symmetrically for small, immediate state:

```cpp
QVariantMap ExampleViewPlugin::toVariantMap() const
{
    auto map = ViewPlugin::toVariantMap();
    _pointSizeAction.insertIntoVariantMap(map);
    map["InputDatasetId"] = _input.getDatasetId();
    return map;
}

void ExampleViewPlugin::fromVariantMap(const QVariantMap& map)
{
    ViewPlugin::fromVariantMap(map);

    if (map.contains(_pointSizeAction.getSerializationName()))
        _pointSizeAction.fromParentVariantMap(map);

    if (map.contains("InputDatasetId"))
        _input = mv::data().getDataset<Points>(map["InputDatasetId"].toString());
}
```

Always call the direct base implementation so framework-owned identity, plugin metadata, view state, and superclass fields survive the round trip.

Do not serialize QWidget pointers, cached rendering output, tasks, transient errors, or values that can be derived cheaply from authoritative state. See {doc}`Saving and restoring action state <../actions/serialization>` for action-specific conventions. When authoritative state contains a binary array or buffer that should not become a large list of ordinary variant values, use a {doc}`blob variant map <binary_blob_data>`.
