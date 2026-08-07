# AbstractPluginManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the plugins manager
mv::plugins().requestPlugin("PluginKind");
```

## Related
- Plugins {doc}`models <../models/plugins/index>`
- {doc}`Plugin communication and creation triggers <../../../development/building_plugins/communication/index>`

**Qualified name:** `mv::AbstractPluginManager`

```{doxygenclass} mv::AbstractPluginManager
:members:
:protected-members:
