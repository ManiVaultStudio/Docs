# Application

`Application` is ManiVault's process-wide `QApplication` subclass. It provides startup configuration, application identity and version information, temporary directories, the application logger, workflow execution facilities, and access to the active Core implementation.

The executable creates this object. Plugins should use `mv::Application::current()` when application-level information is genuinely required and should use the typed accessors from `CoreInterface.h` for manager services.

The Core pointer exposed by the application is non-owning: `Application` connects to Core lifecycle signals and clears the pointer during teardown. Application startup metadata and actions are application integration concerns rather than ordinary plugin state.

**Qualified name:** `mv::Application`

## Related

- {doc}`CoreInterface <core_interface>`
- {doc}`Building applications <../../../development/building_applications/index>`

```{doxygenclass} mv::Application
:members:
:protected-members:
```
