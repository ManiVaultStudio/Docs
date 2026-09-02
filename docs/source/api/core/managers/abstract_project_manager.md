# AbstractProjectManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the project manager
mv::projects().saveProject(filePath);
```

## Opening published projects

Published projects open read-only by default. When the standard Open Project dialog detects a published project, it offers **Allow edit of published project**. The choice is represented by `ProjectOpenParameters::allowEditOfPublishedProject` and is applied after opening completes successfully.

Calls that supply a file path directly do not display this dialog and retain the default value, `false`. Treat editable opening as an explicit authoring operation rather than the normal published-project experience. See {doc}`Publishing a project <../../../development/building_applications/publishing_a_project>` for the user-facing workflow.

## Related
- Project {doc}`models <../models/projects/index>`
- {doc}`Project serialization and restoration <../../../development/building_plugins/persistence/index>`

**Qualified name:** `mv::AbstractProjectManager`

```{doxygenclass} mv::AbstractProjectManager
:members:
:protected-members:
```
