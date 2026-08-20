# Designing drop regions

A drop region communicates one possible interpretation of the current payload. Return a single region for an unambiguous operation, or several regions when the same dataset can fill different roles.

```cpp
return {
    new DropWidget::DropRegion(
        _dropWidget,
        "Horizontal axis",
        "Use this dataset for the horizontal axis",
        "arrows-left-right",
        true,
        [this, points]() { setHorizontalDataset(points); }),
    new DropWidget::DropRegion(
        _dropWidget,
        "Vertical axis",
        "Use this dataset for the vertical axis",
        "arrows-up-down",
        true,
        [this, points]() { setVerticalDataset(points); })
};
```

The regions share the overlay equally. Use short titles and describe the result of dropping, not merely the input type.

## Rejection and explanation

Returning an empty list rejects the drag: no overlay regions are shown and the proposed drop action is not accepted. This is appropriate for unrelated MIME data and payloads that cannot be useful to the plugin.

Sometimes it is more helpful to explain why an otherwise relevant dataset cannot be used. A standard region can be rendered as unavailable:

```cpp
return {
    new DropWidget::DropRegion(
        _dropWidget,
        "Points required",
        "This operation needs a points dataset",
        "file-import",
        false)
};
```

```{important}
The `dropAllowed` constructor argument controls the standard region's presentation; `DropRegion::drop()` does not enforce it. An unavailable region must have no drop callback, or its callback must independently reject the operation.
```

Every callback should still assume that application state may have changed since the region was created. Recheck any condition whose failure could make the operation unsafe.

## Custom region widgets

Use the constructor that accepts a `QWidget*` when the standard title, description, and icon are insufficient:

```cpp
auto* preview = new DatasetDropPreviewWidget(points);

return {
    new DropWidget::DropRegion(
        _dropWidget,
        preview,
        [this, points]() { setPoints(points); })
};
```

The region container places the widget in its layout and owns it for the duration of the drag. Do not retain the preview widget or use it as persistent plugin state.

## One drag, multiple datasets

`DatasetsMimeData` can contain several handles. Decide explicitly whether the operation requires exactly one dataset, accepts the entire group, or offers one operation per compatible dataset. Avoid silently using `first()` without checking the count; hierarchy multi-selection makes that behavior surprising.

When accepting a group, validate every handle before showing an enabled region. Capture the validated handles by value in the callback so the operation receives the same logical inputs that were described to the user.
