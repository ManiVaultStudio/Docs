# Event listener

`EventListener` registers with the core event manager and supports general callbacks plus callbacks filtered by `DataType`. Event types form an explicit allowlist: add at least one supported type before expecting delivery. Destruction unregisters the listener.

For ownership, filtering, and callback-lifetime examples, see {doc}`Listening across datasets <../../../../development/building_plugins/data/events/event_listener>`.

```{doxygenclass} mv::EventListener
:members:
```
