# Teardown and testing

Destruction is a phase of the plugin lifecycle, not merely the last destructor call. Prevent new work first, then stop producers, then release consumers and UI.

## Teardown sequence

A useful order is:

1. Mark the component as stopping so new commands and callbacks decline work.
2. Request cancellation of owned external operations.
3. Stop timers, file watchers, sockets, and other signal producers.
4. Disconnect external senders whose delivery is not protected by this object as context.
5. Remove non-owning registrations and clear borrowed pointers.
6. Let child widgets and heap-owned QObjects follow their documented deletion path.
7. Let C++ members be destroyed in reverse declaration order.

```cpp
ExampleViewPlugin::~ExampleViewPlugin()
{
    _stopping = true;
    _refreshTimer.stop();

    disconnect(_externalService, nullptr, this, nullptr);
    _externalService = nullptr;
}
```

Declare members with destruction dependencies in mind. If member `A` uses member `B` during destruction, `B` must still be alive when `A` is destroyed; because members are destroyed in reverse declaration order, declare `B` before `A`.

## Plugin destruction

Use `Plugin::destroy()` or the owning core manager's lifecycle path. Do not call `delete this`, directly delete a core-owned plugin instance, or allow a worker to delete its plugin receiver.

Factories and plugin libraries normally remain loaded for the application session; plugin **instances** are the recurring destruction boundary. Do not rely on runtime library unloading to clean up static registrations or background callbacks.

Asynchronous completion must tolerate the plugin having disappeared. Prefer context-bound continuations, `QPointer`, and workflow scopes over raw `this` captures stored in external systems. A cancellation request does not itself prove that a worker has stopped.

## deleteLater()

Use `deleteLater()` only for a heap object whose affinity thread will continue processing events. Never call it on a QObject member or stack object.

Dialogs with `Qt::WA_DeleteOnClose` and worker objects connected to `QThread::finished` are common valid uses. Guard independently closing dialogs with `QPointer`. During application shutdown, prefer deterministic parent or C++ ownership where the event loop may already be stopping.

## Avoid shutdown deadlocks

Do not block the GUI thread waiting for a worker whose completion, cancellation, or destructor posts back to the GUI thread. Arrange asynchronous shutdown, or ensure the worker's stopping protocol has no GUI dependency before performing a bounded wait.

If a direct `QThread` is owned by the plugin, test and implement the case where destruction begins while it is running. A `QThread` object must not be destroyed while its underlying thread is still active.

## Verification checklist

Exercise Qt lifecycle behavior with:

- repeated plugin creation and destruction;
- project switching and bulk plugin teardown;
- a timer due while destruction begins;
- queued results arriving before, during, and after cancellation;
- independently closed dialogs and popups;
- datasets and hierarchy items removed before deferred callbacks run;
- a worker finishing after its originating view closes;
- application shutdown with active and cancelled work;
- model reset, row removal, and proxy/view teardown;
- light and dark theme changes while widgets are visible;
- normal and high-DPI screens, including moving a window between screens;
- Debug builds on Windows and Linux, where timing and assertions differ;
- sanitizers or memory diagnostics where supported by the toolchain.

Treat warnings such as `QObject::moveToThread` failures, missing queued meta-types, `QThread: Destroyed while thread is still running`, invalid model-index assertions, and “called object is not of the correct type” as lifecycle defects rather than harmless platform noise.

## Review questions

Before merging a QObject-based component, ask:

- Who owns each object, and can any API reparent or delete it?
- Which object is the context for every lambda connection and timer callback?
- In which thread is each QObject created, mutated, and destroyed?
- Can every queued argument cross the meta-object boundary safely?
- What happens if the project, dataset, view, or plugin disappears first?
- Does shutdown require an event loop that may no longer be running?
- Is displayed state authoritative, or can it be rebuilt from its real owner?
