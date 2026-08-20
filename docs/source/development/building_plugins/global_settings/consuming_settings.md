# Consuming and reacting to settings

## Read through the plugin facade

Every plugin instance can obtain the group registered by its factory. Cast it to the plugin-specific type and handle the absence defensively:

```cpp
void ExampleViewPlugin::init()
{
    auto* globalSettings =
        dynamic_cast<ExampleGlobalSettingsAction*>(getGlobalSettingsAction());

    if (globalSettings == nullptr)
        return;

    auto& enableLabels = globalSettings->getEnableLabelsAction();

    applyLabelPolicy(enableLabels.isChecked());

    connect(&enableLabels, &mv::gui::ToggleAction::toggled,
            this, &ExampleViewPlugin::applyLabelPolicy);
}
```

Reading once and connecting implements a live policy. If the setting is only a default for new instances, initialize the instance-owned action from `isChecked()` but do not connect it to later global changes.

Always apply the current value explicitly. Stored state is loaded while the global settings group is being constructed, before most plugin instances connect to its signals.

## Read through the settings manager

Code that does not already have the factory can query by plugin kind or instance:

```cpp
auto* globalSettings =
    mv::settings().getPluginGlobalSettingsGroupAction<
        ExampleGlobalSettingsAction>(plugin);
```

The settings manager returns `nullptr` when no group is available. Querying another plugin also creates a compile-time and runtime dependency on that plugin's settings type; reserve it for intentional integrations and first confirm that the plugin kind is loaded.

Within a plugin, `getGlobalSettingsAction()` or a typed factory getter usually expresses ownership more clearly.

## UI-less application preferences

Use the plugin facade for a preference that should be shared and persisted but should not appear in the settings dialog:

```cpp
const auto iterations =
    getSetting("Computation/Iterations", 32).toInt();

setSetting("Computation/Iterations", 64);
```

All instances of the same plugin kind address the same path. This API stores a `QVariant`; it does not provide a settings widget, change signal, validation, or automatic synchronization between active instances. Add those semantics explicitly, or use an action-backed global setting when users should edit or observe the value.

Use stable, relative paths without a leading slash. Group related keys, for example `Computation/Iterations`, but do not manually prepend the plugin kind.

## Apply changes safely

Global action signals are GUI-thread notifications. Keep their immediate handlers lightweight. If changing a preference requires a substantial recomputation, update state and start the work through the {doc}`workflow engine or task facilities <../tasks/tasks_and_workflows>`. Define what happens when the setting changes again while previous work is running: cancel, supersede, or queue it.

Avoid having every instance write back to the global action while responding to it. One user change should flow outward from the shared action; feedback connections can create redundant saves or signal loops.
