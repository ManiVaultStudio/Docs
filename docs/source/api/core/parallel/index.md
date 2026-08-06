# Parallel execution

The parallel API is ManiVault's preferred high-level interface for scheduled and concurrent work. `Parallel` runs individual operations, processes or maps collections in parallel, and starts staged execution chains. `ParallelExecutionChain` combines sequential and parallel phases while leaving plan construction and executor integration to the underlying workflow framework.

Start with the {doc}`Parallel execution developer guide <../../../development/parallel_execution/index>` for examples, ownership rules, result handling, and thread-safety guidance. Use the {doc}`advanced workflow API <../workflow/index>` only when these high-level operations do not express the required execution model.

```{toctree}
:maxdepth: 1

parallel
parallel_execution_chain
```
