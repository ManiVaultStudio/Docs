# AbstractSettingsManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the settings manager reference
mv::settings().getPluginGlobalSettingsGroupAction(...);
```

**Qualified name:** `mv::AbstractSettingsManager`

`AbstractSettingsManager` exposes the application's built-in settings groups and looks up global settings registered by plugin factories. Plugin-owned groups, defaults, and persistence are described in {doc}`Global plugin settings <../../../development/building_plugins/global_settings/index>`.

```{doxygenclass} mv::AbstractSettingsManager
:members:
:protected-members:
```
