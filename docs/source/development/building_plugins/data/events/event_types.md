# Event types and payloads

Every dataset event has an `EventType`. Most concrete events carry the affected dataset through `DatasetEvent::getDataset()`; removal is the deliberate exception.

| Event type | Meaning | Relevant payload |
| --- | --- | --- |
| `DatasetAdded` | A dataset entered core ownership | Added dataset; the concrete event also exposes parent-name and visibility fields |
| `DatasetDataChanged` | General dataset content changed | Affected dataset |
| `DatasetDataDimensionsChanged` | Dimensional structure changed | Affected dataset |
| `DatasetDataSelectionChanged` | Dataset selection changed | Affected dataset |
| `DatasetAboutToBeRemoved` | Removal has begun, before destruction | Still-valid affected dataset |
| `DatasetRemoved` | Dataset implementation has been destroyed | Dataset GUID and `DataType`; no valid dataset handle |
| `DatasetChildAdded` | A child was attached | Parent dataset and child dataset |
| `DatasetChildRemoved` | A child was detached | Parent dataset and child GUID |
| `DatasetLocked` | Dataset became locked | Affected dataset |
| `DatasetUnlocked` | Dataset became unlocked | Affected dataset |

After checking `getType()`, cast to the matching concrete class when its additional payload is needed:

```cpp
if (event->getType() == mv::EventType::DatasetChildAdded) {
    auto* childAdded = static_cast<mv::DatasetChildAddedEvent*>(event);
    const auto parent = childAdded->getDataset();
    const auto child  = childAdded->getChildDataset();
    // Update hierarchy-dependent state.
}
```

Selection-change delivery is coalesced through the event manager's polling cycle and propagated to related or linked datasets. Code reacting to it should read the current selection rather than assume one notification per individual edit.

For the complete members of every concrete event, use the {doc}`event-types API page <../../../../api/core/data/events/event_types>`.
