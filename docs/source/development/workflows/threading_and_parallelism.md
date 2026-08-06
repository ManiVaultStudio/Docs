# Threading and parallelism

## Thread affinity

Every job declares a `JobThreadAffinity`. Ordinary computational and I/O work should remain on a worker thread. Jobs that access Qt widgets or APIs requiring GUI-thread affinity must explicitly request GUI-thread execution. `WorkflowGuiThreadDispatcher` performs the boundary crossing used by the executor.

Keep GUI-thread jobs short. A long GUI job blocks input, painting, progress presentation, and potentially completion signals needed elsewhere in the workflow.

## Parallel stages

A parallel stage expresses independence, not merely a desire for speed. Before placing jobs in one, verify that they:

- do not depend on one another's outputs;
- do not mutate the same unsynchronized object;
- can be cancelled independently;
- produce deterministic aggregate results regardless of completion order.

Use sequential stages to establish barriers. Every later stage begins only after the previous stage satisfies its execution policy.

## Batching

Batching limits how much work is exposed to parallel scheduling at once. `WorkflowBatchingOptions` provides conservative defaults for operations such as dataset and block serialization, while a plan can supply a fixed or computed batch size.

Choose batches based on memory pressure and resource contention as well as CPU count. Jobs that each allocate a large buffer usually need smaller batches than lightweight CPU-only jobs.

## Parallelization options

`WorkflowParallelizationOptions` controls executor-wide parallel behavior. Keep policy in options rather than embedding environment-specific thread counts in plan construction. This makes workflows usable in interactive, testing, and headless contexts.

## Deadlock prevention

The highest-risk pattern is blocking the GUI thread while a pending workflow job requires that same thread. Prefer asynchronous root execution from GUI code. If blocking is unavoidable, ensure the plan contains no GUI-affine work and no signal/slot dependency that requires the blocked event loop.
