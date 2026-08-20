# Plugin creation policy and instance limits

A plugin factory controls where its plugin can be offered for creation and how many instances may coexist. Configure that policy deliberately when a plugin owns an exclusive resource, has a high resource cost, should only be created in a specific context, or should have one application-wide instance.

Start with {doc}`choosing_a_policy`. Most plugins need only one or two factory settings; the remaining pages explain how those settings interact with triggers, programmatic requests, destruction, and project restoration.

```{toctree}
:maxdepth: 1

choosing_a_policy
configuring_the_factory
triggers_and_requests
lifecycle_and_restoration
testing_and_pitfalls
```

## Core rules

- Put creation policy on the factory, not on a plugin instance.
- Leave the instance limit unlimited unless the plugin has a concrete exclusivity or resource reason.
- Use contextual trigger actions to decide whether a particular dataset selection is valid.
- Request instances through the plugin manager. Never call `produce()` directly.
- Let the core maintain the live and produced instance counters.
- Include project restoration in the compatibility analysis before introducing or reducing a limit.

The relevant API entry points are {doc}`PluginFactory <../../../api/core/plugin/plugin_factory>`, {doc}`PluginTriggerAction <../../../api/core/gui/actions/internal/plugin_trigger_action>`, and {doc}`AbstractPluginManager <../../../api/core/managers/abstract_plugin_manager>`.
