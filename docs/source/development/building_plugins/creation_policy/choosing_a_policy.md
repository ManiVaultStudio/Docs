# Choosing a creation policy

Creation policy has two independent axes:

1. **Discoverability:** should standard ManiVault interfaces offer the plugin?
2. **Multiplicity:** how many live instances may coexist?

Choose both explicitly. Hiding a plugin does not make it a singleton, and limiting it does not hide it before the limit is reached.

## Common policies

| Requirement | Factory policy | Typical example |
| --- | --- | --- |
| Any number of instances | Keep the default unlimited maximum | Independent views or analyses |
| Exactly one live instance at most | Set the maximum to `1` | Exclusive device or application-wide panel |
| Small finite pool | Set a finite maximum greater than `1` | Expensive GPU-backed views |
| Never user-created through standard UI | Disable standard-GUI creation | Infrastructure created by another plugin or application |
| Valid only for particular datasets | Return contextual trigger actions only for supported selections | Analysis or transformation with exact input requirements |

An instance limit is a **concurrent live-instance limit**. It is not a quota on how many instances may ever be created during the application session. When one instance is destroyed, capacity becomes available again.

## Prefer contextual validity over a global limit

Do not use a maximum to express whether an input selection is valid. Override `supportedDataTypes()` for broad capability discovery and return dataset-sensitive trigger actions for exact constraints such as count, ordering, types, or relationships. The plugin instance should still validate its inputs when it runs.

See {doc}`Creation triggers and inputs <../fundamentals/triggers_and_inputs>` and {doc}`Dataset-sensitive plugin triggers <../communication/dataset_triggers>`.

## When a singleton is appropriate

A maximum of one is appropriate when two instances would be invalid, rather than merely unusual. Examples include exclusive ownership of hardware, one process-wide coordinator, or a UI whose state is intentionally global.

If multiple instances could be valid but are expensive, first consider whether resources can be shared at factory or service scope. A hard limit changes automation and project compatibility, so it should represent a real product constraint.

## Hiding is not access control

`setAllowPluginCreationFromStandardGui(false)` prevents standard ManiVault surfaces from presenting the factory's triggers. It does not prohibit creation through the plugin manager, project restoration, scripts, or plugin-specific UI. Treat it as presentation policy, not security or authorization.
