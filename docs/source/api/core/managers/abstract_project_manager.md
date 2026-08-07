# AbstractProjectManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the project manager
mv::projects().saveProject(filePath);
```

## Related
- Project {doc}`models <../models/projects/index>`
- {doc}`Project serialization and restoration <../../../development/building_plugins/persistence/index>`

**Qualified name:** `mv::AbstractProjectManager`

```{doxygenclass} mv::AbstractProjectManager
:members:
:protected-members:
```
