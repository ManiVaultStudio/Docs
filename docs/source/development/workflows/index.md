# Advanced workflow framework

The ManiVault workflow framework organizes multi-step operations into explicit plans containing stages and jobs. It provides the underlying execution model for sequential and parallel work, GUI-thread dispatch, nested workflows, progress aggregation, cancellation, diagnostics, metrics, and final results.

Most developers should begin with the {doc}`high-level parallel execution utilities <../parallel_execution/index>`. This advanced guide is for developers who need to construct custom workflow plans, integrate nested workflows, control execution contexts, or understand the scheduler's detailed behavior. For individual types and member signatures, use the {doc}`workflow API reference <../../api/core/workflow/index>`.

```{note}
In this section, *workflow* means the C++ execution framework in `mv::workflow`. It does not mean an informal end-user sequence of actions.
```

## Advanced path

Begin with the overview and concepts, then work through planning, execution, and results. The remaining pages are focused references for concurrency, nesting, cancellation, metrics, and framework supporting types.

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
framework_supporting_types
examples_and_recipes
testing
troubleshooting
```
