# Choosing a communication mechanism

Choose the narrowest mechanism that expresses the relationship without making plugins depend unnecessarily on each other's implementation.

| Need | Mechanism |
| --- | --- |
| Exchange or observe data | `Dataset<T>` handles and dataset events |
| Synchronize compatible parameters | Public and private `WidgetAction` connections |
| Offer a user-invoked command | `TriggerAction` or an attached action |
| Let users create a plugin from selected data | Factory-provided `PluginTriggerAction` |
| Create a known plugin programmatically | `mv::plugins().requestPlugin(...)` |
| Find metadata or contextual triggers without creating | Plugin factory or manager queries |

Prefer dataset and action contracts over casting to a concrete plugin. A direct cast is appropriate only when the caller intentionally depends on that plugin kind and needs an API not represented by a shared abstraction.

Do not cache another plugin's raw pointer as a general service locator. Plugin instances can be destroyed independently; pass required context during creation or use lifecycle-aware Qt connections.
