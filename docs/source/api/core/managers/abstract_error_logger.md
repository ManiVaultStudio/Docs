# AbstractErrorLogger

**Qualified name:** `mv::AbstractErrorLogger`

`AbstractErrorLogger` is the application-side base class for an optional error-reporting backend. It receives eligible handled exceptions and user feedback from {doc}`AbstractErrorManager <abstract_error_manager>`, and it follows the global opt-in and enablement settings exposed by that manager.

This is an application integration point, not the routine logging API for plugins. Plugin code should use Qt logging for diagnostic evidence and report user-visible failures at the boundary that owns the operation. See {doc}`Notifications, logging, errors, and diagnostics <../../../development/building_plugins/diagnostics/index>` for that decision model.

Concrete backends implement initialization, startup, shutdown, and DSN validation. Initialization is deliberately divided into `beginInitialization()` and `endInitialization()` so the base class can connect shared settings and track readiness around backend-specific setup.

```{doxygenclass} mv::AbstractErrorLogger
:members:
:protected-members:
```
