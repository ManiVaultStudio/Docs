# Workflow execution framework

The ManiVault workflow execution framework organizes multi-step operations into explicit plans containing stages and jobs. It provides a common execution model for sequential and parallel work, GUI-thread dispatch, nested workflows, progress aggregation, cancellation, diagnostics, metrics, and final results.

This guide explains the framework as a system: how its parts fit together, which guarantees callers can rely on, and how to choose among the available planning and reporting facilities. For individual types and member signatures, use the {doc}`workflow API reference <../../api/core/workflow/index>`.

```{note}
In this section, *workflow* means the C++ execution framework in `mv::workflow`. It does not mean an informal end-user sequence of actions.
```

## Recommended path

New users should begin with the overview and concepts, then work through planning, execution, and results. The remaining pages can be read as focused guides when a workflow needs concurrency, nesting, cancellation, metrics, or specialized utilities.

```{toctree}
:maxdepth: 2

overview
concepts
defining_workflows
execution_model
execution_context
threading_and_parallelism
nested_workflows
progress_and_cancellation
results_and_error_handling
reporting_and_profiling
workflow_utilities
examples_and_recipes
testing
troubleshooting
```
