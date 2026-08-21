# LoggingModel

**Qualified name:** `mv::LoggingModel`

`LoggingModel` presents the {doc}`structured message records <../../util/logging/message_record>` owned by the application logger. It checks for newly captured messages when the event dispatcher wakes and adds model rows without transferring ownership of the underlying records.

Application interfaces may use this model directly or place a {doc}`LoggingFilterModel <logging_filter_model>` in front of it. Plugin code normally emits Qt log messages instead of inserting model rows.

```{doxygenclass} mv::LoggingModel
:members:
:protected-members:
```
