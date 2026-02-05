# Release 1.2

**Published:** 2025-01-22
**Upstream release:** https://github.com/ManiVaultStudio/core/releases/tag/v1.2

Installers for the most recent version of ManiVault can always be found on [manivault.studio/downloads](https://www.manivault.studio/downloads/).
All available installers are listed [here](https://github.com/ManiVaultStudio/Releases/releases).

## What's changed in version 1.2

### New
* Extend the current learning center API with tutorial functionality, added [several tutorials](https://www.manivault.studio/tutorials/) that can be opened from the start page, by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/738
* Implement and use proprietary file dialog class by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/735
* Add some comparison helpers by @alxvth in https://github.com/ManiVaultStudio/core/pull/731
* Add image mask functions by @alxvth in https://github.com/ManiVaultStudio/core/pull/732
* Add ability to select multiple options in options action in a single popup session by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/744
* Add element specifier getter to point data  by @alxvth in https://github.com/ManiVaultStudio/core/pull/758
* Add GUI name setter to DatasetImpl by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/724
* Add method to remove linked data by @alxvth in https://github.com/ManiVaultStudio/core/pull/730
* Add const getMap for SelectionMap by @alxvth in https://github.com/ManiVaultStudio/core/pull/754

### Improved
* Full support for learning center in view plugin hamburger menu by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/698
* Option to use native or Qt file dialog, default to native by @alxvth in https://github.com/ManiVaultStudio/core/pull/696
* Link statically to QuaZip by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/716
* Resolve linked data of all source datasets during selections by @alxvth in https://github.com/ManiVaultStudio/core/pull/713
* Highlight cluster selections by @alxvth in https://github.com/ManiVaultStudio/core/pull/727
* Implements two dataset(s) identifier copy modalities by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/742
* Reset the dock manager also for non view plugin dock widgets by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/739
* Run plugin manager dialog modal by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/751
* Several improvements to mv::gui::VersionAction and util::version in https://github.com/ManiVaultStudio/core/pull/767, https://github.com/ManiVaultStudio/core/pull/769, https://github.com/ManiVaultStudio/core/pull/771 by @ThomasKroes 

### Fixed
* Fix plugin destruction in https://github.com/ManiVaultStudio/core/pull/759, https://github.com/ManiVaultStudio/core/pull/764  by @ThomasKroes and @alxvth
* Fix manager destruction by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/728
* Fix plugin numbering by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/761
* Fix HTML rendering problems in sample scope plugin by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/709
* Several cmake fixes in  https://github.com/ManiVaultStudio/core/pull/714, https://github.com/ManiVaultStudio/core/pull/718, https://github.com/ManiVaultStudio/core/pull/719, https://github.com/ManiVaultStudio/core/pull/721 by @alxvth
* Fix malformed clusters crash by @alxvth in https://github.com/ManiVaultStudio/core/pull/725
* Fix inversion of selections of subsets by @JulianThijssen in 15ea0ad9bb4c23289735d469fb8e0a567f5c46bd, a136e05a4ccedb25c10acd969ea5f96faf7c98cd
* Fix toggle action drag and drop by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/723
* Fix crash on open project by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/733
* Fix zoom changes brush size by @alxvth in https://github.com/ManiVaultStudio/core/pull/765
* Fix recent projects not showing up after loading a project by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/740
* Properly restore floating view plugins from project by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/752
* Solves mv::gui::TriggerAction and mv::gui::ToggleAction scaling issues by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/746
* Only enable non-default presets in presets in presets manager dialog by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/755
* Fix plugin preset with data by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/756
* Prevent duplicate public action names by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/757
* Fix view plugin learning center overlay blocking the view plugin widget interaction by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/773

**Full Changelog**: https://github.com/ManiVaultStudio/core/compare/v1.1...v1.2

