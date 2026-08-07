# Dataset

`Dataset<T>` is a typed, non-owning handle to a core-managed dataset. It tracks dataset identity, becomes invalid when the implementation is removed, and exposes dataset lifecycle and change events as Qt signals inherited from `DatasetPrivate`.

```{doxygenclass} mv::Dataset
:members:
```
