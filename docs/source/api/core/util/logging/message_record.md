# MessageRecord

**Qualified name:** `mv::util::MessageRecord`

`MessageRecord` is the structured representation of one captured Qt log message. In addition to the message text and `QtMsgType`, it retains sequence, source-location, function, category, and format-version information for presentation and support diagnostics.

Records are owned by the application {doc}`Logger <logger>`. Consumers such as `LoggingModel` retain references to those records, so callers should not treat record pointers as independently owned objects.

```{doxygenstruct} mv::util::MessageRecord
:members:
```
