# Application, projects, and workspaces

These APIs describe the process-wide application, its access to Core services, the active analysis project, and the workspace used to arrange view plugins. They are primarily lifecycle and orchestration interfaces: plugin code normally consumes the active objects through Core accessors instead of constructing or owning them.

| Concept | Responsibility | Normal access |
|---|---|---|
| `Application` | Process-wide Qt application, startup state, temporary resources, and connection to the Core implementation | `mv::Application::current()` |
| `CoreInterface` | Lifecycle boundary and registry for Core managers | `mv::core()` and the typed manager accessors |
| `Project` | Metadata and serialized analysis state coordinated across managers | `mv::projects().getCurrentProject()` |
| `Workspace` | Layout-oriented workspace state, file identity, metadata, and locking | `mv::workspaces().getCurrentWorkspace()` |
| `AbstractWorkspaceManager` | Workspace I/O, view-plugin docking, layout operations, and workspace lifecycle signals | `mv::workspaces()` |
| `WorkspaceLocation` | Value describing a discoverable built-in, path-based, or recent workspace | Returned by the workspace manager |

## Project and workspace boundaries

A project represents the analysis session. Its workflow-based serialization coordinates state from the data hierarchy, plugins, actions, events, and project metadata. User-facing project operations belong to {doc}`AbstractProjectManager <../managers/abstract_project_manager>`; opening a project replaces the active project, while importing a project brings in data only.

A workspace is layout-oriented. `Workspace` stores its file identity and descriptive or locking actions, while `AbstractWorkspaceManager` manages the current workspace, view-plugin docking, layout restoration, previews, and workspace files. A workspace may be loaded when a project is created or opened, but project APIs allow that step to be omitted.

For task-oriented guidance, see {doc}`Project persistence <../../../development/building_plugins/persistence/index>` and {doc}`Building applications <../../../development/building_applications/index>`.

## Ownership and intended audience

- The executable creates the `Application` and concrete Core implementation.
- The Core implementation creates and exposes the managers represented by `CoreInterface`.
- Project and workspace managers expose the current `Project` and `Workspace`; callers must treat returned pointers as manager-owned and must not retain them across project or workspace replacement.
- Plugin developers normally use `mv::data()`, `mv::plugins()`, `mv::projects()`, `mv::workspaces()`, and the other typed accessors from `CoreInterface.h`.
- Implementing `CoreInterface` or a manager interface is application/Core integration work, not a normal plugin extension point.

```{toctree}
:maxdepth: 1

core_interface
application
project
workspace
abstract_workspace_manager
workspace_location
```
