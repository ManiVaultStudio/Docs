# Tasks and workflows

The workflow framework and task system occupy different layers:

```text
Workflow plan and executor
  -> schedule work, aggregate progress, preserve diagnostics and outcome
  -> project overall progress into a ManiVault Task
  -> present that Task through its GUI scope
```

The workflow result is authoritative. The task is a UI-facing projection that can disappear without erasing the structured execution result.

## Prefer one owner

When a workflow runs the operation, let its executor own progress aggregation, completion, failure reporting, and result construction. Job callbacks report through their `WorkflowExecutionContext`; they should not independently update a second task for the same work.

This keeps a single source of truth:

- workflow progress nodes track pending, running, completed, failed, and skipped work;
- the execution context aggregates progress and synchronizes it to an associated task;
- `WorkflowResult` retains status, messages, metrics, timings, and outputs;
- the task supplies the chosen GUI presentation.

## Executor-created task

For asynchronous root execution, enable workflow progress reporting in the execution options:

```cpp
mv::workflow::WorkflowOptions options;
options.reporting.progress = true;

auto future = executor.execute(std::move(plan), nullptr, options);
auto* task  = future.getTask();
```

In the current executor, this creates a modal GUI-scoped task and makes it available through `WorkflowResultFuture::getTask()`. The future must be retained so the caller can observe completion and keep any captured operation state alive. Do not create another foreground or modal task around this execution.

## Caller-supplied task

The blocking root executor overload accepts an existing task:

```cpp
mv::ForegroundTask task{this, "Import datasets"};
task.setRunning();

const auto result = executor.executeBlocking(
    std::move(plan),
    &task,
    options);
```

The execution context synchronizes aggregate workflow progress to the supplied task, and the executor completes its task presentation when execution ends. The caller owns the task and must keep it alive until `executeBlocking()` returns.

Inspect `result` to determine success or failure. A task cannot express the workflow's failed state, and a completed progress display does not by itself mean the workflow succeeded.

## Progress inside jobs

For an indivisible job, automatic progress is normally sufficient. For a long job with measurable internal work, report through its execution context:

```cpp
for (std::size_t index = 0; index < items.size(); ++index) {
    process(items[index]);
    context.setProgress(
        static_cast<double>(index + 1) /
        static_cast<double>(items.size()));
}
```

The context updates the workflow progress tree, which in turn updates the associated task. Direct calls to `task->setProgress()` would bypass that tree and make workflow reports disagree with the GUI.

## Cancellation and failure

Cancellation remains cooperative: jobs must check the workflow's shared cancellation state at safe boundaries and leave resources valid. A task abort control is a request, never forced thread termination. Use only an executor integration that explicitly connects the UI request to workflow cancellation; associating a task for progress alone should not be assumed to provide that connection.

Failures belong in the workflow context and result. Report or throw them through the workflow boundary so stage policy, failure branches, finalization, and diagnostics remain correct. Do not translate them into `Task::Aborted`.

See {doc}`Workflow progress and cancellation <../../workflows/progress_and_cancellation>` and {doc}`Workflow results and error handling <../../workflows/results_and_error_handling>`.

