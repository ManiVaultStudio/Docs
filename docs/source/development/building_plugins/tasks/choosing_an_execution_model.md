# Choosing an execution model

Choose how the operation runs before choosing how its progress looks. A task is appropriate only after execution ownership is clear.

## Recommended path

| Need | Start with | Why |
| --- | --- | --- |
| One operation, collection processing, mapping, or a straightforward pipeline | {doc}`High-level Parallel utilities <../../parallel_execution/index>` | Concise workflow-backed execution with scheduling, aggregation, and structured results |
| Explicit stages, nested operations, GUI-thread jobs, custom weights, detailed diagnostics, or asynchronous lifecycle integration | {doc}`Workflow framework <../../workflows/index>` | Full control over planning, execution contexts, progress trees, results, and reporting |
| Execution is already owned by a library, service, worker, or established plugin implementation | Directly managed `Task` | Adds ManiVault progress presentation without replacing the existing executor |
| Small synchronous work with no meaningful wait | Direct function call | No execution framework or task is needed |

For new substantial operations, prefer one of the workflow-backed paths. The high-level `Parallel` utilities are the normal entry point into that machinery; a custom workflow plan is the advanced path, not a requirement for every loop.

## Why workflow-first

A workflow owns concerns that a task deliberately does not:

- scheduling and worker-thread execution;
- ordering, dependencies, and parallel stages;
- structured success, failure, and cancellation results;
- progress aggregation across jobs and nested operations;
- diagnostics, outputs, metrics, and finalization;
- asynchronous completion and execution lifetime.

A task contributes GUI scope, progress presentation, and an abort-request signal. Calling `setRunning()` never runs code or moves it off the GUI thread.

## When direct task management is appropriate

Manage a task directly when introducing a workflow would duplicate an executor that already owns the operation. Examples include a third-party API with its own asynchronous lifecycle, a process wrapper, or legacy worker code that is not yet being migrated.

The task object must remain alive for the entire operation. Store it as a plugin member, give it a longer-lived `QObject` owner, or use the task already owned by the dataset it describes.

## Choosing task presentation

Once direct task management is justified, choose the least intrusive presentation that still makes the operation understandable.

| Type | Use it for | Presentation |
| --- | --- | --- |
| `BackgroundTask` | Work that may continue without the user's attention | Aggregated with other background work and available through the task UI |
| `ForegroundTask` | Work the user initiated and is likely to watch | Appears automatically in the foreground task popup |
| `ModalTask` | Work during which continuing to interact with the application would be invalid | Blocks other interaction with a modal task dialog |
| `DatasetTask` | Work whose progress belongs to one dataset | Appears in the data hierarchy and as foreground progress |
| `Task` with `GuiScope::None` | Progress needed by code or custom observers, without an automatic dedicated presentation | Still observable by the task system |

Prefer `BackgroundTask` or `ForegroundTask` for ordinary plugin work. Use `ModalTask` only when other interaction would genuinely be invalid. For dataset work, use `dataset->getTask()` instead of creating an unrelated duplicate.

## Failure belongs to the execution result

`Task::Status` has no `Failed` value. A workflow records failure in its progress tree, reports, and final `WorkflowResult`; its associated task remains only a progress projection. For directly managed operations, preserve the error through a result or exception, return the task to a non-running state, and present the failure once at the owning boundary.

Do not encode failure as cancellation and do not leave a task running. See {doc}`Exceptions <../diagnostics/exceptions>` and {doc}`Asynchronous failures <../diagnostics/asynchronous_failures>`.

