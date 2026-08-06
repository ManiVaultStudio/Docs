# Progress and cancellation

## Progress tree

`WorkflowProgressNode` represents a node in the workflow hierarchy. Parent progress is computed from child progress and relative weights. Nodes also carry status such as pending, running, completed, failed, or skipped, allowing dashboards to show more than a percentage.

Automatic progress is sufficient when a job is an indivisible unit: it becomes complete when the function returns successfully. For long jobs, report intermediate progress or nest a more detailed plan. Keep reported progress monotonic and bounded.

`WorkflowExecutionNotifier` can bridge overall workflow progress into a ManiVault `Task`, while `WorkflowConsoleDashboard` and `WorkflowConsoleFormatter` provide headless-friendly observation.

## Cooperative cancellation

Cancellation is cooperative. Requesting cancellation updates shared execution state; it cannot safely terminate arbitrary C++ code. Jobs must check cancellation at useful boundaries and return promptly while leaving owned resources valid.

Good check points include:

- before starting an expensive unit;
- between records, files, blocks, or batches;
- after a blocking API returns;
- before publishing output or committing a side effect.

Do not check so rarely that cancellation appears broken, or so frequently that synchronization overhead dominates tiny operations.

## Skipped work

When cancellation or stage policy prevents a planned node from running, it should be represented as skipped rather than completed. This distinction matters in result interpretation and progress visualization.

## Cleanup

Cancellation does not remove the need for cleanup. Use RAII for local resources and finalization stages for operation-level cleanup. Finalization code should itself be bounded and should not silently erase the original failure or cancellation reason.
