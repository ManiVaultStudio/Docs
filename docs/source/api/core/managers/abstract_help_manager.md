# AbstractHelpManager

```cpp
// The core and its managers are located in this header
#include "CoreInterface.h"

// Use this global function to access the help manager
mv::help()->...
```

## Aggregated third-party licenses

`getThirdPartyLicensesModel()` returns the read-only `mv::ThirdPartyLicensesListModel` exposed by the help manager:

```cpp
const mv::ThirdPartyLicensesListModel& licenses =
    mv::help()->getThirdPartyLicensesModel();
```

The model combines Core license data with the `thirdPartyLicenses` metadata from available plugin factories, deduplicates matching dependencies, and records which plugins declare or currently use each dependency. Use `ThirdPartyLicensesFilterModel` when a view needs text, Core/plugin, or loaded-plugin filtering. The application presents the same aggregate through **Help → Third-party licenses**.

**Qualified name:** `mv::AbstractHelpManager`

```{doxygenclass} mv::AbstractHelpManager
:members:
:protected-members:
