# Threading and integration

## Updating from worker threads

The task mutation methods detect calls from a thread other than the task's Qt thread and queue the update to the owning thread. This makes progress reporting from workers possible. It also means the update is asynchronous: do not set a value from a worker and immediately read it back as synchronization.

Keep the task itself in a stable Qt thread, normally the GUI thread, and ensure it outlives every queued update. All members of a task hierarchy should share the same thread affinity.

The general QObject rules for connection contexts, queued delivery, event loops, and worker teardown are collected in {doc}`Qt plugin considerations <../qt_considerations/index>`.

Task thread-safety does not make plugin data thread-safe. Protect operation state independently and publish dataset changes on the correct thread. See {doc}`Thread safety <../../parallel_execution/thread_safety>`.

Avoid enabling `setAlwaysProcessEvents(true)` for ordinary plugin work. Processing GUI events inside progress updates introduces re-entrancy and is intended for exceptional code paths such as work before the main event loop starts.

## Dataset integration

Datasets expose an associated task through `dataset->getTask()`. Use it when progress describes an operation on that dataset:

```cpp
auto& task = dataset->getTask();
task.setRunningIndeterminate();
task.setProgressDescription("Rebuilding spatial index");

rebuildIndex(dataset);

task.setFinished();
```

The dataset task is tied to dataset presentation and lifetime. Do not retain a reference after the dataset may have been removed; guard long-running dataset operations with the same lifetime checks used for dataset handles.

## Notifications and the Tasks UI

Task GUI scopes determine normal presentation. If a particular operation also warrants a toaster that follows its live task state, use the task overload:

```cpp
mv::help().addNotification(QPointer<mv::Task>(&_task));
```

Do not construct an ordinary notification with `DurationType::Task`; that does not associate it with a task. Avoid presenting the same operation simultaneously through several intrusive channels unless each serves a distinct purpose.

## Moving to workflow-backed execution

The high-level `Parallel` helpers are the preferred entry point for common new operations. They use the workflow execution machinery internally, but their current blocking paths do not create a task. Consequently, reporting options alone do not add interactive task progress to those calls.

Use the task-backed workflow executor when interactive progress is required, or manage a task directly only if execution genuinely remains outside the workflow framework. See {doc}`Tasks and workflows <tasks_and_workflows>` for the integration boundary.
