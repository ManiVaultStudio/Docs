# PropertiesSerializer

**Qualified name:** `mv::PropertiesSerializer`

`PropertiesSerializer` provides workflow-based conversion for ManiVault property maps. Core uses it while persisting dataset and set properties so that potentially substantial property values participate in the surrounding serialization workflow.

```{warning}
This is a specialized, temporary Core helper and may be removed in a future release. Do not use it as the general persistence contract for a plugin. Implement {doc}`Serializable <serializable>` and follow the {doc}`plugin persistence guide <../../../../development/building_plugins/persistence/index>` instead.
```

```{doxygenclass} mv::PropertiesSerializer
:members:
:protected-members:
```
