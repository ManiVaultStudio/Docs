# Building execution chains

An execution chain combines sequential `run()` stages and parallel `forEach()` stages without exposing `WorkflowPlan` directly.

```cpp
const auto result = mv::Parallel::stages("Import datasets")
    .run("Read metadata", []() {
        readMetadata();
    })
    .forEach("Decode datasets", datasets, [](Dataset& dataset) {
        decode(dataset);
    })
    .run("Publish results", []() {
        publishResults();
    })
    .execute();
```

Stages execute in the order they were appended. A `run()` stage contains one sequential job. A `forEach()` stage contains one parallel job per owned input item. The boundary between stages acts as a dependency barrier.

## Lazy, move-only construction

`ParallelExecutionChain` stores stage-building functions until `execute()` creates and submits the underlying workflow plan. A chain is move-only and execution is rvalue-qualified, encouraging this build-then-consume style. It is a single-use description; attempting to execute the same chain twice is an error.

## Composing chains

`then()` appends the stages from another chain:

```cpp
auto preparation = mv::Parallel::stages("Preparation")
    .run("Validate", validate);

auto processing = mv::Parallel::stages("Processing")
    .forEach("Transform", items, transform);

const auto result = std::move(preparation)
    .then(std::move(processing))
    .execute();
```

The receiving chain keeps its workflow name; `then()` transfers the other chain's stages.
