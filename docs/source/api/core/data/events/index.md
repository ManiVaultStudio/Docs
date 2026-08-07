# Dataset events

The dataset event API broadcasts lifecycle, content, dimensional, selection, hierarchy, and locking changes. `Dataset<T>` translates these events into per-handle Qt signals; `EventListener` supports broader observation and filtering.

Start with the {doc}`developer guide <../../../../development/building_plugins/data/events/index>` to choose between per-handle signals and a broad listener. The pages below provide the exact API after that choice is clear.

```{toctree}
:maxdepth: 1

event_listener
event_types
```
