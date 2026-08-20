# Thread safety and lifetime

Parallel utilities define scheduling; they do not synchronize application data automatically.

## Prefer independent items

The safest `forEach()` or `map()` callback reads immutable shared inputs and writes only to state owned by its current item or result slot. If callbacks update a shared counter, collection, cache, logger, or external library, verify that the operation is thread-safe and use appropriate synchronization.

## Qt object affinity

Do not access widgets from callbacks scheduled by these utilities. Most `QObject` instances also have thread-affinity constraints. Prepare data in parallel and apply it to the GUI through an established GUI-thread hand-off. Use the advanced workflow API when explicit job thread affinity is required.

## Captures

The call itself blocks, but callbacks execute on scheduled worker threads during that interval. References captured from the caller remain alive only if their owners outlive the complete call. Prefer value captures, shared ownership, or an explicit synchronized context over untracked raw references.

## Input ownership

Ranges are copied or moved into internal storage. This protects the scheduled jobs from the range object's lifetime, but it does not necessarily give exclusive ownership of what an element references. A copied pointer or dataset handle may still refer to shared mutable state.

## Oversubscription and resource pressure

One job is created per item. For very large collections or jobs with high memory use, external resource limits, or nested parallelism, the advanced workflow batching facilities may be more appropriate than the simple high-level collection operations.

When a workflow job calls code that uses OpenMP, oneTBB, a threaded numerical library, or another worker pool, both layers may create runnable work. Limit concurrency at one or both layers so that outer workflow jobs multiplied by inner workers do not oversubscribe the machine or multiply per-job memory use. Measure the combined configuration rather than tuning each layer independently.

Workflow cancellation is cooperative at workflow boundaries. It does not automatically stop an inner parallel runtime or third-party kernel; pass cancellation through when that API supports it, or let the kernel finish before the workflow job reaches its terminal state.
