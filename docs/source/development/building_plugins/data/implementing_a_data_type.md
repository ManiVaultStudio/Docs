# Implementing a data type

A data plugin supplies a `plugin::RawData` implementation, a `RawDataFactory`, and one or more concrete `DatasetImpl` classes. This is a framework-extension task; plugins that merely consume existing data types do not need these pieces.

## Raw-data plugin

Derive from `plugin::RawData` and associate it with a `DataType`. Implement `createDataSet()` to allocate an unregistered concrete dataset implementation:

```cpp
mv::Dataset<mv::DatasetImpl> MyRawData::createDataSet(
    const QString& id) const
{
    return mv::Dataset<mv::DatasetImpl>(
        new MyDataset(getName(), true, id));
}
```

The data manager takes ownership after creation. `getRawDataSize()` should report the storage attributable to the raw-data instance when meaningful.

The factory derives from `plugin::RawDataFactory` and produces the raw-data plugin. Its plugin kind is the string consumers pass to `createDataset()`.

## Concrete dataset

Derive the implementation from `DatasetImpl`. At minimum, implement the abstract data and selection contract:

- `copy()`;
- `createSubsetFromSelection()`;
- `getSelectionIndices()` and `setSelectionIndices()`;
- selection capability and convenience operations;
- serialization of the concrete data;
- assignment or copy behavior needed by subset creation.

Use `init()` for setup that requires manager and hierarchy registration. Constructors should establish local invariants without assuming that the dataset has already been registered.

## Full data, selections, and subsets

The manager asks the raw-data plugin for both a full implementation and a selection implementation. Ensure the concrete class can represent each state. `copy()` is used to create subset material from the selection dataset, after which the manager assigns source content and records the full-dataset relationship.

Study an existing built-in data plugin with similar storage and selection semantics before defining a new one. Point data demonstrates multidimensional numerical storage and proxy behavior; image, color, cluster, and text data demonstrate different selection and serialization choices.

## Notifications

After a mutation, notify the core through the established event-manager path used by existing data types. Emit the narrowest correct event: ordinary data changes, dimension changes, and selection changes have different consumers.

## Serialization

`DatasetImpl` participates in workflow-based serialization. A concrete implementation must preserve its data, source/full relationships, properties, selections, linked mappings, and type-specific metadata in the appropriate phase. IDs supplied during creation are reserved for restoration so references can be reconnected consistently.

## Checklist

Before publishing a data type, test full-dataset creation, selection creation, copying, subset creation, derived data, hierarchy removal, invalidated handles, serialization round trips, linked selection where supported, and concurrent access according to the storage contract.
