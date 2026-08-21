# Project

`Project` represents the active analysis session and its project metadata. Its workflow-based serialization coordinates state from the relevant Core managers, including the data hierarchy, plugins, actions, and events.

Use {doc}`AbstractProjectManager <../managers/abstract_project_manager>` for creating, opening, importing, saving, and publishing projects. The manager owns the current project; callers should not delete it or retain its pointer across project replacement.

Plugins normally participate through their own serialization contract. They should not invoke `Project::fromVariantMapWorkflow()` or `Project::toVariantMapWorkflow()` directly.

**Qualified name:** `mv::Project`

## Related

- {doc}`Project persistence <../../../development/building_plugins/persistence/index>`
- {doc}`Workspace <workspace>`

```{doxygenclass} mv::Project
:members:
:protected-members:
```
