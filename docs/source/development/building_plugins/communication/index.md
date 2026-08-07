# Plugin communication and creation triggers

Plugins should communicate through stable core abstractions: datasets for data exchange, actions for shared parameters and commands, and the plugin manager plus factory triggers for creating and initializing plugin instances.

```{toctree}
:maxdepth: 1

choosing_a_mechanism
requesting_plugins
dataset_triggers
lifetime_and_errors
```

For exact signatures, see the {doc}`plugin manager <../../../api/core/managers/abstract_plugin_manager>`, {doc}`plugin factory <../../../api/core/plugin/plugin_factory>`, and {doc}`PluginTriggerAction <../../../api/core/gui/actions/internal/plugin_trigger_action>` references.
