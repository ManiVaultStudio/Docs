# Plugin fundamentals

A ManiVault plugin has two cooperating objects: one factory loaded for the plugin library and zero or more plugin instances created from it. The factory describes what can be created and where creation is offered; an instance owns the state and behavior of one running plugin.

Start here when creating a plugin or when deciding where new behavior belongs.

```{toctree}
:maxdepth: 1

choosing_a_type
factory_and_instance
lifecycle
triggers_and_inputs
metadata_and_build
implementation_checklist
```

The {doc}`plugin API reference <../../../api/core/plugin/index>` provides complete class and member documentation. The pages in this section explain how those APIs fit together.
