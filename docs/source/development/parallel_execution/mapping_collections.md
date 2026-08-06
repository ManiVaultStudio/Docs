# Mapping collections

`Parallel::map()` transforms every item concurrently and returns a `std::vector` of results.

```cpp
const auto squares = mv::Parallel::map(
    "Square values",
    std::vector<int>{ 1, 2, 3, 4 },
    [](int value) {
        return value * value;
    });
```

The returned vector contains `{1, 4, 9, 16}`. Results preserve input order even though jobs may finish in a different order.

## Return requirements

The mapping callable must return a non-`void` value. One optional result slot is allocated per input item; after successful execution, the slots are moved into the returned vector.

The current callback form receives the item only. If mapping requires an index or execution context, use `forEach()` with indexed output storage or construct an advanced workflow plan.

## Failures

`map()` must populate every result slot before constructing its return value. A failed workflow therefore does not yield a partial result vector through this convenience API. Use a lower-level workflow or an explicitly shared result structure when partial results are part of the intended contract.

As with `forEach()`, lvalue elements are copied and rvalue elements are moved into operation-owned storage.
