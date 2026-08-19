# Factory and plugin instance

The factory is the plugin library's long-lived registration object. It advertises metadata, supported inputs, creation triggers, global settings, status-bar integration, and instance limits. `produce()` creates one instance.

The instance represents one use of the plugin. It owns per-instance actions, widgets, datasets, tasks, and serializable state. Always pass the producing factory to the instance base-class constructor.

```cpp
class ExampleViewPlugin final : public mv::plugin::ViewPlugin
{
    Q_OBJECT

public:
    explicit ExampleViewPlugin(const mv::plugin::PluginFactory* factory);
    void init() override;
};

class ExampleViewPluginFactory final : public mv::plugin::ViewPluginFactory
{
    Q_OBJECT
    Q_INTERFACES(mv::plugin::ViewPluginFactory mv::plugin::PluginFactory)
    Q_PLUGIN_METADATA(IID  "studio.manivault.ExampleViewPlugin"
                      FILE "PluginInfo.json")

public:
    ExampleViewPluginFactory();
    mv::plugin::ViewPlugin* produce() override;
};
```

Construct factory-owned facilities in the factory constructor:

```cpp
ExampleViewPluginFactory::ExampleViewPluginFactory() :
    ViewPluginFactory(false)
{
    setIconByName("chart-scatter");
    getPluginMetadata().setDescription("Shows an example visualization");
    getPluginMetadata().setSummary(
        "Displays supported point datasets in an interactive view.");
}

mv::plugin::ViewPlugin* ExampleViewPluginFactory::produce()
{
    return new ExampleViewPlugin(this);
}
```

`produce()` should allocate the matching concrete instance and return it. Request creation through the plugin manager or a `PluginTriggerAction`; those paths register the instance, assign type-specific inputs, initialize it, update instance counts, and integrate it into the application. Calling `produce()` directly bypasses that work.

## Where state belongs

| State or behavior | Owner |
| --- | --- |
| Display name, authors, license, summary | Factory metadata |
| Supported data types and creation triggers | Factory |
| Global settings shared by all instances | Factory |
| Status-bar action representing the plugin kind | Factory |
| Per-view controls, input datasets, computation state | Instance |
| Project-persisted settings for one instance | Instance actions and serialization |

For shared settings, see {doc}`Global settings <../global_settings>`. For per-instance state, see {doc}`Project persistence <../persistence/index>`.
