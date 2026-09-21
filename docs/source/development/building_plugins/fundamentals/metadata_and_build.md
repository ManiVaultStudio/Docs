# Metadata and build integration

Plugin information is split between `PluginInfo.json`, Qt's plugin declaration, and the factory's runtime metadata.

## `PluginInfo.json`

Place `PluginInfo.json` beside the plugin target's `CMakeLists.txt` and make it available to the target that contains the exported factory.

```json
{
  "name": "Example View",
  "version": {
    "plugin": "1.0.0"
  },
  "type": "View",
  "dependencies": [],
  "thirdPartyLicenses": [
    {
      "name": "Example dependency",
      "license": "MIT",
      "url": "https://example.org/license"
    }
  ]
}
```

`name` identifies the library, and `version.plugin` is its semantic version. `mv_handle_plugin_config()` requires both values, appends the plugin and ManiVault core versions to the output library name, and uses the optional top-level `type` only to group targets in generators that support folders. `dependencies` records plugin dependencies for the surrounding plugin tooling. `thirdPartyLicenses` records the third-party libraries shipped or used by the plugin so ManiVault can show their license information together with Core and other available plugins.

Each `thirdPartyLicenses` entry must be an object with a non-empty `name` and `license`; `url` is the link to the dependency or its license information and may be empty when no link is available. The field is optional, and an empty array is valid. Keep one entry per dependency and use the license identifier or name that the dependency publishes (for example, `MIT`, `MPL-2.0`, or `BSD-3-Clause`).

Do not add a manually maintained `version.core` value for `mv_handle_plugin_config()`: the helper obtains the current core version from CMake.

## Qt declaration

The exported factory declares the Qt interfaces and embeds the JSON metadata:

```cpp
class ExampleViewPluginFactory final : public mv::plugin::ViewPluginFactory
{
    Q_OBJECT
    Q_INTERFACES(mv::plugin::ViewPluginFactory mv::plugin::PluginFactory)
    Q_PLUGIN_METADATA(IID  "studio.manivault.ExampleViewPlugin"
                      FILE "PluginInfo.json")

    // ...
};
```

Use a stable, unique IID. Renaming it later can break discovery and compatibility assumptions.

## Runtime metadata

Populate user-facing metadata in the factory constructor. The core uses it for discovery, help, and automatically generated about information.

```cpp
auto& metadata = getPluginMetadata();
metadata.setDescription("Shows an example visualization");
metadata.setSummary("Displays point datasets in an interactive view.");
metadata.setCopyrightHolder({ "Example Institute" });
metadata.setAuthors({
    { "A. Developer", { "Developer" }, { "EX" } }
});
metadata.setOrganizations({
    { "EX", "Example Institute", "https://example.org" }
});
metadata.setLicenseText(
    "Distributed under the [LGPL v3.0](https://www.gnu.org/licenses/lgpl-3.0.html)."
);
```

Override `getRepositoryUrl()`, `getReadmeMarkdownUrl()`, or `getDefaultBranch()` when the plugin supplies external help or source links. Keep the short description suitable for menus and search results; use the summary for the fuller explanation.

### Third-party dependency licenses

`PluginInfo.json` is the preferred place to declare licenses for dependencies that a plugin uses. Core reads the `thirdPartyLicenses` array while loading the plugin factory and copies valid entries into the plugin metadata. The public API also allows a plugin to manage this information at runtime through `PluginMetadata::getThirdPartyLicenses()`, `setThirdPartyLicenses()`, `addThirdPartyLicense()`, and `removeThirdPartyLicense()`. Plugin and factory facades expose the same data through `Plugin::getThirdPartyLicenses()` and `PluginFactory::getThirdPartyLicenses()`.

Use the JSON metadata for licenses that are part of the plugin's normal distribution. If a dependency is selected only in a particular build configuration, keep its entry aligned with the binaries shipped in that configuration. License entries are metadata; they do not replace the dependency's `target_link_libraries()` or runtime installation rules.

