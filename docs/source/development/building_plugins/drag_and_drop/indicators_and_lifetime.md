# Indicators, events, and lifetime

## Empty-state indicator

An optional indicator can advertise the drop target before a drag begins:

```cpp
_dropWidget->setDropIndicatorWidget(
    new DropWidget::DropIndicatorWidget(
        &getWidget(),
        "No data loaded",
        "Drag a points dataset here"));
```

`setDropIndicatorWidget()` reparents the indicator to the target widget. The drop widget hides it while regions are visible and restores it after the drag leaves or completes. Toggle it when the plugin's empty state changes:

```cpp
_dropWidget->setShowDropIndicator(!_points.isValid());
```

The indicator is only a visual cue. `setAcceptDrops(true)` and an initialized region callback are still required.

## Event sequence

`DropWidget` installs an event filter on its parent target and handles the interaction as follows:

1. On drag enter, it removes old regions, asks the callback for new ones, and accepts the proposed action when at least one region is returned.
2. On drag move, it highlights the region under the pointer.
3. On drop, it invokes the callback of the region under the pointer and removes all regions.
4. On drag leave, it removes all regions without invoking an operation.
5. On target resize, it resizes the overlay and indicator to match the target.

Region discovery may run for every new drag. Keep it fast and side-effect free: inspect handles and build presentation, but defer data conversion, computation, and publication until the user actually drops.

## Ownership

The objects have distinct lifetimes:

| Object | Lifetime and owner |
| --- | --- |
| Target widget | Owned by the plugin's normal Qt widget hierarchy |
| `DropWidget` | Child of the target widget |
| Drop indicator | Reparented to the target widget |
| `DropRegion` | Reparented to a temporary region container |
| Standard or custom region widget | Owned through the temporary container layout |
| Captured `Dataset<T>` | A non-owning, invalidation-aware handle to core-owned data |

Regions and their widgets disappear when the drag leaves or completes. Never store pointers to them. A callback can safely capture a dataset handle by value, but capturing unrelated raw objects is safe only when their lifetime is guaranteed by the drop target. Capturing `this` is appropriate when the `DropWidget` is a child of that same plugin widget and cannot outlive the plugin.
