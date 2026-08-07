# Parenting, changes, and lifetime

A hierarchy item's parent determines where its dataset appears. It does not change source data, subset membership, selection sharing, or proxy membership.

## Establish parentage during creation

Prefer supplying the intended parent when creating a dataset. The data manager then registers the dataset and hierarchy item together:

```cpp
auto result = mv::data().createDataset<Points>(
    "Points",
    "Result",
    sourceDataset);
```

This establishes hierarchy parentage only. Use the dedicated derived- or subset-creation API when the dataset also has source or full-dataset semantics; see {doc}`Creating and registering datasets <../creating_datasets>`.

`DataHierarchyItem::setParent()` can change presentation parentage later. Use it deliberately, avoid cycles, and retain semantic relationships separately. The manager emits `itemParentChanged(item)` after the item emits `parentChanged(parent)`.

## Observe hierarchy changes

The hierarchy manager exposes collection-level signals:

- `itemAdded(item)`;
- `itemAboutToBeRemoved(item)`;
- `itemRemoved(datasetId)`;
- `itemParentChanged(item)`;
- `selectedItemsChanged(items)`.

Use `itemAboutToBeRemoved` for final access to the item or its dataset. After `itemRemoved`, only the stable dataset ID remains.

## Pointer lifetime

The hierarchy manager owns `DataHierarchyItem` objects. A pointer returned by `getItem()`, `getItems()`, or a signal is borrowed and becomes invalid when its dataset is removed. Do not capture that pointer in queued or asynchronous work.

Capture a `Dataset<T>` handle or dataset ID instead, and perform a fresh lookup when work runs:

```cpp
const auto datasetId = dataset.getDatasetId();

schedule([datasetId]() {
    auto* item = mv::dataHierarchy().getItem(datasetId);
    if (!item)
        return;

    // Use the current hierarchy item synchronously.
});
```

For the dataset's own two-phase removal contract, see {doc}`Removal and asynchronous work <../events/removal_and_lifetime>`.
