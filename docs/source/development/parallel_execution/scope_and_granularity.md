# Intended scope and granularity

ManiVault's workflow engine coordinates **application operations**. Its parallelism is primarily task and stage parallelism: run independent, meaningful units concurrently while preserving dependencies, progress, cancellation, diagnostics, thread affinity, and a structured final result.

This is a different layer from APIs primarily used to parallelize the body of a loop or optimize a computational kernel.

## The intended unit of work

A good workflow job normally has application meaning and enough work to justify orchestration. Examples include:

- load or export one file;
- compute an analysis for one dataset or independent data block;
- run one stage of a multi-step transformation;
- prepare data on workers and apply a short result on the GUI thread;
- coordinate a request to an external service;
- execute a numerical kernel and capture its outcome as part of a larger operation.

These units benefit from being named, timed, cancelled, reported, inspected, or represented in progress UI. The workflow can retain those semantics whether a stage runs sequentially or exposes several independent jobs.

## What it is not intended to replace

The workflow engine is not primarily a replacement for:

- an OpenMP worksharing loop or task loop;
- `oneTBB::parallel_for`, `parallel_reduce`, or its concurrent containers;
- SIMD vectorization or accelerator offloading;
- fine-grained fork/join building blocks;
- an optimized numerical, image-processing, or machine-learning library's internal threading.

Those facilities operate closer to the computational loop, iteration space, memory layout, reduction, vector unit, or hardware target. They can partition very small units efficiently and expose controls that are deliberately outside the ManiVault workflow contract.

`Parallel::forEach()` and `Parallel::map()` may look like parallel-loop APIs, but they create workflow jobs. Use them for coarse collection items that deserve workflow lifecycle and reporting. Do not mechanically replace every ordinary `for` loop with them.

## Comparison by concern

| Concern | ManiVault workflow and `Parallel` utilities | OpenMP and oneTBB-style parallel algorithms |
| --- | --- | --- |
| Primary level | Application operations, stages, and observable jobs | Iteration spaces, kernels, tasks, and data-parallel algorithms |
| Typical unit | File, dataset, block, processing step, service request | Loop chunk, range partition, reduction body, small task |
| Main value | Dependencies, progress, cancellation, diagnostics, results, GUI affinity | Efficient work distribution, locality, reductions, vectorization, scalable algorithms |
| Application integration | Built into ManiVault tasks, reporting, options, and result handling | Supplied by the surrounding application |
| Best fit | Long-running or operational work that users or developers need to observe | Performance-sensitive computation close to the data |

The boundary is not absolute. OpenMP supports tasks as well as loops, and oneTBB includes a flow-graph API in addition to parallel algorithms. Those features can overlap with general task-graph scheduling. ManiVault's reason for adding its workflow layer is the application-specific execution contract around the work, not the claim that other runtimes cannot express dependencies.

## Complementary use

A workflow job may call a function that internally uses OpenMP, oneTBB, a GPU API, or a threaded third-party library:

```cpp
const auto result = mv::Parallel::run(
    "Compute embedding",
    [&input, &output]() {
        computeEmbeddingWithOptimizedBackend(input, output);
    });
```

Here the optimized backend owns kernel-level parallelism. The workflow owns the application-level operation: when it runs, how it is reported, how its outcome is represented, and how it composes with earlier and later stages.

The reverse composition can also be valid: a larger application may use another scheduler and invoke a blocking ManiVault workflow as one coarse operation, provided thread affinity and worker-pool interactions are understood.

## Avoid accidental nested parallelism

Combining layers requires an explicit concurrency policy. If a workflow runs eight jobs and each job starts eight inner workers, the application may expose 64 runnable workers plus their memory allocations. This can reduce performance and responsiveness rather than improve them.

Choose one of these strategies and measure it:

- use workflow parallelism across jobs and configure inner kernels to run sequentially or with few workers;
- run fewer workflow jobs concurrently and let each optimized kernel use the machine;
- batch small items into coarse workflow jobs, then parallelize inside each batch;
- reserve GUI-thread jobs for short application updates, never for a long inner parallel kernel.

Cancellation, progress, and diagnostics also stop at the boundary unless explicitly adapted. A workflow can request cancellation, but an inner runtime continues until it cooperates or returns. Likewise, kernel-internal progress is not automatically visible in the workflow report.

## Decision guide

Use the workflow layer when the answer to one or more of these questions is yes:

- Does the operation have stages, dependencies, cleanup, or a structured result?
- Should users see progress, cancellation, warnings, or failure details?
- Must some work cross between worker and GUI threads?
- Does the operation need to compose with other ManiVault execution?

Use a loop/kernel parallelization facility when the main question is how to divide a computational iteration space efficiently. Use both when a meaningful ManiVault operation contains a performance-sensitive kernel.

For the mechanics of combining worker pools safely, continue with {doc}`Thread safety and lifetime <thread_safety>`. For custom stages and execution policies, see the {doc}`advanced workflow framework <../workflows/index>`.

## Related external models

- The [OpenMP worksharing-loop construct](https://www.openmp.org/spec-html/5.2/openmpse66.html) distributes loop iterations among a thread team.
- The [oneTBB `parallel_for` guide](https://uxlfoundation.github.io/oneTBB/main/tbb_userguide/parallel_for_os.html) describes partitioning an iteration space into chunks.
