# Processing collections

`Parallel::forEach()` creates one workflow job per item and runs those jobs in a parallel stage.

```cpp
const auto result = mv::Parallel::forEach(
    "Export datasets",
    datasets,
    [](const std::shared_ptr<Dataset>& dataset) {
        exportDataset(dataset);
    });
```

## Supported callback forms

The callback may accept any of these signatures:

```cpp
void(Item& item);
void(Item& item, std::size_t index);
void(Item& item, const mv::workflow::SharedWorkflowExecutionContext& context);
void(Item& item, std::size_t index,
     const mv::workflow::SharedWorkflowExecutionContext& context);
```

Use the index for stable positional output. Request the workflow context only when the callback needs advanced reporting, progress, or execution-state facilities; ordinary operations should use the smallest signature.

## Range ownership

The utility converts the supplied range into owned `std::vector` storage before scheduling:

- elements from an lvalue range are copied;
- elements from an rvalue range are moved;
- callbacks receive mutable references to the owned elements.

Consequently, mutating an item inside the callback does not mutate the original lvalue collection. If results must be returned to the caller, use `Parallel::map()`, write to explicitly shared output storage, or operate on copyable handles whose referenced objects are intentionally shared.

## Empty ranges

An empty range produces a parallel stage with no item jobs. Callers should not rely on callbacks running for validation or setup; perform those actions in a separate `run()` stage.
