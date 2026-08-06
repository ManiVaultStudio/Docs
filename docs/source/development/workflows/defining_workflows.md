# Defining workflows

Create a `WorkflowPlan`, give it a descriptive name and context, then add stages in dependency order. The plan owns its stages; the executor consumes the plan through `UniqueWorkflowPlan`, making single-use ownership explicit.

## Choose a stage shape

Use a sequential stage when jobs depend on one another or touch state that cannot be accessed concurrently. Use a parallel stage only when every included job is independent under the documented synchronization rules. For a large homogeneous job set, use a batched parallel stage so concurrency and scheduling overhead can be bounded.

The principal construction helpers are:

- `addSequentialStage()` for one function or an ordered collection of jobs;
- `addParallelStage()` for independent jobs;
- `addBatchedParallelStage()` for bounded batches;
- `addNestedWorkflowStage()` for a child plan;
- `addParallelNestedWorkflowStage()` for independent child plans;
- `addOnSuccessStage()`, `addOnFailureStage()`, and `addFinalizationStage()` for lifecycle work.

## Give each unit one responsibility

Stage names should describe a phase, such as “Read metadata” or “Serialize datasets.” Job names should identify a concrete unit within that phase. Clear names are visible in progress trees, console dashboards, result details, and diagnostics.

## Weights

Stage and job weights express relative expected work, not percentages. For weights 1, 2, and 1, the units contribute 25%, 50%, and 25% of their parent. Zero-weight lifecycle stages are useful for short bookkeeping that should not distort visible progress.

Use stable estimates. Frequently changing weights during execution makes progress difficult to interpret and can appear to move backwards as the tree is rebalanced.

## Execution policies

`StageExecutionPolicy` controls how stage failure affects later work. `JobCompletionPolicy` and `JobProgressMode` control who marks a job complete and whether nested progress is treated atomically or exposed in detail. Prefer automatic completion for ordinary functions. Use manual or nested completion only when the job explicitly owns that lifecycle.

## Capture safely

Jobs may outlive the scope that creates the plan. Capture shared state by value or place it in the workflow context. Avoid references to stack variables unless blocking execution guarantees their lifetime. Parallel jobs must not mutate shared data without synchronization.
