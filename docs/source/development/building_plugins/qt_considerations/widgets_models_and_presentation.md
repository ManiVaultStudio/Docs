# Widgets, models, and presentation

## Actions and widget representations

A ManiVault `WidgetAction` is long-lived state and behavior. Its widgets are disposable representations:

```cpp
void ExampleViewPlugin::init()
{
    auto* layout = new QVBoxLayout(&getWidget());
    layout->addWidget(
        _showLabelsAction.createWidget(&getWidget()));
}
```

Parent created widgets into the plugin's widget hierarchy. Do not delete an action because one of its widgets closes, and do not store an action-created widget as the authoritative setting. Multiple widgets may represent the same action.

When code must retain a widget that can close or be rebuilt independently, use `QPointer`. Prefer updating the action and letting every representation react over reaching into a particular checkbox, line edit, or combo box.

## Layout and widget ownership

A layout manages geometry, while its containing widget normally becomes the QObject parent of widgets added to it. Constructing a layout with the intended parent or installing it promptly avoids unparented intermediate widgets.

Do not install two layouts on one widget, reuse one widget in several layouts, or assume removing a widget from a layout deletes it. Decide whether a removed widget is reinserted, explicitly deleted, or deferred-deleted while its event loop is active.

## Model/view updates

Mutate a `QAbstractItemModel` in its affinity thread, normally the GUI thread when views consume it. Use the correct `beginInsertRows`/`endInsertRows`, removal, move, and reset protocol so views and proxy models do not retain invalid indices.

Do not pass a transient `QModelIndex` into asynchronous work. Capture stable domain identity, then find the current index when returning to the model thread. Use `QPersistentModelIndex` only when the model's documented operations preserve the needed identity.

The model, proxy model, selection model, and view have separate lifetimes. Give each an explicit owner and disconnect or clear sources before destroying a model that a surviving proxy or view still references.

## Themes, icons, and high DPI

Use palette roles, ManiVault actions, and `mv::util::StyledIcon` rather than hard-coded foreground and background colors. Re-polish or redraw custom widgets when the application theme changes, and verify both light and dark schemes.

Use device-independent layout sizes and scalable `QIcon` resources. Avoid caching a single low-resolution pixmap for all screens. When custom painting depends on physical pixels, account for the target device's device-pixel ratio.

For the framework icon conventions, see {doc}`Icons <../icons>`.

## OpenGL widgets

Create context-dependent resources in `initializeGL()` or while the intended context is current, not in the plugin constructor. Render only through the widget's OpenGL lifecycle, and perform explicit resource cleanup while a valid context is current when the resource wrappers require it.

Framebuffer dimensions may differ from logical widget dimensions on high-DPI displays. Use the OpenGL widget and current device-pixel ratio consistently for viewport, picking, and readback calculations. Never issue rendering commands from an arbitrary worker thread against the GUI widget's context.
