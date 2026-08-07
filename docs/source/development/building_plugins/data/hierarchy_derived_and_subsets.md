# Hierarchy, derived data, and subsets

These concepts describe different relationships and should be chosen deliberately.

## Data hierarchy

Every registered dataset has a `DataHierarchyItem`. The item controls UI parentage, visibility, expansion, hierarchy selection, lock presentation, attached actions, and context-menu content.

Read hierarchy relationships through the dataset when possible:

```cpp
const auto parent   = dataset->getParent();
const auto children = dataset->getChildren({}, true);
```

Use `mv::dataHierarchy()` for hierarchy-wide queries and UI selection. Hierarchy selection means that dataset rows are selected in the application interface; it is distinct from selecting elements inside a dataset.

## Derived datasets

A derived dataset is a full dataset with a source relationship:

```cpp
auto derived = mv::data().createDerivedDataset<Points>(
    "Normalized measurements",
    sourceDataset);
```

By default it is placed below its source in the hierarchy. A separate parent argument can change that presentation without changing its source.

Derived datasets use their source dataset's selection. `getSourceDataset<T>()` resolves to the original source through a chain, while `getNextSourceDataset<T>()` returns the immediate source. Use the immediate relation when reconstructing a transformation chain and the resolved source when common raw-data or selection identity matters.

The `mayUnderive` policy of the concrete implementation controls what happens when its source disappears: a dataset may become independent, or it may need to be removed with its source.

## Subsets

A subset is copied from a selection and remembers its original full dataset:

```cpp
auto subset = sourceDataset->createSubsetFromSelection(
    "Selected measurements",
    sourceDataset);
```

The data manager copies the selection implementation, assigns values from the source according to the concrete dataset's assignment behavior, and records the full-dataset relationship. If the source is already a subset, the new subset still points back to the original full dataset.

## Proxy datasets

A proxy dataset combines foreign member datasets instead of owning ordinary storage. Concrete types decide whether a proposed group is compatible through `mayProxy()` and how member values are exposed. Check `isProxy()` and use `getProxyMembers()` when behavior differs for grouped data.

## Do not infer semantics from the tree

Hierarchy placement is presentation and navigation. Always query `isDerivedData()`, `isFull()`, `getSourceDataset()`, `getFullDataset()`, or `isProxy()` for semantic relationships.
