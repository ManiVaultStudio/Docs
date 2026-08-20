# Threads and the event loop

Every QObject has thread affinity. Queued slots and posted events execute in the object's affinity thread, provided that thread has a running event loop.

## GUI objects stay on the GUI thread

Create and mutate widgets, plugin actions used by widgets, GUI-facing models, selections, and OpenGL widgets on the GUI thread. Do computational and blocking I/O work elsewhere, then publish compact results back to the GUI thread.

For new plugin operations, prefer {doc}`workflow-backed execution <../tasks/choosing_an_execution_model>`. Workflow jobs declare worker or GUI affinity explicitly, and the executor performs the GUI-thread hand-off without making the plugin own a `QThread` lifecycle.

```cpp
QMetaObject::invokeMethod(
    this,
    [this, result = std::move(result)]() mutable {
        applyResult(std::move(result));
    },
    Qt::QueuedConnection);
```

Here `this` supplies both the destination thread and the lifetime context. Capture completed values, stable IDs, or handles—not worker-owned references.

## Connection types

With `Qt::AutoConnection`, delivery is direct when the receiver executes in the emitting thread and queued when it does not. A connection that was direct in a simple test can therefore become queued after an object moves or a signal originates from a worker.

Use an explicit connection type only when the contract requires it. Avoid `Qt::BlockingQueuedConnection` in plugin code: blocking the GUI thread while a worker waits for GUI work, or blocking a worker whose completion the GUI is awaiting, produces deadlocks.

Queued arguments must remain representable by Qt's meta-type system and are copied or moved for later delivery. Do not use a queued signal as proof that the underlying object referred to by a raw pointer remains alive.

## Moving QObjects

An object with a parent cannot be moved independently to another thread. Moving a parent also moves its children. Widgets cannot be moved away from the GUI thread.

If direct `QThread` integration is unavoidable for an externally owned executor, use a dedicated heap-allocated worker with no parent, retain the thread in a `QPointer<QThread>` member for teardown, move the worker before starting work, and arrange deletion in the worker thread:

```cpp
auto* worker = new ExternalWorker();
auto* thread = new QThread(this);

_workerThread = thread;

worker->moveToThread(thread);

connect(thread, &QThread::started,
        worker, &ExternalWorker::start);
connect(worker, &ExternalWorker::finished,
        thread, &QThread::quit);
connect(thread, &QThread::finished,
        worker, &QObject::deleteLater);
connect(thread, &QThread::finished,
        thread, &QObject::deleteLater);

thread->start();
```

This is only the beginning of a safe lifecycle: the plugin must request cancellation and ensure the worker cannot call back into a destroyed plugin. Do not parent the worker to the plugin and then call `moveToThread()`; the move will fail.

## Event-loop assumptions

`deleteLater()`, queued connections, timers, and posted events require the destination event loop to run. During startup and shutdown that assumption may not hold. Do not use `deleteLater()` for member QObjects, and do not rely on deferred deletion after the owning thread has stopped.

Never block the GUI event loop while waiting for work that may post a GUI-affine continuation. Prefer asynchronous completion and make plugin destruction an explicit cancellation boundary.

Thread affinity does not make shared data thread-safe. Follow the dataset's locking and notification contract and see {doc}`Parallel thread safety <../../parallel_execution/thread_safety>`.
