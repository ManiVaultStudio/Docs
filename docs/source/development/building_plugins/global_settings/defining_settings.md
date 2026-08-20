# Defining global settings

## Create a typed group

Derive a plugin-specific action so callers can access typed child actions without searching by title:

```cpp
#include <PluginGlobalSettingsGroupAction.h>
#include <actions/ToggleAction.h>

class ExampleGlobalSettingsAction final
    : public mv::gui::PluginGlobalSettingsGroupAction
{
public:
    ExampleGlobalSettingsAction(
        QObject* parent,
        const mv::plugin::PluginFactory* factory) :
        PluginGlobalSettingsGroupAction(parent, factory),
        _enableLabelsAction(this, "Enable labels by default", true)
    {
        _enableLabelsAction.setSerializationName("EnableLabelsByDefault");
        addAction(&_enableLabelsAction);
    }

    mv::gui::ToggleAction& getEnableLabelsAction()
    {
        return _enableLabelsAction;
    }

private:
    mv::gui::ToggleAction _enableLabelsAction;
};
```

Set an explicit serialization name before `addAction()`. The displayed title can then be improved or translated without changing the persistent key.

The child action must belong to the settings group through its QObject parent chain. `GlobalSettingsGroupAction::addAction()` assigns an automatic settings prefix only to its children. Adding an action parented to the factory or another object will display it but will not establish the expected persistence path.

## Register from the factory

Create and register the group during factory initialization:

```cpp
void ExampleViewPluginFactory::initialize()
{
    ViewPluginFactory::initialize();

    setGlobalSettingsGroupAction(
        new ExampleGlobalSettingsAction(this, this));
}
```

The first `this` makes the factory the QObject owner; the second identifies the plugin factory whose kind names the group. `setGlobalSettingsGroupAction()` stores a pointer and emits a change signal, but it does not take ownership or reparent the group. Give the group a lifetime at least as long as the factory.

The settings dialog enumerates loaded factories and includes each registered group. Plugin code does not manually add the group to that dialog.

## Defaults and restoration order

Construct each child with its fallback default, assign its stable serialization name, and then add it to the group. Adding it assigns the settings path and immediately attempts to load a stored action map. A stored value therefore replaces the constructor default.

Do not apply the default again after `addAction()`, because doing so can overwrite the restored preference and save the overwrite immediately.

Standard value actions such as toggles, numeric actions, strings, colors, and options save when their values change. A custom action that owns additional persistent state must include that state in `toVariantMap()` and `fromVariantMap()` and call `saveToSettings()` from the relevant mutator.
