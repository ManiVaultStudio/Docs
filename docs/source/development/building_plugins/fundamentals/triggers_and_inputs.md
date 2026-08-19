# Creation triggers and inputs

A factory answers two related but different questions:

- Which data types can this plugin generally consume?
- Is creation valid for this exact ordered selection of datasets?

Override `supportedDataTypes()` for the broad capability declaration. Use dataset-sensitive trigger actions for exact rules involving dataset count, order, type combinations, parentage, or other properties.

```cpp
mv::DataTypes ExampleViewPluginFactory::supportedDataTypes() const
{
    return { PointType };
}
```

Return no dataset-sensitive trigger actions when the selection is unsupported. A returned action should capture the validated input selection and request the plugin through the normal plugin-manager path when triggered. Do not make the action call `produce()` directly.

The exact trigger constructor and ownership pattern depends on the desired placement and plugin type. See {doc}`Dataset-sensitive plugin triggers <../communication/dataset_triggers>` for complete patterns, and {doc}`Requesting plugins <../communication/requesting_plugins>` when one plugin needs to create another.

## Receiving inputs

The core assigns creation inputs before `init()` for analysis, transformation, and writer plugins. Views can additionally receive datasets through `loadData()`, including after the view already exists. Loader plugins obtain their inputs from an external source selected by the user. Data plugins create the storage backing new datasets.

Validate inputs at both boundaries:

- The factory controls whether the UI offers a creation path.
- The instance validates data before executing, because projects, scripts, linked datasets, and other programmatic pathways can change state without using that exact trigger.

For safe dataset access and ownership rules, see {doc}`Working with data and datasets <../data/index>`.
