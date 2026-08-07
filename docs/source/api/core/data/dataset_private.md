# Dataset handle state

`DatasetPrivate` stores the identity and observed implementation behind `Dataset<T>`. It listens to core dataset events and re-emits changes as Qt signals. Plugin code normally interacts with it through `Dataset<T>` rather than constructing it directly.

```{doxygenclass} mv::DatasetPrivate
:members:
```
