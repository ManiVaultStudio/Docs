# AbstractWorkspaceManager

`AbstractWorkspaceManager` is the Core-managed interface for workspace lifecycle and view layout. It creates, loads, saves, and enumerates workspaces; manages docking and isolation of view plugins; produces workspace previews; and reports lifecycle changes through Qt signals.

Plugin code accesses the active implementation through `mv::workspaces()`. Subclassing this interface is application/Core integration work rather than a normal plugin extension point.

`loadWorkspaceWorkflowPlan()` constructs a workflow plan without executing it. This allows framework code to compose workspace restoration into a larger project or application workflow while retaining progress, cancellation, and reporting behavior.

**Qualified name:** `mv::AbstractWorkspaceManager`

## Related

- {doc}`Workspace <workspace>`
- {doc}`WorkspaceLocation <workspace_location>`
- {doc}`Parallel execution guide <../../../development/parallel_execution/index>`

```{doxygenclass} mv::AbstractWorkspaceManager
:members:
:protected-members:
```
