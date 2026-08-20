# PluginTriggerAction

**Qualified name:** `mv::gui::PluginTriggerAction`

This action represents a default or contextual request to create a plugin instance. For factory overrides, dataset validation, and callback lifetime, see {doc}`Dataset-sensitive plugin triggers <../../../../../development/building_plugins/communication/dataset_triggers>`.

Trigger availability is presentation; managed creation and instance-limit enforcement remain the plugin manager's responsibility. See {doc}`Triggers and creation requests <../../../../../development/building_plugins/creation_policy/triggers_and_requests>`.

```{doxygenclass} mv::gui::PluginTriggerAction
:members:
:protected-members:
