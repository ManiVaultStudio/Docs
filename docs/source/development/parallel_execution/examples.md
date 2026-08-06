# Examples and recipes

## Collect indexed output with context-aware processing

Use `forEach()` when the callback needs an index or workflow context:

```cpp
std::vector<Result> results(inputs.size());

const auto outcome = mv::Parallel::forEach(
    "Compute results",
    inputs,
    [&results](Input& input, std::size_t index,
               const mv::workflow::SharedWorkflowExecutionContext& context) {
        context->info("Computing indexed result");
        results[index] = compute(input);
    });
```

Each callback writes a distinct result slot, so no container growth or shared-element mutation occurs concurrently.

## Prepare, process, and commit

```cpp
const auto result = mv::Parallel::stages("Rebuild cache")
    .run("Prepare cache", prepareCache)
    .forEach("Build cache entries", records, buildCacheEntry)
    .run("Commit cache", commitCache)
    .execute(options);
```

This pattern places explicit sequential barriers around independent parallel work.

## Transform immutable values

```cpp
const auto labels = mv::Parallel::map(
    "Format labels",
    values,
    [](const auto& value) {
        return formatLabel(value);
    });
```

Use `map()` when every input produces exactly one value and partial results are not required.

## When to step down a level

Use the {doc}`advanced workflow framework <../workflows/index>` for bounded batching, GUI-thread jobs, conditional success/failure/finalization stages, nested workflows, custom weights, or explicit published outputs.
