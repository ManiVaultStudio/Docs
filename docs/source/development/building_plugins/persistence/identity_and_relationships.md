# Identity and persistent relationships

`Serializable::getId()` is persistent identity. Restoration reapplies stored IDs so references between datasets, plugins, actions, and hierarchy nodes can be resolved consistently.

Store stable IDs for relationships, not raw pointers, display names, hierarchy row numbers, or container addresses:

```cpp
map["SourceDatasetId"] = _source.getDatasetId();
```

During restoration, resolve an ID only after the owning subsystem has recreated the target. Dataset implementations and hierarchy restoration are orchestrated by the core; plugin code should use the restored input datasets supplied by the plugin manager where possible.

## Serialization name versus object ID

- The serialization name is the key used inside a parent map.
- The object ID identifies the persistent object represented by the map.
- A GUI title is presentation and should not be used for either unless it is intentionally stable.

Sibling entries need unique serialization names. Renaming a key requires migration logic; changing an ID changes logical identity and can break references.

Use hierarchy parentage only for presentation. Persist source, full-dataset, derived, linked-data, or proxy relationships through their dedicated dataset contracts.
