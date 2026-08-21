# Logging

ManiVault installs a global Qt message handler that turns diagnostic output into structured {doc}`MessageRecord <message_record>` entries held by {doc}`Logger <logger>`. The {doc}`logging models <../../models/logging/index>` expose those records to application interfaces for display, filtering, and sorting.

Plugin code normally writes through Qt's `qDebug()`, `qInfo()`, `qWarning()`, and `qCritical()` functions. It should not append records to the global logger or manipulate the presentation models directly. See {doc}`Logging diagnostic evidence <../../../../development/building_plugins/diagnostics/logging>` for severity selection, useful context, and privacy guidance.

## Logging and error reporting are different paths

This logger records local diagnostic messages. Optional reporting of handled exceptions or crashes is coordinated by {doc}`AbstractErrorManager <../../managers/abstract_error_manager>` and a consent-aware {doc}`AbstractErrorLogger <../../managers/abstract_error_logger>` backend. Writing a Qt log message does not replace user-facing error handling, and it should not be treated as an instruction to send telemetry.

```{toctree}
:maxdepth: 1

message_record
logger
```
