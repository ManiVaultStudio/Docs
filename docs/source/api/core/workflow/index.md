# Workflow

The workflow API provides ManiVault's advanced execution framework for structured, observable operations. A workflow plan describes sequential or parallel stages containing jobs; an executor runs that plan using hierarchical contexts, progress and reporting nodes, cooperative cancellation, and configurable threading behavior. Completed executions produce structured results containing status, diagnostics, metrics, and published values.

Most developers should begin with the {doc}`parallel API <../parallel/index>` and the {doc}`Parallel execution <../../../development/parallel_execution/index>` guide. The pages below are the curated class-level reference for custom workflow plans and deeper framework integration. For architectural guidance, see the {doc}`Advanced workflow framework <../../../development/workflows/index>` guide.

## API areas

```{toctree}
:maxdepth: 2

planning/index
execution/index
context/index
progress/index
results/index
reporting/index
utilities/index
```
