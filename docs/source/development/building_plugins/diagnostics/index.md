# Notifications, logging, errors, and diagnostics

Good diagnostics separate the user-facing outcome from the evidence needed to understand it. Choose the least intrusive channel that matches the situation, preserve structured context as an error crosses layers, and present a failure only once at the owning boundary.

```{toctree}
:maxdepth: 1

choosing_a_channel
notifications_and_status
logging
exceptions
asynchronous_failures
troubleshooting
```

For exact signatures, see {doc}`notifications <../../../api/core/util/notifications/index>`, {doc}`exceptions <../../../api/core/util/exception/index>`, and the {doc}`error manager <../../../api/core/managers/abstract_error_manager>`.
