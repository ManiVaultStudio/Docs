# AbstractErrorManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the errors manager
mv::errors().getDebugStackTrace();
```

The error manager supplies application-level stack capture and error-logging configuration. Plugin failure-handling patterns are covered in {doc}`Notifications, logging, errors, and diagnostics <../../../development/building_plugins/diagnostics/index>`.

**Qualified name:** `mv::AbstractErrorManager`

```{doxygenclass} mv::AbstractErrorManager
:members:
:protected-members:
