# Events and dataset lifetime

Dataset changes are distributed through the core event system. `Dataset<T>` handles listen to those events and expose Qt signals for the common case; `EventListener` provides lower-level filtering across datasets.

## Prefer handle signals for one dataset

When a component already stores a dataset handle, connect to that handle:

```cpp
connect(&_points, &mv::Dataset<Points>::dataChanged,
        this, &ViewModel::refresh);

connect(&_points, &mv::Dataset<Points>::aboutToBeRemoved,
        this, &ViewModel::detachDataset);
```

This keeps identity filtering and event registration inside the handle.

## Use an event listener for broad observation

`EventListener` can receive all dataset events or events filtered by `DataType`. Supported `EventType` values further restrict delivery.

```cpp
_eventListener.addSupportedEventType(
    static_cast<std::uint32_t>(mv::EventType::DatasetAdded));

_eventListener.registerDataEvent(
    [this](mv::DatasetEvent* event) {
        handleDatasetEvent(event);
    });
```

Make the listener an owned member. Its destructor unregisters it from the core. Callbacks receive event pointers for the duration of dispatch; do not retain those pointers.

## Removal phases

Removal has two important phases:

- **about to be removed:** the dataset is marked for removal but its implementation can still be inspected for final detachment;
- **removed:** the implementation is gone, handles have been reset, and the event carries stable information such as dataset ID and data type.

Never dereference a handle in a removed callback without checking it. Cache only the metadata needed after removal.

## Queued and asynchronous work

A handle that was valid when work was scheduled can become invalid before that work runs. Capture a `Dataset<T>` rather than a raw pointer and check it inside the callback:

```cpp
auto points = _points;

schedule([points]() mutable {
    if (!points.isValid())
        return;

    // Access the dataset according to its threading contract.
});
```

Dataset validity does not make the implementation thread-safe. It only indicates that the core still owns the object and that it is not in the removal state.

## Emitting change events

Concrete data implementations should modify their state completely before notifying the core about data, dimensional, selection, locking, or hierarchy changes. Observers should see a consistent new state when the event arrives.
