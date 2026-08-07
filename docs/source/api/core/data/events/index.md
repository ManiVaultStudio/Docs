# Dataset events

The dataset event API broadcasts lifecycle, content, dimensional, selection, hierarchy, and locking changes. `Dataset<T>` translates these events into per-handle Qt signals; `EventListener` supports broader observation and filtering.

For recommended subscription and removal patterns, see {doc}`Events and dataset lifetime <../../../../development/building_plugins/data/events_and_lifetime>`.

```{toctree}
:maxdepth: 1

event_listener
event_types
```
