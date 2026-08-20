# Triggers and creation requests

Creation triggers are UI entry points; the plugin manager is the creation authority. Keeping that distinction intact ensures that menu actions, contextual actions, scripts, other plugins, and project restoration use the same managed lifecycle.

## Standard and contextual triggers

Each factory owns a standard `PluginTriggerAction`. The core disables that action when the live instance count reaches the configured maximum and enables it again after capacity becomes available.

Factories can also return contextual trigger actions for a particular dataset selection. Only return an action when that selection is valid, and capture the validated datasets in its request callback. See {doc}`Dataset-sensitive plugin triggers <../communication/dataset_triggers>` for the complete pattern.

The standard-GUI flag is checked by standard presentation surfaces. A custom application surface that displays trigger actions should apply the same flag if it intends to honor standard ManiVault presentation policy.

## Always request through the manager

Use the plugin manager from both plugin code and trigger callbacks:

```cpp
try {
    auto* plugin = mv::plugins().requestPlugin<MyAnalysisPlugin>(
        "MyAnalysisPlugin",
        inputDatasets);

    if (!plugin)
        return;
} catch (const mv::ManiVaultException& exception) {
    // Report the failure through the appropriate diagnostics channel.
}
```

Do not call `PluginFactory::produce()` yourself. Direct production bypasses manager ownership, input assignment, initialization, registration, view placement, signals, and instance accounting.

See {doc}`Requesting plugin instances <../communication/requesting_plugins>` for type-specific request and ownership guidance.

## `mayProduce()` is a snapshot

`PluginFactory::mayProduce()` reports whether the current live count is below the maximum. It is useful for disabling an optional UI affordance, but it is not a reservation and should not be treated as final authorization.

State may change between a preflight check and the actual request. Always handle failure from the manager request even if `mayProduce()` returned `true`. Conversely, do not reimplement the limit in every caller; the manager performs the authoritative check.

## Programmatic creation remains possible

Disabling standard-GUI creation does not disable manager requests. A controlled creator can therefore hide a low-level plugin from general menus and still request it:

```cpp
auto* factory = mv::plugins().getPluginFactory("InfrastructurePlugin");

if (factory && factory->mayProduce())
    mv::plugins().requestPlugin("InfrastructurePlugin");
```

The preflight improves the immediate user experience, while exception handling around the request remains necessary.
