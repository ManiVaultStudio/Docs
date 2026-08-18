# Recipes and pitfalls

## Pick the simplest progress model

| Shape of work | Recommended model |
| --- | --- |
| Unknown duration | `RunningIndeterminate` |
| Known count or measurable fraction | `Manual` and `setProgress()` |
| Small fixed sequence | `Subtasks` |
| Independently observable child operations | Parent/child `Aggregate` tasks |

## Reusing a member task

Before a new run, call `reset()` to clear progress, subtask state, and descriptions, then configure the progress mode and start it. `reset()` does not itself select a status, so set `Running` or `RunningIndeterminate` explicitly.

Reject or serialize overlapping invocations that would try to drive the same task simultaneously. If concurrent runs are valid, give each run its own task and stable lifetime.

## Always close the lifecycle

Structure asynchronous completion so every path is accounted for:

| Outcome | Task action | Additional reporting |
| --- | --- | --- |
| Success | `setFinished()` | Usually none |
| User cancellation completed | `setAborted()` | Usually none |
| Failure | `reset()`, then `setIdle()` | Preserve and present the error at the owning boundary |
| Owner destroyed | Stop work and prevent queued callbacks from using the task | Log unexpected destruction if useful |

Because `Task` has no failed state, reusable operation code should document its convention if returning to `Idle` would be ambiguous. The essential rule is that the task must not remain running after the operation ends.

## Common mistakes

- Creating a task as a local variable and starting work that outlives it.
- Assuming `setRunning()` starts or threads the operation.
- Enabling cancellation without connecting `requestAbort()` to the work.
- Calling `setAborted()` immediately when cancellation is requested, before cleanup has completed.
- Treating a processing error as cancellation.
- Calling `setProgress()` while the task is in `Subtasks` or `Aggregate` mode.
- Using `0..100` with `setProgress()` instead of a fraction in `[0, 1]`.
- Giving parent and child tasks different thread affinities.
- Confusing the task hierarchy with `QObject` ownership.
- Leaving a task running on an exception or early return.
- Creating a second task for dataset work instead of using the dataset's task.
- Making routine work modal when foreground or background presentation is sufficient.

For debugging task behavior, observe `statusChanged`, `progressChanged`, and `requestAbort`, and inspect the Tasks plugin. Pair lifecycle evidence with the {doc}`diagnostics guide <../diagnostics/index>` when the operation also fails.