The aggregated view is available to users from the Help menu. It combines Core and plugin entries, removes duplicates, retains which plugins use each dependency, and links each entry to its URL. See [core PR #1340](https://github.com/ManiVaultStudio/core/pull/1340), the [Image Loader example](https://github.com/ManiVaultStudio/ImageLoaderPlugin/blob/feature/license-aggregation/PluginInfo.json), and the [t-SNE Analysis examples](https://github.com/ManiVaultStudio/t-SNE-Analysis/commit/67eecce62fa685d750eb6535e847c61c75243fc4) for the API and metadata changes. See the {doc}`Third-party licenses guide <../../../user_guide/third_party_licenses>` for the user workflow.

## CMake

The ManiVault CMake package makes the following helpers available after `find_package(ManiVault ... CONFIG REQUIRED)`. No separate `include()` calls are needed. The [ExamplePlugins repository](https://github.com/ManiVaultStudio/ExamplePlugins), particularly [ExampleDependencies/CMakeLists.txt](https://github.com/ManiVaultStudio/ExamplePlugins/blob/master/ExampleDependencies/CMakeLists.txt), demonstrates their use together.

| Helper | Purpose | When to call it |
| --- | --- | --- |
| `mv_project_defaults()` | Apply shared compiler and platform settings | Immediately after finding ManiVault, before creating targets |
| `mv_handle_plugin_config(target)` | Read plugin metadata and set the output library name | After creating the plugin target |
| `mv_install_dependencies(target ...)` | Gather and install runtime library dependencies | After defining and linking the plugin and dependency targets |
| `mv_check_and_set_AVX(target enabled)` | Enable supported AVX compiler options | After creating each target that should use AVX |

Use a ManiVault installation that provides the helpers you call; `mv_project_defaults()` was added more recently than the other helpers.

### Project defaults

Call `mv_project_defaults()` to keep platform settings consistent with ManiVault core:

```cmake
project(ExampleViewPlugin LANGUAGES CXX)

find_package(Qt6 COMPONENTS Widgets WebEngineWidgets REQUIRED)
find_package(ManiVault COMPONENTS Core PointData CONFIG REQUIRED)
mv_project_defaults()

# Define the plugin sources and create the target next.
```

On MSVC, this selects the DLL runtime (`/MD` or `/MDd`) and common warning, parallel compilation, and language/preprocessor flags. On Unix platforms it configures build and install RPATH behavior; on macOS it also enables Xcode scheme generation. The helper guards its common global settings against repeated application.

For MSVC Release builds with PDB debug information, configure with `-DMV_RELWITHDEBUGINFO=ON` before calling the helper. This option defaults to `OFF` and adds `/Zi`, `/Zf`, and shared-library linker `/DEBUG` flags while retaining the Release configuration.

Continue to set target-specific properties such as the C++ standard, `AUTOMOC`, and `UNITY_BUILD` in the plugin's own CMake code. The helper does not set those properties.

See [core PR #1240](https://github.com/ManiVaultStudio/core/pull/1240) and [issue #1187](https://github.com/ManiVaultStudio/core/issues/1187) for background, and [ExamplePlugins PR #54](https://github.com/ManiVaultStudio/ExamplePlugins/pull/54) and [Scatterplot PR #241](https://github.com/ManiVaultStudio/Scatterplot/pull/241) for migrations from manually maintained flags.

### Plugin configuration

After creating the plugin target, process the `PluginInfo.json` in `CMAKE_CURRENT_SOURCE_DIR`:

```cmake
mv_handle_plugin_config(${PLUGIN_TARGET})
```

The file must exist and contain `name` and `version.plugin`. The helper sets the target's `OUTPUT_NAME` to `<target>_p<plugin-version>_c<core-version>`. For example, target `ExampleViewPlugin`, plugin version `1.0.0`, and core version `1.5.1` produce the base name `ExampleViewPlugin_p1.0.0_c1.5.1`; the platform adds its usual library prefix and extension. The CMake target name stays unchanged, so keep using `${PLUGIN_TARGET}` in linking and installation commands.

The core version comes from `ManiVault_VERSION` for external plugins or `MV_VERSION` for plugins built with core. If neither is available, the helper warns and uses `0.0.0`. It reads the JSON and sets target properties; it does not rewrite the JSON or populate runtime factory metadata.

When `type` is present, the helper also sets the target's IDE folder to `<type>Plugins`. To choose your own folder, pass the optional second argument `0`, as the example plugins do:

```cmake
mv_handle_plugin_config(${PLUGIN_TARGET} 0)
set_target_properties(${PLUGIN_TARGET} PROPERTIES FOLDER "ExamplePlugins")
```

Ensure `PluginInfo.json` is part of the target sources when required by the Qt build setup, and that Qt's metadata compiler can find it for `Q_PLUGIN_METADATA`.

See [core PR #911](https://github.com/ManiVaultStudio/core/pull/911), [core PR #912](https://github.com/ManiVaultStudio/core/pull/912), [Scatterplot PR #176](https://github.com/ManiVaultStudio/Scatterplot/pull/176), and [ExamplePlugins PR #43](https://github.com/ManiVaultStudio/ExamplePlugins/pull/43). Some historical examples contain `version.core`; the current helper obtains the core version from CMake as described above.

### Runtime dependency installation

Use `mv_install_dependencies()` when the plugin needs additional shared libraries at runtime:

```cmake
# The plugin and the Highway shared-library targets already exist.
target_link_libraries(${PLUGIN_TARGET} PRIVATE hwy hwy_contrib)
mv_install_dependencies(${PLUGIN_TARGET} hwy hwy_contrib)
```

The first argument is the plugin target. Optional additional arguments are CMake library targets whose output directories should be searched when resolving dependencies. The plugin's own output directory is included automatically. If no extra search locations are needed, use `mv_install_dependencies(${PLUGIN_TARGET})`.

The helper registers the `PLUGIN_DEPENDENCIES` install component and a post-build command that runs it for the active configuration. It scans the built plugin with CMake's `file(GET_RUNTIME_DEPENDENCIES)` and installs resolved libraries, including transitive dependencies, into:

```text
${ManiVault_INSTALL_DIR}/<configuration>/PluginDependencies/<plugin-target>/
```

ManiVault loads libraries from this per-plugin directory before loading the plugin. Platform-specific filters exclude Qt, core/data-plugin libraries, and selected system libraries already supplied by the application or operating system. Check the installation output for unresolved or conflicting dependencies.

This helper gathers runtime binaries; dependency acquisition and `target_link_libraries()` remain part of your build setup. It also does not install the plugin itself. Keep the plugin's own install rules and installation step, for example:

```cmake
install(TARGETS ${PLUGIN_TARGET}
    RUNTIME DESTINATION Plugins COMPONENT PLUGINS
    LIBRARY DESTINATION Plugins COMPONENT PLUGINS
)

add_custom_command(TARGET ${PLUGIN_TARGET} POST_BUILD
    COMMAND "${CMAKE_COMMAND}"
        --install "${CMAKE_CURRENT_BINARY_DIR}"
        --config $<CONFIGURATION>
        --component PLUGINS
        --prefix "${ManiVault_INSTALL_DIR}/$<CONFIGURATION>"
)
```

The `dependencies` array in `PluginInfo.json` is separate from this runtime-library scan. See [core PR #692](https://github.com/ManiVaultStudio/core/pull/692) and [ExamplePlugins PR #32](https://github.com/ManiVaultStudio/ExamplePlugins/pull/32) for the dependency-loading design and a complete example.

### Optional AVX compilation

Use `mv_check_and_set_AVX()` to opt a target into AVX compiler flags:

```cmake
option(MV_USE_AVX "Enable AVX instructions for this plugin" OFF)

# Call after add_library().
mv_check_and_set_AVX(${PLUGIN_TARGET} ${MV_USE_AVX})
```

With the option disabled, the helper leaves the target unchanged. When enabled on x86, it checks compiler flag support, prefers AVX2, and falls back to AVX. It adds the selected flag privately to the target: `/arch:AVX2` or `/arch:AVX` on MSVC, and `-mavx2` or `-mavx` otherwise. Non-x86 targets are skipped, and no flag is added if neither is supported.

To restrict the helper to AVX even when the compiler supports AVX2, use this alternative call with a third argument:

```cmake
mv_check_and_set_AVX(${PLUGIN_TARGET} ${MV_USE_AVX} 1)
```

These are compiler capability checks, not runtime CPU detection or dispatch. Enable AVX only when the machines running the plugin support the selected instruction set. Keep the option off for builds that must run on CPUs without AVX support.

The [ExampleDependencies CMake file](https://github.com/ManiVaultStudio/ExamplePlugins/blob/master/ExampleDependencies/CMakeLists.txt) shows an explicit `OFF` call. See [core PR #331](https://github.com/ManiVaultStudio/core/pull/331), [core PR #336](https://github.com/ManiVaultStudio/core/pull/336), and [core PR #692](https://github.com/ManiVaultStudio/core/pull/692) for the helper's introduction and later integration into the ManiVault package.

The complete signatures for runtime metadata are in the {doc}`PluginMetadata API reference <../../../api/core/plugin/plugin_metadata>`.

For `Q_OBJECT`, AUTOMOC discovery, custom meta-types, and Qt binary compatibility, see {doc}`Meta-object and build integration <../qt_considerations/meta_object_and_build>`.
