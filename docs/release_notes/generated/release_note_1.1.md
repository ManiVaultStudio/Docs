# Release 1.1

**Published:** 2024-11-11
**Upstream release:** https://github.com/ManiVaultStudio/core/releases/tag/v1.1

Installers for the most recent version of ManiVault can always be found on [manivault.studio/downloads](https://www.manivault.studio/downloads/).
All available installers are listed [here](https://github.com/ManiVaultStudio/Releases/releases).


## What's changed in version 1.1

### New
* Add learning page by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/611
* Plugin learning center by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/671, https://github.com/ManiVaultStudio/core/pull/694
* CMake find package by @alxvth in https://github.com/ManiVaultStudio/core/pull/619
* Add randomized point depth option to point renderer by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/632
* Add Images::getScalarData(std::uint32_t imageIndex, ...) overload for retrieving image scalar data in one operation by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/629
* Add project icon by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/636
* Add project selector to application startup by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/639
* Fine-grained plugins dependency loading by @alxvth in https://github.com/ManiVaultStudio/core/pull/692
* Generic view plugin sampler action by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/670
* Support project selection grouping serialization by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/641

### Improved
* Always use own zlib by @alxvth in https://github.com/ManiVaultStudio/core/pull/635
* Add zlib reference to help menu by @alxvth in https://github.com/ManiVaultStudio/core/pull/666
* Improve sample context exploration by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/679
* Improve startup project GUI by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/657
* Add dynamic cast to WidgetAction::findChildByPath(...) by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/650
* Add OpenGLWidget abstract convenience baseclass by @JulianThijssen in https://github.com/ManiVaultStudio/core/pull/684
* Update dependencies 08/24 by @alxvth in https://github.com/ManiVaultStudio/core/pull/672
* Separate version file by @alxvth in https://github.com/ManiVaultStudio/core/pull/661
* Edit status bar configuration by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/647
* Unlock/lock workspace layout from status bar for (published) projects by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/660

### Fixed
* Fix locking of GUI during publishing by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/644
* Fix qt6 deprecation warnings by @alxvth in https://github.com/ManiVaultStudio/core/pull/662, https://github.com/ManiVaultStudio/core/pull/664, https://github.com/ManiVaultStudio/core/pull/667
* Fix drag and drop problem and some drive-by changes by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/652
* Fix Font Awesome icons on Mac OS and Linux by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/654
* Fixes closing crash by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/649
* Fix ordered map warnings by @alxvth in https://github.com/ManiVaultStudio/core/pull/663
* Fix drag and drop problem and some drive-by changes by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/652
* Fix Font Awesome icons on Mac OS and Linux by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/654
* Remove linked data flag checking by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/626
* Fix macos bundling by @bldrvnlw in https://github.com/ManiVaultStudio/core/pull/682
* Fix non pch build by @alxvth in https://github.com/ManiVaultStudio/core/pull/685, https://github.com/ManiVaultStudio/core/pull/673
* Fix view plugin learning center toolbar bug by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/693
* Fix view plugin sampler action read-only by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/678
* Add missing Q_OBJECTs by @alxvth in https://github.com/ManiVaultStudio/core/pull/681
* Symlink to quazip lib should be relative by @alxvth in https://github.com/ManiVaultStudio/core/pull/674


**Full Changelog**: https://github.com/ManiVaultStudio/core/compare/v1.0...v1.1

