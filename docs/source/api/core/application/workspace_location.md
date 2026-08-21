# WorkspaceLocation

`WorkspaceLocation` is a small value object returned by the workspace manager when enumerating discoverable workspaces. It combines a display title, file path, and location type.

The type distinguishes built-in workspaces, workspaces found on the configured global path, and recent workspaces. `WorkspaceLocation` describes a location; it is not the active `Workspace` and does not own workspace state.

**Qualified name:** `mv::WorkspaceLocation`

## Related

- {doc}`AbstractWorkspaceManager <abstract_workspace_manager>`
- {doc}`Workspace <workspace>`

```{doxygenclass} mv::WorkspaceLocation
:members:
```
