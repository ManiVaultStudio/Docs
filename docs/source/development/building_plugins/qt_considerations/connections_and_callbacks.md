# Connections and deferred callbacks

Qt connections are lifetime relationships. Make the receiver or context explicit whenever a callback captures plugin state.

## Always provide a context object

Prefer the overload that includes `this` as the context:

```cpp
connect(&_refreshAction, &mv::gui::TriggerAction::triggered,
        this, [this]() { refreshView(); });
```

Qt disconnects the functor when the sender or context is destroyed, and queued delivery follows the context object's thread affinity. Avoid a context-free lambda that captures `this`:

```cpp
// Unsafe if the sender outlives this plugin.
connect(sender, &Sender::ready,
        [this]() { consumeResult(); });
```

A safe context protects only that context. Any other raw pointer captured by the lambda still needs its own lifetime guarantee. Capture dataset handles, IDs, values, or `QPointer` guards instead of borrowed implementation pointers.

## Timers and delayed work

Use the context-bearing `QTimer::singleShot` overload:

```cpp
QTimer::singleShot(250, this, [this]() {
    if (_points.isValid())
        refreshView();
});
```

The callback is suppressed when the context is destroyed. A context-free delayed lambda that captures a plugin or widget can run after teardown.

For repeated work, store the timer with a clear owner and stop it when the plugin begins teardown. Do not use timer callbacks as a replacement for the workflow engine when the work is substantial or has dependencies, cancellation, or results.

## QPointer and stable identities

`QPointer<T>` becomes null when its QObject is destroyed:

```cpp
QPointer<QDialog> dialog = _detailsDialog;

QTimer::singleShot(0, this, [dialog]() {
    if (dialog)
        dialog->raise();
});
```

It is a lifetime guard, not a synchronization primitive. Another thread must not dereference it without respecting the object's affinity, and a successful check does not lock the object against simultaneous destruction.

For ManiVault datasets, capture `Dataset<T>` or a dataset ID and validate it when the callback runs. For hierarchy items and other manager-owned objects, perform a fresh lookup from a stable ID.

## Queued delivery during teardown

Automatic connection cleanup is necessary but not always sufficient. Stop timers, watchers, workers, and external producers at the beginning of the most-derived destructor. Disconnect sources that can emit during member destruction, especially when callbacks invoke derived-class behavior.

Avoid processing the event loop from a destructor. Re-entrancy can deliver queued work while the object is only partially alive. Assertions reporting that a called object is not of the correct type often indicate delivery after the derived portion has already been destroyed, and timing differences can make this appear on only one platform.
