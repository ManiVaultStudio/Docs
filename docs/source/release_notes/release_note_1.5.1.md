# Release 1.5.1

**Published:** 2026-09-14
**Upstream release:** https://github.com/ManiVaultStudio/core/releases/tag/v1.5.1

Installers for the most recent version of ManiVault can always be found on [manivault.studio/downloads](https://www.manivault.studio/downloads/).
All available installers are listed [here](https://github.com/ManiVaultStudio/Releases/releases).

## Major changes
* Add parallel workflow utilities and cooperative cancellation by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1300
* Improve Sentry crash reporting, user feedback, and developer testing by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1306
* Add configurable point Z ordering and non-selectable point rendering by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1310

<details>
<summary>Additional changes</summary>

## Additions
* Add extractDataForDimension for subset point data by @alxvth in https://github.com/ManiVaultStudio/core/pull/1289
* Add heads-up display toggle for view plugins by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1311

## Fixed
* Fix: Icon not visible, show text instead by @alxvth in https://github.com/ManiVaultStudio/core/pull/1291
* Fix SampleScope visibility updates for widget-based sample views by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1294
* Prevent concurrent PointData access during workflow serialization by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1297
* Fix number of elements in subset point data serialization by @alxvth in https://github.com/ManiVaultStudio/core/pull/1298
* Fix random point selections after reopening projects by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1299
* Changes ColorAction to use native dialog on macOS by @thoellt in https://github.com/ManiVaultStudio/core/pull/1305
* Restore legacy PointData accessor behavior for backwards compatibility by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1302
* Continue restoring view plugins after individual state restoration failures by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1313
* Defer and coalesce dimension picker summary updates by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1314
* Restore project publishing with workflow-based serialization by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1316
* Run dataset `fromVariantMap()` on the GUI thread by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1318
* Improve view plugin state restore error handling by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1320
* Fix version variable scope in cmake helper by @alxvth in https://github.com/ManiVaultStudio/core/pull/1322
* lower case file names on windows by @alxvth in https://github.com/ManiVaultStudio/core/pull/1323
* PluginTriggerAction: copy enabled status in copy constructor by @alxvth in https://github.com/ManiVaultStudio/core/pull/1326
* Enable tooltips for view plugin menu actions by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1329
* Restore configurable BLOB storage location during project serialization by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1330
* Restore “Allow edit of published project” when opening projects by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1333
* Fix some apple clang warnings by @alxvth in https://github.com/ManiVaultStudio/core/pull/1308

## Miscellaneous
* Optimize guard selection restore with count check by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1303
* Refine PRE_EXCLUDE patterns for Apple and Linux by @alxvth in https://github.com/ManiVaultStudio/core/pull/1321

</details>

**Full Changelog**: https://github.com/ManiVaultStudio/core/compare/v1.5.0...v1.5.1

