# Reporting, metrics, and profiling

`WorkflowReportingOptions` controls lifecycle messages, notifications, console reporting, and result presentation. `WorkflowProfilingOptions` controls timing and profiling behavior. They are grouped with cancellation and parallelization settings in `WorkflowOptions` so one execution policy can be passed at the root.

## Report tree

`WorkflowReportNode` mirrors execution hierarchy and records structured messages at their source. `WorkflowExecutionLifecycleScope` provides RAII-based start/finish reporting, ensuring lifecycle completion is recorded even when a scope exits exceptionally.

Use severity consistently:

- informational messages describe meaningful milestones or outcomes;
- warnings describe recoverable or degraded behavior;
- errors describe failed units;
- fatal errors describe failures that invalidate the overall operation.

## Metrics

`WorkflowExecutionMetrics` is the thread-safe accumulator used during execution. A `WorkflowMetric` is the immutable display-oriented value included in results and notifications. Metrics have a name, value, unit, and optional metadata.

Choose stable metric names and meaningful units. Counters such as processed records are integers; durations, rates, and ratios are typically floating point. Avoid high-cardinality names containing dataset IDs or file paths; place such context in metadata.

## Stage summaries

`WorkflowStageSummary` aggregates stage-level counts and timing for diagnostics and telemetry. It helps explain how parallel work behaved without requiring consumers to traverse every job result.

## Console presentation

`WorkflowConsoleFormatter` turns messages and progress snapshots into readable text. `WorkflowConsoleDashboard` periodically renders the current progress tree, and `WorkflowConsoleDashboardScope` manages its lifetime. These utilities are useful for tests, command-line operation, and debugging workflows without GUI task presentation.
