# Execution

Execution types consume workflow plans, schedule their jobs, maintain root execution state, and expose synchronous or asynchronous completion. Callers should use the abstract executor contract rather than depend on the internal scheduling backend.

For the end-to-end lifecycle, see {doc}`Execution model <../../../../development/workflows/execution_model>`.

```{toctree}
:maxdepth: 1

abstract_workflow_plan_executor
workflow_execution_state
workflow_result_future
workflow_execution_notifier
```
