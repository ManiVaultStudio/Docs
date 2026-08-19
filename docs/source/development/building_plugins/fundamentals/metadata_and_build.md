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
  "dependencies": []
}
```

`name` identifies the library, and `version.plugin` is its semantic version. `mv_handle_plugin_config()` requires both values, appends the plugin and ManiVault core versions to the output library name, and uses the optional top-level `type` only to group targets in generators that support folders. `dependencies` records plugin dependencies for the surrounding plugin tooling.

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

## CMake

After defining and linking the plugin target, let the ManiVault helper process its configuration:

```cmake
mv_handle_plugin_config(${PLUGIN_TARGET})
```

Ensure `PluginInfo.json` is part of the target sources when required by the Qt build setup. The complete signatures for runtime metadata are in the {doc}`PluginMetadata API reference <../../../api/core/plugin/plugin_metadata>`.
