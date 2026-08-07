# Finding items and navigating the tree

Use dataset methods when starting from a dataset. They preserve the convenient `Dataset<T>` handle abstraction:

```cpp
const auto parent   = dataset->getParent();
const auto children = dataset->getChildren({}, false); // direct children
const auto descendants = dataset->getChildren({}, true);
```

Use the hierarchy manager for project-wide traversal or when an API requires hierarchy items:

```cpp
auto& hierarchy = mv::dataHierarchy();

const auto* item = hierarchy.getItem(dataset.getDatasetId());
const auto topLevelItems = hierarchy.getTopLevelItems();
const auto allItems = hierarchy.getItems();
```

`getItem()` returns `nullptr` when lookup fails after reporting the core error. Check the result before use, and do not retain an item pointer across dataset removal.

From an item, `getParent()`, `getAncestors()`, and `getChildren(recursively)` navigate the displayed tree. `getDataset()` converts back to a generic dataset handle; use the templated overload only when the concrete type is known.

## Filter semantic relationships through datasets

Tree ancestry alone does not establish that data is derived, a subset, or a proxy. Two datasets can be parent and child for presentation while having independent storage. Query the dataset explicitly:

```cpp
if (dataset->isDerivedData()) {
    const auto source = dataset->getNextSourceDataset<mv::DatasetImpl>();
    // Immediate transformation source.
}

if (!dataset->isFull()) {
    const auto full = dataset->getFullDataset<mv::DatasetImpl>();
    // Original full dataset for this subset.
}
```

Use tree relationships for navigation and presentation; use dataset relationships for data semantics.
