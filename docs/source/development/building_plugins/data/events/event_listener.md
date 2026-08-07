# Listening across datasets

`mv::EventListener` is appropriate for project-wide observers, services that follow a whole data type, and code that needs concrete event payloads. Constructing it registers it with the core; destruction unregisters it, so keep it as an owned member rather than a temporary local variable.

## Select event types first

The supported-event set is an allowlist. Add every event kind the listener should receive:

```cpp
_eventListener.addSupportedEventType(
    static_cast<std::uint32_t>(mv::EventType::DatasetAdded));
_eventListener.addSupportedEventType(
    static_cast<std::uint32_t>(mv::EventType::DatasetRemoved));

_eventListener.registerDataEvent(
    [this](mv::DatasetEvent* event) {
        handleDatasetEvent(event);
    });
```

`setSupportedEventTypes(...)` replaces the complete allowlist. `removeSupportedEventType(...)` stops delivery of that kind. An empty allowlist delivers no events.

## Choose callback filtering

`registerDataEvent(...)` adds a callback for every allowed dataset event. `registerDataEventByType(...)` invokes a callback only for datasets of the specified `DataType`:

```cpp
_eventListener.registerDataEventByType(
    PointType,
    [this](mv::DatasetEvent* event) {
        updatePointDatasetState(event);
    });
```

Registering another callback for the same `DataType` replaces the previous type-specific callback. General callbacks registered with `registerDataEvent(...)` are appended.

To follow one dataset with an `EventListener`, register a general callback and compare its ID. Treat removal separately because its event no longer contains a valid dataset handle:

```cpp
_eventListener.registerDataEvent([this](mv::DatasetEvent* event) {
    if (event->getType() == mv::EventType::DatasetRemoved) {
        auto* removed = static_cast<mv::DatasetRemovedEvent*>(event);
        if (removed->getDatasetGuid() == _datasetId)
            datasetWasRemoved();
        return;
    }

    const auto dataset = event->getDataset();
    if (dataset.isValid() && dataset.getDatasetId() == _datasetId)
        datasetChanged(event);
});
```

## Dispatch lifetime

Events are stack objects dispatched directly to current listeners. The `DatasetEvent*` is borrowed for the callback only; never store it. Copy a `Dataset<T>` handle, ID, or other required metadata if work must continue later.
