# Task

**Qualified name:** `mv::Task`

`Task` is the common state and progress model behind all task presentations. It reports an operation but does not execute it. Prefer workflow-backed execution for substantial new work; use a presentation-specific task directly when another component already owns execution. See the {doc}`practical execution and task guide <../../../development/building_plugins/tasks/index>`.

```{important}
`Task::Status` has no failed state. Preserve failures through the operation result, exception, or workflow context, and ensure the task no longer remains running.
```

```{doxygenclass} mv::Task
:members:
:protected-members:
```
