# Selections and linked data

ManiVault distinguishes selection of dataset rows in the hierarchy from selection of elements inside a dataset. This page concerns element selection.

## Selection datasets

Creating a normal full dataset also creates an associated selection dataset for the same raw-data instance. `DatasetImpl::getSelection()` returns that dataset. Derived datasets resolve selection through their source.

Concrete data types implement:

- `getSelectionIndices()`;
- `setSelectionIndices()`;
- `canSelect()`, `canSelectAll()`, `canSelectNone()`, and `canSelectInvert()`;
- `selectAll()`, `selectNone()`, and `selectInvert()`.

Set selection through the concrete dataset API rather than mutating internal storage. The implementation is responsible for maintaining its representation and notifying the event system.

```cpp
if (points.isValid() && points->canSelect())
    points->setSelectionIndices(indices);
```

## Selection notifications

Consumers can connect to `Dataset<T>::dataSelectionChanged`. Keep callbacks idempotent: linked datasets and grouped selections can cause one user operation to update several datasets.

Avoid writing a new selection unconditionally from inside a selection-changed callback. Compare the intended state or use the propagation facilities provided by the data type to prevent feedback loops.

## Linked data

`LinkedData` associates a source dataset, a target dataset, and a `SelectionMap`. The map translates selected source indices to target indices. Indexed mappings store explicit index relationships; image-pyramid mappings calculate relationships from source and target image sizes.

Datasets can add, remove, serialize, and resolve linked-data mappings. Send and receive flags control the allowed propagation direction.

Use linked data when two datasets describe corresponding entities but do not share one raw-data selection. Use derived datasets when the new dataset is a transformation sharing source lineage, and use subsets when the new dataset contains selected elements from a full dataset.

## Selection groups and proxies

The event manager also supports selection grouping across compatible datasets, while proxy datasets represent several member datasets as one dataset. These features have concrete-type-specific behavior. Before implementing custom propagation, check whether the data type already resolves selections through linked data or proxy membership.
