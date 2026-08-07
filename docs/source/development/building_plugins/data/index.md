# Working with data and datasets

Datasets are ManiVault's central data abstraction. Plugins exchange `Dataset<T>` handles, while the core owns the corresponding `DatasetImpl` objects, registers them with the data manager, places them in the data hierarchy, maintains selections, and broadcasts lifecycle events.

This guide explains the model from a plugin developer's perspective: how to safely retain and access datasets, create new data, represent derived data and subsets, react to changes and removal, and implement a new data type.

```{important}
Do not treat `Dataset<T>` as an owning smart pointer. It is an event-aware reference managed around a core-owned dataset. Always check `isValid()` before dereferencing it, particularly across event-loop turns and asynchronous work.
```

## Recommended path

Begin with the mental model and dataset handles. Continue with creation and hierarchy for ordinary plugin development. The final pages cover selection propagation, events, and implementing a new raw-data plugin.

```{toctree}
:maxdepth: 2

mental_model
dataset_handles
accessing_data
creating_datasets
hierarchy/index
hierarchy_derived_and_subsets
selections_and_linked_data
events/index
implementing_a_data_type
```

For exact signatures, see the {doc}`core data API reference <../../../api/core/data/index>`.
