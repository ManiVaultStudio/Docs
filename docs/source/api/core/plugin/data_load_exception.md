# DataLoadException

**Qualified name:** `mv::plugin::DataLoadException`

`DataLoadException` represents failure to load a particular file. Its `what()` text combines the file path with the technical reason, allowing the UI boundary that owns the load operation to present or record a useful cause.

Throwing the exception does not itself notify the user. Catch or propagate it through the execution mechanism that owns the loader operation, following the {doc}`diagnostics guidance <../../../development/building_plugins/diagnostics/index>`. Avoid duplicating the same failure in a log, notification, and dialog.

```{doxygenstruct} mv::plugin::DataLoadException
:members:
```
