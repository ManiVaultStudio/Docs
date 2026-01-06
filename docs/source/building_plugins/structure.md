## Plugin class
The heart of every plugin is the class deriving from one of the ManiVault base plugin classes (ViewPlugin, AnalysisPlugin, etc.). This class represents an opened instance of that specific plugin. An example plugin class derived from ViewPlugin is shown below:

```Cpp
class ExampleViewPlugin : public ViewPlugin
{
    Q_OBJECT
public:
    /**
     * Constructor
     * @param factory Pointer to the plugin factory
     */
    ExampleViewPlugin(const PluginFactory* factory) { }

    /** Destructor */
    ~ExampleViewPlugin() override = default;
    
    /** This function is called by the core after the view plugin has been created */
    void init() override { }
};
```

At minimum the plugin class consists of:
* A constructor, responsible for initializing the plugin members
* A destructor, responsible for correctly cleaning up data if the plugin is closed by the user
* An init() function, responsible for initializing the plugin after it has been added to the system

## Plugin factory
Factories create plugin and are used for setting up meta data, like names, supported data types, icons, links to README and documentation.

A bare-bone example looks like this:
```cpp
class ExampleViewPluginFactory : public ViewPluginFactory
{
    Q_INTERFACES(mv::plugin::ViewPluginFactory mv::plugin::PluginFactory)
    Q_OBJECT
    Q_PLUGIN_METADATA(IID   "studio.manivault.ExampleViewPlugin"
                      FILE  "PluginInfo.json")

public:

    /** Default constructor */
    ExampleViewPluginFactory();

    /** Creates an instance of the example view plugin */
    ViewPlugin* produce() override;

    /** Returns the data types that are supported by the example view plugin */
    mv::DataTypes supportedDataTypes() const override;

    /**
     * Get plugin trigger actions given \p datasets
     * @param datasets Vector of input datasets
     * @return Vector of plugin trigger actions
     */
    PluginTriggerActions getPluginTriggerActions(const mv::Datasets& datasets) const override;
};
```

## Plugin Config File

Each plugin must be accompanied by a config file, above called `PluginInfo.json`.
 This file contains meta data which is read at build time. 

Example for a Loader type plugin:
```json
{
    "name" : "Example Loader",
    "menuName" : "Example (.xmp)",
    "version" :  {
        "plugin" : "1.4",
        "core" : ["1.3"]
    },
    "type" : "Loader",
    "dependencies" : ["Points"]
}
```

Required fields:
- `name`: Name of the plugin
- `dependencies`: Documents runtime dependencies, other ManiVault (data) plugins

Optional:
- `type`: Plugin type, may be handled by CMake helper function `mv_handle_plugin_config` 
- `version::plugin`: Version of the plugin, is handled by CMake helper function `mv_handle_plugin_config` 
- `version::core`: Version(s) of the core that this plugin version has been tested against
- `menuName`: Entry in drop down menus [Only Loader and Writer types] 

The CMake helper function `mv_handle_plugin_config` may be used to automatically append plugin version and the version of the core that the plugin is built against to the plugin library file. When using this function, `version::plugin` becomes a required field as well.

The CMake entry:
```cmake
mv_handle_plugin_config(${PROJECT})
```
will automatically append the plugin version and the core version that is currently build against (not the exact version from the `PluginInfo.json`) to output library name, e.g. for the `ScatterplotPlugin`:
 - `ScatterplotPlugin_p1.0.0_c1.4.0.dll` on Windows
 - `libScatterplotPlugin_p1.0.0_c1.4.0.dylib` on Mac
 - `libScatterplotPlugin_p1.0.0_c1.4.0.so` on Linux

## Plugin help menu entry
It is always helpful to provide information about how a plugin works, e.g. description of settings or a listing of features.

For view plugins this is as easy as providing a URL to the repository, and ManiVault will automatically add a `Readme` entry into the burger menu of the plugin's widget:

```cpp
/// [MyPlugin.h]

class MyPluginFactory {
public:
    QUrl getRepositoryUrl() const override { return { "https://github.com/ManiVaultStudio/Scatterplot" }; }
}
```

| Access | Markdown display      |
| ------------- | ------------- |
| ![Access](https://github.com/user-attachments/assets/df38947d-85f7-4a91-a6fd-7a97716f8ad6) | ![markdown](https://github.com/user-attachments/assets/655a4d3e-11a1-432d-a773-f40eecd7069e) |

For other plugins that do not have their own UI widget (e.g. Analysis and Loader), we can provide this information by adding a markdown file to the `Help` `->` `Plugins` menu entry for our plugin:

```cpp
/// [MyPlugin.h]

namespace mv::util {
    class MarkdownDialog;
}

class MyPluginFactory {
public:
    QUrl getReadmeMarkdownUrl() const override;
    bool hasHelp() const override { return true; }

private:
    QPointer<mv::util::MarkdownDialog>   _helpMarkdownDialog = {};

}

/// [MyPlugin.cpp]

#include <widgets/MarkdownDialog.h>

MyPluginFactory::MyPluginFactory() {
    connect(&getPluginMetadata().getTriggerHelpAction(), &TriggerAction::triggered, this, [this]() -> void {
        if (!getReadmeMarkdownUrl().isValid() || _helpMarkdownDialog.get())
            return;

        _helpMarkdownDialog = new util::MarkdownDialog(getReadmeMarkdownUrl());

        _helpMarkdownDialog->setWindowTitle(QString("%1").arg(getKind()));
        _helpMarkdownDialog->setAttribute(Qt::WA_DeleteOnClose);
        _helpMarkdownDialog->setWindowModality(Qt::NonModal);
        _helpMarkdownDialog->show();
        });

}
```

| Access | Markdown display      |
| ------------- | ------------- |
| ![help](https://github.com/user-attachments/assets/c41ccfa5-4ea1-4497-ba31-f6300c627118)| ![markdown](https://github.com/user-attachments/assets/ffdb7603-b186-4bc2-baec-3bbc4783b847)|