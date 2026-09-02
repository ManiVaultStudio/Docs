# Release 1.5.0

**Published:** 2026-08-21
**Upstream release:** https://github.com/ManiVaultStudio/core/releases/tag/v1.5.0

Installers for the most recent version of ManiVault can always be found on [manivault.studio/downloads](https://www.manivault.studio/downloads/).
All available installers are listed [here](https://github.com/ManiVaultStudio/Releases/releases).

## Major changes
* Workflow-based project serialization and parallel execution by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1229
* Feature/extended coloring scatterplot by @thoellt in https://github.com/ManiVaultStudio/core/pull/1277
* Remove Release build and install steps by @alxvth in https://github.com/ManiVaultStudio/core/pull/1281
* Refactor workflow execution reporting and eliminate duplicate lifecycle messages by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1282
* Streamline workflow documentation by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1283
* Performance: speedup some methods in images plugin by @alxvth in https://github.com/ManiVaultStudio/core/pull/1264
* Adds an option for power/logarithmic scaling of the slider by @thoellt in https://github.com/ManiVaultStudio/core/pull/1257
* Add exception stack trace by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1259

<details>
<summary>Additional changes</summary>

## Additions
* Add missing serializations by @JulianThijssen in https://github.com/ManiVaultStudio/core/pull/1178
* Add CITATION.cff by @alxvth in https://github.com/ManiVaultStudio/core/pull/1179
* Add project version action to publish workflow by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1170
* Add invalidateFilter() to mv::gui::DatasetPickerAction by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1202
* Add findPluginAncestor to WidgetAction by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1205
* Add datasetAboutToBePicked signal and emit it by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1207
* Add ability to connect widget actions directly to view plugin actions from context menu by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1220
* Add reference getter to DatasetsMimeData by @alxvth in https://github.com/ManiVaultStudio/core/pull/1232
* Add `StandardPaths::getPluginDependenciesDirectory` by @alxvth in https://github.com/ManiVaultStudio/core/pull/1236
* Add data UI plugin readmes by @alxvth in https://github.com/ManiVaultStudio/core/pull/1243
* Plugin info for core plugins by @alxvth in https://github.com/ManiVaultStudio/core/pull/1244

## Fixed
* Move cursor override in publishProject by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1166
* Feature/fix leaking event listeners by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1177
* Prevents Customization directory from being created in the root directory by @JulianThijssen in https://github.com/ManiVaultStudio/core/pull/1171
* Fix project stale status for OSF-hosted projects (due to re-direction) by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1181
* Move cursor override in saveProject method by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1176
* Return value instead of local reference for Icon by @alxvth in https://github.com/ManiVaultStudio/core/pull/1184
* Update application name in About menu by @alxvth in https://github.com/ManiVaultStudio/core/pull/1185
* Single set file path call by @alxvth in https://github.com/ManiVaultStudio/core/pull/1188
* Fix project manager state update timing issues by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1189
* Set resize mode to contents for the HUD by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1191
* Fix compilation errors in ProjectsModelVisibilityController by @sbvis in https://github.com/ManiVaultStudio/core/pull/1197
* Discard fragments with zero opacity by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1199
* Fix linux actions editor by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1209
* Avoid creating view plugins twice while opening project by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1215
* Remove duplicate GradientCompute.frag resource by @alxvth in https://github.com/ManiVaultStudio/core/pull/1222
* Refactor override cursor sorting lambda to prevent crash by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1226
* Incorporate studio mode in widget action label state by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1227
* PointData problems with large data files bug fixed by @jeggermont in https://github.com/ManiVaultStudio/core/pull/1231
* Consistently use uint64_t in PointData by @alxvth in https://github.com/ManiVaultStudio/core/pull/1242
* Fixes issues for building the core standalone on macOS brought up in issue 1228 by @thoellt
* C++ version compile feature should be public for exported targets by @alxvth in https://github.com/ManiVaultStudio/core/pull/1233
* Improve theme switching robustness by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1266
* Fix plugin name regression by @alxvth in https://github.com/ManiVaultStudio/core/pull/1246
* Fix macOS notification visibility issue by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1280
* Improve notification link color contrast by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1268
* Follow common folder structure by @alxvth in https://github.com/ManiVaultStudio/core/pull/1269
* Restore action load order before plugin state restoration by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1271
* Fix corrupt viewers in saved project by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1274
* Restore DatasetPickerAction signal semantics by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1285
* Update child widget on button action changes by @thoellt in https://github.com/ManiVaultStudio/core/pull/1286
* Fix serialization of pinned view plugin dock widgets by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1287
* Fix nested plugintrigger title by @alxvth in https://github.com/ManiVaultStudio/core/pull/1288
* Add missing Qt headers by @alxvth in https://github.com/ManiVaultStudio/core/pull/1252
* Additional missing headers and points cmake typo by @thoellt in https://github.com/ManiVaultStudio/core/pull/1258
* Uses .icns file instead of lowres png to set icon on macOS (issue #1143) by @thoellt in https://github.com/ManiVaultStudio/core/pull/1251
* Do not use `using namespace mv` in headers by @alxvth in https://github.com/ManiVaultStudio/core/pull/1245
* Remove duplicate FILE_DIALOG_VERBOSE definition by @alxvth in https://github.com/ManiVaultStudio/core/pull/1250
* Optional PDB files in release mode for MSVC by @alxvth in https://github.com/ManiVaultStudio/core/pull/1240

## Miscellaneous
* Refactor suffix check for version string generation by @alxvth in https://github.com/ManiVaultStudio/core/pull/1164
* Decommission custom splash screen for published projects by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1168
* Ensure zlib builds with fPIC by @alxvth in https://github.com/ManiVaultStudio/core/pull/1186
* Temporarily disable the read-only logic for the option action by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1196
* Delegate view plugin requests in plugin manager by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1212
* Revamp navigation action linking by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1218
* Warnings as error by @alxvth in https://github.com/ManiVaultStudio/core/pull/1213
* Change navigationbar icon order by @alxvth in https://github.com/ManiVaultStudio/core/pull/1241
* Rely on hard-coded serialization name by @ThomasKroes in https://github.com/ManiVaultStudio/core/pull/1254
* CI: Use cache_variables for CMake options in `conanfile.py` by @alxvth in https://github.com/ManiVaultStudio/core/pull/1248

## Dependencies
* Seasonal dependency update 03/26 [zlib, valijson, ads & sentry] by @alxvth in https://github.com/ManiVaultStudio/core/pull/1221
* Update dependencies 2026/07 by @alxvth in https://github.com/ManiVaultStudio/core/pull/1256
* Update Qt to 6.9.3 by @alxvth in https://github.com/ManiVaultStudio/core/pull/1276
* Update Qt to 6.10.3 by @alxvth in https://github.com/ManiVaultStudio/core/pull/1278
* Update Quazip to 1.7.0 by @alxvth in https://github.com/ManiVaultStudio/core/pull/1247

</details>

**Full Changelog**: https://github.com/ManiVaultStudio/core/compare/v1.4.3...v1.5.0
