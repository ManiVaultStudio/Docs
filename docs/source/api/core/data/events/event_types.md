# Event types

`EventType` identifies dataset lifecycle and change events. The concrete event classes carry the dataset handle or stable removal information appropriate to each phase.

For a compact payload table and casting example, see {doc}`Event types and payloads <../../../../development/building_plugins/data/events/event_types>`.

```{doxygenenum} mv::EventType
```

```{doxygenclass} mv::ManiVaultEvent
:members:
```

```{doxygenclass} mv::DatasetEvent
:members:
```

```{doxygenclass} mv::DatasetAddedEvent
:members:
```

```{doxygenclass} mv::DatasetDataChangedEvent
:members:
```

```{doxygenclass} mv::DatasetDataDimensionsChangedEvent
:members:
```

```{doxygenclass} mv::DatasetDataSelectionChangedEvent
:members:
```

```{doxygenclass} mv::DatasetAboutToBeRemovedEvent
:members:
```

```{doxygenclass} mv::DatasetRemovedEvent
:members:
```

```{doxygenclass} mv::DatasetChildAddedEvent
:members:
```

```{doxygenclass} mv::DatasetChildRemovedEvent
:members:
```

```{doxygenclass} mv::DatasetLockedEvent
:members:
```

```{doxygenclass} mv::DatasetUnlockedEvent
:members:
```
