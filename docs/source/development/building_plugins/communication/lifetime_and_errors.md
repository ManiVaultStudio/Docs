# Lifetime and error handling

Creation triggers often outlive the menu that displays them but contain dataset handles whose implementations can disappear. Validate context at invocation time, not only when constructing the trigger.

## Trigger and callback lifetime

`PluginTriggerActions` stores `QPointer<PluginTriggerAction>`, so consumers can detect deleted actions. A request callback is owned by its trigger. Capture stable values or handles and avoid capturing UI objects without a Qt lifetime guard.

If a callback needs the trigger's current datasets, read `action.getDatasets()` and remove invalid handles before requesting the plugin. Never retain the callback's raw plugin result without accounting for plugin destruction.

## Failure boundaries

Programmatic plugin creation can fail because:

- the plugin kind is not loaded;
- the factory cannot produce an instance;
- the maximum instance count has been reached;
- type-specific initialization rejects its inputs;
- plugin initialization throws.

Let expected optionality influence the UI before invocation. At the request boundary, either allow the core's `ManiVaultException` to reach the standard error handling or catch it where your component can add meaningful context. Do not continue with a null or partially initialized plugin.

## Expensive follow-up work

Keep creation callbacks short. Create and initialize the plugin, then let its normal task or workflow API perform expensive analysis, loading, or transformation with progress and cancellation. A trigger callback runs on the interaction path and should not block the GUI thread.
