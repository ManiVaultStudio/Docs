# Dataset-sensitive plugin triggers

A `PluginTriggerAction` is a discoverable request to create a plugin. Every factory has a default trigger; factories can additionally return contextual triggers for selected datasets or data types.

Override the dataset form when availability depends on actual dataset properties:

```cpp
mv::gui::PluginTriggerActions MyViewFactory::getPluginTriggerActions(
    const mv::Datasets& datasets) const
{
    mv::gui::PluginTriggerActions triggers;

    if (datasets.isEmpty() ||
        !areAllDatasetsOfTheSameType(datasets, PointType))
        return triggers;

    auto* trigger = new mv::gui::PluginTriggerAction(
        nullptr,
        this,
        "My view",
        "Open the selected point datasets",
        icon());

    trigger->setDatasets(datasets);
    trigger->setRequestPluginCallback(
        [this](mv::gui::PluginTriggerAction& action) {
            mv::Datasets validDatasets;
            for (const auto& dataset : action.getDatasets())
                if (dataset.isValid())
                    validDatasets << dataset;

            if (!validDatasets.isEmpty())
                mv::plugins().requestViewPlugin(getKind(), nullptr,
                    mv::gui::DockAreaFlag::Right, validDatasets);
        });

    triggers << trigger;
    return triggers;
}
```

The plugin manager collects, sorts, and initializes contextual triggers before returning them to the UI. `initialize()` assigns the factory icon and stable trigger hash. Code calling a factory override directly must use `PluginFactory::initializePluginTriggerActions()` before presentation.

## Dataset versus data-type overloads

Use `getPluginTriggerActions(const Datasets&)` when count, order, identity, or current state matters. Use the `DataTypes` overload when the operation can be described from types alone. `supportedDataTypes()` is broad factory metadata; it does not replace contextual validation.

Set a task-oriented menu location with `setMenuLocation()` when the default Data, Import, Transform, View, Analyze, or Export path is insufficient. Keep titles concise and tooltips explicit about the selected-data requirements.
