# Dataset events and listeners

Dataset events let a plugin react when datasets enter or leave the project, their contents or selection change, or their place in the hierarchy changes. Most plugin code should observe a `Dataset<T>` handle; use `EventListener` when the scope is broader than one known dataset.

## Choose the narrowest subscription

| Need | Prefer |
| --- | --- |
| Refresh a view for one stored dataset | {doc}`Signals on the dataset handle <handle_signals>` |
| Observe one or more event kinds across datasets | {doc}`EventListener <event_listener>` |
| Understand the payload available for each change | {doc}`Event types and payloads <event_types>` |
| Detach safely when data disappears | {doc}`Removal and asynchronous work <removal_and_lifetime>` |

The handle-signal API performs dataset identity filtering for you. `EventListener` is lower-level: you select event types explicitly and then optionally filter callbacks by `DataType` or inspect dataset identity yourself.

```{important}
An `EventListener` does not receive anything until at least one supported `EventType` is added. Registering a callback alone is not sufficient.
```

```{toctree}
:maxdepth: 1

handle_signals
event_listener
event_types
removal_and_lifetime
```

For exact class and method signatures, see the {doc}`dataset events API reference <../../../../api/core/data/events/index>`.
