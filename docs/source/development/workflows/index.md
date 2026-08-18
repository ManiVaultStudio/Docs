# Advanced workflow framework

The ManiVault workflow framework is the primary execution mechanism for substantial new operations. It provides the underlying model for sequential and parallel work, GUI-thread dispatch, nested workflows, progress aggregation, cancellation, diagnostics, metrics, and final results.

Most developers should enter this machinery through the {doc}`high-level parallel execution utilities <../parallel_execution/index>`. This advanced guide is for developers who need to construct custom workflow plans, integrate task-backed progress, use nested workflows, control execution contexts, or understand the scheduler's detailed behavior. For individual types and member signatures, use the {doc}`workflow API reference <../../api/core/workflow/index>`.

A ManiVault `Task` is a presentation adapter for workflow progress, not an alternative execution engine. See {doc}`Tasks and workflows <../building_plugins/tasks/tasks_and_workflows>` for their relationship.

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
