# AbstractPluginManager

Use the plugin manager to create and destroy managed plugin instances. It applies factory creation policy and performs the surrounding initialization and ownership work. See {doc}`Requesting plugin instances <../../../development/building_plugins/communication/requesting_plugins>` and {doc}`Plugin creation policy and instance limits <../../../development/building_plugins/creation_policy/index>`.

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
