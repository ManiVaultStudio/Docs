# Lifecycle and progress

This page is for operations whose execution is managed outside the workflow framework. For new substantial operations, first follow {doc}`Choosing an execution model <choosing_an_execution_model>`. When a workflow owns the work, report progress through its execution context instead of manually driving a task.

## A minimal lifecycle

Create the task with stable ownership, configure it before starting work, and close every execution path with a non-running state.

```cpp
#include <ForegroundTask.h>

class MyAnalysisPlugin : public mv::plugin::AnalysisPlugin
{
public:
    MyAnalysisPlugin(const mv::plugin::PluginFactory* factory) :
        mv::plugin::AnalysisPlugin(factory),
        _task(this, "Computing embedding")
    {
    }

private:
    mv::ForegroundTask _task;
};
```

For determinate work, the normal sequence is:

```cpp
_task.reset();
_task.setDescription("Computes a two-dimensional embedding");
_task.setRunning();

for (std::size_t index = 0; index < items.size(); ++index) {
    process(items[index]);
    _task.setProgress(
        static_cast<float>(index + 1) / static_cast<float>(items.size()),
        QString("Processing item %1 of %2").arg(index + 1).arg(items.size()));
}

_task.setFinished();
```

`setProgress()` accepts values in `[0, 1]` and clamps values outside that range. `setFinished()` sets the displayed progress to complete. A root task returns to `Idle` shortly after finishing; observers that need to react to completion should use the status signals rather than poll for `Finished` later.

Use `RunningIndeterminate` when no meaningful denominator exists:

```cpp
_task.setProgressDescription("Waiting for the remote process");
_task.setRunningIndeterminate();
```

Switch to `Running` and report a fraction once the amount of work becomes known.

## Three progress modes

`Task` supports three mutually exclusive progress modes:

- `Manual` is the default. Call `setProgress()` with a fraction.
- `Subtasks` tracks a fixed list of logical steps and computes the fraction from completed steps.
- `Aggregate` derives progress and status from child tasks, weighted by each child's `weight`.

Use named subtasks when a job has a small, known sequence:

```cpp
_task.setSubtasks({"Read input", "Compute", "Store result"});
_task.setRunning();

_task.setSubtaskStarted("Read input");
readInput();
_task.setSubtaskFinished("Read input");

_task.setSubtaskStarted("Compute");
compute();
_task.setSubtaskFinished("Compute");

_task.setSubtaskStarted("Store result");
storeResult();
_task.setSubtaskFinished("Store result");
_task.setFinished();
```

Calling `setSubtasks()` selects `Subtasks` mode, so later calls to `setProgress()` have no effect until the mode is changed back to `Manual`. Likewise, adding a child task makes the parent aggregate its children.

## Names, descriptions, and progress text

- The task name identifies the operation and should remain concise.
- The description explains its purpose.
- The progress description identifies the current item or phase and may change frequently.
- The progress text is generated from state and progress; use `setProgressTextFormatter()` only when the standard text is insufficient.

Avoid updating progress for every element in a very tight loop. Report meaningful increments; `Task` coalesces its change signals, but unnecessary updates still add synchronization and formatting work.
