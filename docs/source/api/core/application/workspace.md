# Workspace

`Workspace` is the serializable value associated with the current layout-oriented workspace. It stores the workspace file path and exposes actions for locking, title, description, tags, and comments.

Use {doc}`AbstractWorkspaceManager <abstract_workspace_manager>` to create, load, save, and query workspaces or to manipulate view-plugin layout. The manager exposes the current workspace; callers should treat that pointer as manager-owned and should not retain it across workspace replacement.

The `Workspace` object stores workspace metadata and locking state. Docking and view-plugin layout operations remain responsibilities of the workspace manager.

**Qualified name:** `mv::Workspace`

## Related

- {doc}`Project <project>`
- {doc}`WorkspaceLocation <workspace_location>`

```{doxygenclass} mv::Workspace
:members:
:protected-members:
```
