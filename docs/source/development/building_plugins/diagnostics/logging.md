# Logging diagnostic evidence

Use Qt logging for information intended primarily for developers and support. Match severity to operational meaning:

- `qDebug()` for verbose development detail;
- `qInfo()` for noteworthy normal lifecycle events;
- `qWarning()` for recoverable unexpected conditions;
- `qCritical()` for serious failures that leave an operation unusable.

```cpp
qWarning() << "Unable to restore optional view setting"
           << "plugin=" << getKind()
           << "key=" << settingKey
           << "reason=" << exception.what();
```

Prefer stable labels and identifiers over prose-only messages. Include enough context to correlate related events, but do not log entire datasets, authentication material, private URLs, or arbitrary serialized maps.

## Log once at the useful layer

Repeatedly logging the same exception at every catch-and-rethrow point produces noise without new evidence. Add context when crossing an abstraction boundary, then either rethrow or handle it. Log at a boundary only when that boundary will consume the failure.

Avoid using logs as invisible user feedback. If the user must change an input or retry an action, provide an appropriate notification, validation state, workflow result, or dialog as well.

The logging models expose collected application logs to ManiVault interfaces; plugin code normally writes through Qt rather than manipulating those models directly.

For exact types and ownership, see the {doc}`Core logging API <../../../api/core/util/logging/index>`. Optional handled-exception and crash reporting is a separate, consent-aware application facility described by {doc}`AbstractErrorManager <../../../api/core/managers/abstract_error_manager>` and {doc}`AbstractErrorLogger <../../../api/core/managers/abstract_error_logger>`.
