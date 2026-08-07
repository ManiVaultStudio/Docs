# Project serialization and restoration

Project persistence reconstructs datasets, hierarchy state, plugin instances, views, and settings as one coordinated operation. Plugin code contributes only the state it owns; the project manager controls the file operation, ordering, workflows, progress, and final lifecycle signals.

```{toctree}
:maxdepth: 1

plugin_state
synchronous_and_workflow
identity_and_relationships
project_lifecycle
compatibility_and_testing
```

For exact signatures, see {doc}`Serializable <../../../api/core/util/serialization/serializable>` and the {doc}`project manager <../../../api/core/managers/abstract_project_manager>`.
