# Getting started

The high-level `Parallel` API is the shortest route into workflow-backed execution when direct synchronous code is no longer sufficient. It builds and executes plans for common operation shapes without requiring callers to manage workflow stages and execution contexts directly.

Using it is a design choice, not a framework requirement. Keep direct code for work that completes quickly and does not need scheduling or a structured execution result. Standard action serialization is one common example that normally remains synchronous.

Include the high-level API and call the operation that matches the shape of the work:

```cpp
#include <parallel/Parallel.h>
```

- `Parallel::run()` schedules one operation.
- `Parallel::forEach()` invokes a callback once per input item in parallel.
- `Parallel::map()` transforms items in parallel and returns ordered results.
- `Parallel::stages()` builds a pipeline containing sequential and parallel stages.

## A first scheduled operation

Use `run()` when one self-contained operation should execute through the workflow executor and the caller is allowed to wait:

```cpp
const auto result = mv::Parallel::run(
    "Compute density",
    [&dataset]() {
        computeKernelDensity(dataset);
    });

if (!result ||
    result->getStatus() != mv::workflow::WorkflowResultBase::Status::Success) {
    // Handle failure or cancellation at the operation boundary.
}
```

The callable is scheduled as workflow work, but `run()` itself is blocking. If the user must continue interacting with the application and observe live progress, start with the {doc}`advanced workflow framework <../workflows/index>` instead of wrapping the operation in a blocking UI callback.

## A first parallel collection

```cpp
std::vector<QString> files = filesToImport();

const auto result = mv::Parallel::forEach(
    "Import files",
    files,
    [](const QString& file) {
        importFile(file);
    });

if (!result ||
    result->getStatus() != mv::workflow::WorkflowResultBase::Status::Success) {
    // Handle the failed or cancelled operation.
}
```

The range is owned by the scheduled operation: an lvalue range is copied and an rvalue range is moved into internal storage. The call blocks until every scheduled job reaches a terminal outcome.

```{important}
Parallel scheduling does not make the callback or the objects it accesses thread-safe. Items may be processed concurrently, so shared mutable state must be synchronized or avoided.
```

## Choosing the right level

Stay with `Parallel` when the work is one operation, a homogeneous collection, a transformation, or a straightforward sequence of such phases and the caller may block. Move to the {doc}`advanced workflow framework <../workflows/index>` when you need asynchronous execution, custom stage policies, nested workflows, explicit job weights, GUI-thread affinity, published context values, task-backed interactive progress, or detailed lifecycle integration. Manage a standalone task only when execution is already owned outside these workflow-backed paths; see {doc}`Choosing an execution model <../building_plugins/tasks/choosing_an_execution_model>`.

The collection helpers resemble parallel loops syntactically, but each item becomes a workflow job with result, reporting, cancellation, and scheduling semantics. They are best suited to coarse, independently meaningful items rather than tiny iterations in a numerical kernel. If the main problem is efficiently distributing a hot loop, use a loop/kernel parallelization API or an optimized library. Such a kernel can still run inside a workflow job when the surrounding application operation needs workflow lifecycle features. See {doc}`Intended scope and granularity <scope_and_granularity>` for the detailed boundary.
