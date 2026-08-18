# DatasetTask

**Qualified name:** `mv::DatasetTask`

`DatasetTask` associates progress with a dataset and exposes it through data-hierarchy and foreground presentation. Plugin code normally accesses the task already owned by a dataset through `dataset->getTask()`.

For dataset lifetime and progress guidance, see {doc}`Threading and integration <../../../../development/building_plugins/tasks/threading_and_integration>`.

```{doxygenclass} mv::DatasetTask
:members:
:protected-members:
```
