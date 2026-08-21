# Logger

**Qualified name:** `mv::util::Logger`

`Logger` is the application-owned store behind ManiVault's global Qt message handler. It maintains structured {doc}`MessageRecord <message_record>` entries, provides synchronized access to them, and supports the models that present newly captured records in the interface.

Application startup initializes the logger. Plugin code should emit Qt log messages rather than construct or initialize another `Logger`. The record-access and mutex APIs primarily support Core presentation and integration code.

```{doxygenclass} mv::util::Logger
:members:
```
