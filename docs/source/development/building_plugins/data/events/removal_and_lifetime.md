# Removal and asynchronous work

Dataset removal deliberately has two phases. Choose the callback according to what information you need.

## Before removal

`DatasetAboutToBeRemoved` and `Dataset<T>::aboutToBeRemoved()` run before the core destroys the dataset implementation. Use this phase to disconnect dataset-dependent state, remove UI references, or copy small pieces of metadata needed later.

Do not attempt to prevent removal or start new work against the dataset. It has already been marked as about to be removed.

## After removal

`DatasetRemoved` is emitted after the implementation has gone. Its dataset handle is intentionally invalid; `DatasetRemovedEvent` instead supplies `getDatasetGuid()` and `getDataType()`. The handle signal `removed(datasetId)` likewise supplies only the stable ID.

```cpp
if (event->getType() == mv::EventType::DatasetRemoved) {
    const auto* removed = static_cast<mv::DatasetRemovedEvent*>(event);
    forgetDataset(removed->getDatasetGuid(), removed->getDataType());
}
```

## Queued and asynchronous work

A handle that is valid when work is scheduled may be invalid when that work runs. Capture the handle instead of a raw implementation pointer and check it inside the callback:

```cpp
auto points = _points;

schedule([points]() mutable {
    if (!points.isValid())
        return;

    // Access the dataset according to its threading contract.
});
```

Validity only describes lifetime; it does not make the dataset implementation thread-safe. Complete mutations before notifying the event manager so synchronous observers see consistent state.
