# CoreInterface

`CoreInterface` is the abstract lifecycle and service boundary between the application and the Core managers. Plugin code usually includes `CoreInterface.h` and uses its typed convenience accessors rather than storing a `CoreInterface` pointer.

Common accessors include `mv::data()`, `mv::dataHierarchy()`, `mv::plugins()`, `mv::events()`, `mv::tasks()`, `mv::projects()`, and `mv::workspaces()`. They return Core-managed interfaces and are only valid while the application and Core are initialized.

Implementing this interface is application/Core integration work. Plugin developers should consume it, not subclass it.

**Qualified name:** `mv::CoreInterface`

## Related

- {doc}`Manager interfaces <../managers/index>`
- {doc}`Application <application>`

```{doxygenclass} mv::CoreInterface
:members:
:protected-members:
```
