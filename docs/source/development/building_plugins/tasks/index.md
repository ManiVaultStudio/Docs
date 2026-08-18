# Long-running operations and task progress

For new long-running operations, prefer ManiVault's workflow-backed execution facilities. Start with the high-level `Parallel` utilities for common operation shapes and move to a custom workflow plan when you need explicit stages, dependencies, thread affinity, structured results, or detailed reporting.

A `Task` is the presentation layer for progress and abort requests; it does not schedule or execute work. Manage one directly when execution already belongs to an external, legacy, or otherwise independently managed operation. A workflow can instead drive a task while remaining the authoritative owner of execution and outcome.

```{toctree}
:maxdepth: 1

choosing_an_execution_model
tasks_and_workflows
lifecycle_and_progress
cancellation
task_hierarchies
threading_and_integration
recipes_and_pitfalls
```

Start with {doc}`choosing_an_execution_model`. If the work is workflow-backed, continue with {doc}`tasks_and_workflows`; otherwise use the remaining pages to manage task reporting directly. For exact signatures and all signals, see the {doc}`Task API <../../../api/core/task/index>`.
