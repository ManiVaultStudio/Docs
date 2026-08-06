# Options, reporting, and cancellation

Every terminal high-level operation accepts a `mv::workflow::WorkflowOptions` value. For chains, pass it to `execute()`; for one-off operations, pass it as the final argument.

```cpp
mv::workflow::WorkflowOptions options;
options.reporting.finishedNotification = true;
options.execution.maxWorkerThreadCount = 8;

const auto result = mv::Parallel::forEach(
    "Analyze datasets",
    datasets,
    analyze,
    options);
```

The option bundle groups reporting, cancellation, batching, parallelization, and profiling policy. Prefer constructing it at the operation boundary so callbacks remain reusable and tests can select quieter or more deterministic behavior.

## Parallel execution

Set `options.execution.parallel` to `false` to restrict the executor to one worker, or use `maxWorkerThreadCount` to cap the worker pool. The cap is also limited by the hardware concurrency reported by the platform.

`forEach()` and `map()` create one equally weighted job per item, so the underlying workflow still records aggregate progress. Execution chains expose each stage and its jobs in the progress hierarchy.

## Reporting

Finished notifications, the console dashboard, logging depth, result-detail text, and profiling are configured through their respective option groups. The `reporting.progress` option controls task-backed GUI progress in executor paths that create or receive a ManiVault `Task`.

The high-level `Parallel` helpers currently use blocking execution without a task. Consequently, setting `reporting.progress` does not by itself create a progress dialog for these calls.

## Cancellation

Cancellation is cooperative and is driven by a task in the current workflow executor. The high-level blocking helpers do not supply a task, so `options.cancellation.enabled` does not provide user-driven cancellation for these calls. A callback may still honor an application-owned cancellation token captured explicitly by the caller.

Use the asynchronous or task-backed advanced workflow interface when the operation must expose ManiVault cancellation or interactive progress. For detailed option fields and cancellation semantics, see {doc}`Progress and cancellation <../workflows/progress_and_cancellation>` and the {doc}`WorkflowOptions API <../../api/core/workflow/planning/workflow_options>`.
