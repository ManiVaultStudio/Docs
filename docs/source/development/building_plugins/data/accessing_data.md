# Accessing and finding data

Use `mv::data()` to query the registered dataset collection. The manager returns handles rather than transferring ownership.

## By identifier

Dataset IDs are stable identifiers used by events and serialization:

```cpp
const auto dataset = mv::data().getDataset(datasetId);

if (!dataset.isValid())
    return;
```

Use the typed overload when the expected implementation is known:

```cpp
const auto points = mv::data().getDataset<Points>(datasetId);
```

Looking up an unavailable ID produces an invalid handle. Treat restoration as a dependency-resolution step rather than assuming every serialized reference is immediately available.

## Enumerating datasets

`getAllDatasets()` returns all registered datasets or filters them by `DataType` values. Prefer manager queries over walking GUI models when application data—not its presentation—is required.

The datasets list model and its filter models exist primarily for Qt views and selection widgets. Use them when constructing UI, but do not make domain logic depend on row positions or proxy-model ordering.

## Data types and kinds

A `DataType` is the logical type exposed by a raw-data plugin. The `kind` passed to `createDataset()` selects the plugin that will create the implementation. Display names, plugin kinds, raw-data instance names, dataset IDs, and hierarchy names serve different purposes and should not be substituted for one another.

## Concrete data access

The base `DatasetImpl` API covers common behavior; actual values are exposed by the concrete data type. For example, point-data operations should use `Dataset<Points>` and the `Points` API.

Respect the synchronization contract of the concrete implementation. A valid dataset handle protects lifetime observation, not concurrent access to its underlying storage. When processing data in parallel, use the data type's documented read/write locking or copy the required values before scheduling work.

## Properties

`DatasetImpl` supports named `QVariant` properties for lightweight metadata. Use them for optional, serializable annotations—not as a replacement for a typed data model. Establish stable names and value types when properties form a contract between plugins.
