# Overview

The workflow framework separates an operation's **description** from its **execution**. A `WorkflowPlan` describes stages and jobs. An `AbstractWorkflowPlanExecutor` runs that plan while a `WorkflowExecutionContext` exposes the current node's shared state, progress, reporting, outputs, and cancellation status. Execution produces a `WorkflowResult`, synchronously or through a `WorkflowResultFuture`.

This separation is useful when an operation must do more than invoke a function. A workflow can:

- run independent jobs concurrently while preserving stage ordering;
- move selected jobs to the GUI thread;
- embed another workflow and include its progress;
- aggregate progress using relative weights;
- propagate cancellation through the execution hierarchy;
- collect structured messages, metrics, outputs, and timing information;
- run cleanup regardless of whether the main stages succeeded.

## System at a glance

```text
Caller -> WorkflowPlan -> Workflow plan executor -> Execution contexts
                    ^                                |-- Progress tree
                    |                                |-- Report tree
              WorkflowOptions                       `-- Metrics and outputs

Workflow plan executor -> WorkflowResult / WorkflowResultFuture
```

The executor owns the scheduling details. Workflow code should express dependencies through stages and use the context for runtime interaction instead of coordinating threads directly.

## When to use it

Use a workflow when an operation has multiple observable steps, needs cancellation or progress, crosses thread boundaries, contains independent work, or must return structured diagnostics. A direct function call remains preferable for small, synchronous operations that need none of those facilities.

## Public and internal pieces

The types in `mv::workflow` form the reusable framework API. The current concrete executor is an internal Taskflow-based implementation. Callers should depend on `AbstractWorkflowPlanExecutor` and the public plan/context/result contracts rather than on Taskflow details.

See {doc}`Defining workflows <defining_workflows>` for plan construction and the {doc}`API reference <../../api/core/workflow/index>` for individual types.
