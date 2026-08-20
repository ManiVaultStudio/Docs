# Getting started

The high-level `Parallel` API is the normal entry point for workflow-backed execution. It builds and executes workflow plans for common operation shapes without requiring callers to manage stages and execution contexts directly.

Include the high-level API and call the operation that matches the shape of the work:

```cpp
#include <parallel/Parallel.h>
```

- `Parallel::run()` schedules one operation.
- `Parallel::forEach()` invokes a callback once per input item in parallel.
- `Parallel::map()` transforms items in parallel and returns ordered results.
- `Parallel::stages()` builds a pipeline containing sequential and parallel stages.

These collection helpers resemble parallel loops syntactically, but each item becomes a workflow job with result, reporting, cancellation, and scheduling semantics. They are best suited to coarse, independently meaningful items rather than tiny iterations in a numerical kernel. See {doc}`Intended scope and granularity <scope_and_granularity>`.

## A first collection operation

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

Stay with `Parallel` when the work is one operation, a homogeneous collection, a transformation, or a straightforward sequence of such phases. Move to the {doc}`advanced workflow framework <../workflows/index>` when you need custom stage policies, nested workflows, explicit job weights, GUI-thread affinity, published context values, task-backed interactive progress, or detailed lifecycle integration. Manage a standalone task only when execution is owned outside these workflow-backed paths; see {doc}`Choosing an execution model <../building_plugins/tasks/choosing_an_execution_model>`.

If the main problem is efficiently distributing a tight loop, vectorizing arithmetic, implementing a reduction, controlling cache-level partitioning, or using an accelerator, use a loop/kernel parallelization API or an optimized library. Such a kernel can run inside a workflow job when the surrounding application operation also needs workflow lifecycle features.
