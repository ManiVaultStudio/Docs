# Data and datasets

The data API defines ManiVault's central runtime data model. `Dataset<T>` is the event-aware handle used by consumers, `DatasetImpl` is the common implementation base, and raw-data plugins provide concrete data kinds. Supporting types describe identity, hierarchy placement, linked selections, and dataset lifecycle events.

For ownership rules, relationship semantics, and examples, begin with {doc}`Working with data and datasets <../../../development/building_plugins/data/index>`.

## Dataset model

```{toctree}
:maxdepth: 1

dataset
dataset_impl
dataset_private
data_type
data_hierarchy_item
```

## Data plugins

```{toctree}
:maxdepth: 1

raw_data
raw_data_factory
```

## Relationships and events

```{toctree}
:maxdepth: 2

linked_data
selection_map
events/index
```

## Related managers and models

- {doc}`AbstractDataManager <../managers/abstract_data_manager>` owns and manages registered datasets.
- {doc}`AbstractDataHierarchyManager <../managers/abstract_data_hierarchy_manager>` manages hierarchy items and hierarchy selection.
- Dataset {doc}`models <../models/datasets/index>` expose registered datasets to Qt views.
- Data-hierarchy {doc}`models <../models/data_hierarchy/index>` expose the hierarchy to Qt views.
