# Parallel execution

ManiVault provides a small high-level API for scheduling work without manually constructing workflow plans. `mv::Parallel` covers one-off operations and collection processing, while `mv::ParallelExecutionChain` combines sequential and parallel stages into a readable pipeline.

These utilities are the recommended starting point for plugin and application developers. They run on the workflow framework, so callers receive structured results and can configure worker limits, notifications, profiling, and console reporting through `WorkflowOptions`.

```{note}
The high-level calls described here are blocking: they return after the scheduled operation has finished. Avoid calling them from a context that must remain responsive unless the surrounding design explicitly permits blocking.
```

## Start here

Read the getting-started page first, then choose the page matching the operation you need. The advanced workflow framework is available when the high-level API does not express the required scheduling or integration behavior.

```{toctree}
:maxdepth: 2

getting_started
running_operations
processing_collections
mapping_collections
execution_chains
options_and_cancellation
thread_safety
examples
../workflows/index
```

## API reference

For exact signatures, see the {doc}`parallel API reference <../../api/core/parallel/index>`. The underlying types are documented in the {doc}`workflow API reference <../../api/core/workflow/index>`.
