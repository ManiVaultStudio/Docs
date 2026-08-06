# Running an operation

`Parallel::run()` schedules a single callable through the workflow executor and returns its `WorkflowResult`.

```cpp
const auto result = mv::Parallel::run("Build index", []() {
    buildIndex();
});
```

Use this entry point when one operation should participate in workflow reporting or share the same execution policy as other parallel utilities, but does not need a multi-stage plan.

## Result handling

The returned shared result describes how execution ended and contains collected diagnostics and metrics. Treat a returned result as an outcome to inspect; completion of the blocking call does not by itself mean the operation succeeded.

Exceptions escaping the callable are caught at the workflow job boundary and represented by the workflow failure machinery. Prefer actionable explicit diagnostics for expected failures and exceptions for violated contracts or failures naturally raised by a called API.

## Naming

Supply a short operation-oriented name. It is used for the workflow, stage, and job created by this convenience call and may appear in progress, logs, notifications, and result details.

For multiple phases, use an {doc}`execution chain <execution_chains>` rather than placing an entire pipeline inside one opaque callback.
