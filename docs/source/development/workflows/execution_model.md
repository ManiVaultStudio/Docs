# Execution model

## Root execution lifecycle

A root execution follows these broad phases:

1. The caller submits an owned plan and `WorkflowOptions` to the executor.
2. The executor creates root report and progress nodes plus shared `WorkflowExecutionState`.
3. Main stages are compiled and run in plan order; jobs within a stage follow its concurrency mode.
4. The success or failure branch runs according to the main outcome.
5. Finalization runs to complete cleanup and reporting.
6. Progress, messages, metrics, outputs, status, and timings are assembled into a result.
7. Synchronous callers receive the result directly; asynchronous callers observe it through `WorkflowResultFuture`.

```text
Create execution state -> Run main stages -- success --> Run success stages --+
                                          \- failure --> Run failure stages --+--> Run finalization -> Publish result
```

## Blocking and asynchronous execution

`executeBlocking()` is appropriate when the caller deliberately waits and the selected thread affinities cannot deadlock that caller. `execute()` returns a future-like value for non-blocking integration. Do not discard an asynchronous future if the surrounding code must observe completion or preserve state required by captured jobs.

## Failure boundaries

The executor wraps job execution so exceptions and explicit job failures become workflow diagnostics and failed outcomes. A failure is not merely a log message: it participates in stage policy, later-stage eligibility, and the final result status. Conversely, warning messages do not necessarily fail a job.

## Ownership

Plans are uniquely owned and consumed for execution. Execution contexts and results are shared where multiple observers or nested operations need access. This prevents accidental plan reuse while allowing safe observation of a running or completed workflow.
