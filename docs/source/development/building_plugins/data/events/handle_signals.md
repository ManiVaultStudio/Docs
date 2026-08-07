# Signals on a dataset handle

When a component already owns a `Dataset<T>` handle, its Qt signals are the simplest way to observe that dataset. The handle translates core events into signals and discards events belonging to other datasets.

```cpp
connect(&_points, &mv::Dataset<Points>::dataChanged,
        this, &ViewModel::refreshData);

connect(&_points, &mv::Dataset<Points>::dataSelectionChanged,
        this, &ViewModel::refreshSelection);

connect(&_points, &mv::Dataset<Points>::aboutToBeRemoved,
        this, &ViewModel::detachDataset);
```

Available handle signals cover:

- `dataChanged()` for changes to values or other general content;
- `dataDimensionsChanged()` when dimensional structure changes;
- `dataSelectionChanged()` when the selection changes;
- `childAdded(...)` and `childRemoved(...)` for hierarchy changes;
- `aboutToBeRemoved()` and `removed(datasetId)` for the two removal phases;
- `guiNameChanged()` for a display-name change;
- `changed(dataset)` when the handle itself is reset or points at another implementation.

Use the most specific signal available. For example, a dimensional change may require rebuilding controls, while an ordinary data change may only require repainting a view.

## Connection lifetime

Normal Qt connection rules apply. Supplying a receiver context, as in the examples above, disconnects the callback when that receiver is destroyed. The `Dataset<T>` object itself must also outlive connections made through its address; storing it as a member is the usual pattern.

Signals are notifications, not ownership. Check `isValid()` before dereferencing a handle whenever the callback may run after other event-loop or asynchronous work.
