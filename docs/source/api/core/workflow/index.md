# Workflow

The workflow API provides ManiVault's execution framework for structured, observable operations. A workflow plan describes sequential or parallel stages containing jobs; an executor runs that plan using hierarchical contexts, progress and reporting nodes, cooperative cancellation, and configurable threading behavior. Completed executions produce structured results containing status, diagnostics, metrics, and published values.

The pages below are a curated class-level reference. For architectural guidance, recommended patterns, and examples, see the {doc}`Workflow execution framework <../../../development/workflows/index>` guide.

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

