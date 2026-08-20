# Building plugins

Plugins are ManiVault's primary extension mechanism. A plugin can introduce data storage, loading, analysis, transformation, visualization, or export while relying on the core for datasets, project state, execution, actions, and application integration.

## Choose a starting point

| Goal | Start here |
| --- | --- |
| Create a plugin and choose its type | {doc}`Plugin fundamentals <fundamentals/index>` |
| Read, create, link, or observe datasets | {doc}`Working with data and datasets <data/index>` |
| Add persistent controls and settings | {doc}`Plugin actions and settings <actions/index>` |
| Exchange state or request another plugin | {doc}`Plugin communication and creation triggers <communication/index>` |
| Run a long operation and report progress | {doc}`Long-running operations and task progress <tasks/index>` |
| Save and restore plugin-owned state | {doc}`Project serialization and restoration <persistence/index>` |
| Diagnose a failure or report it to the user | {doc}`Notifications, logging, errors, and diagnostics <diagnostics/index>` |
| Integrate with application UI and help | See **Application integration** below |

If you are implementing a new plugin, follow Fundamentals first, then Data and Actions. Add the remaining sections when the plugin's behavior requires them. Use the {doc}`core API reference <../../api/core/index>` for exact class and member signatures.

## Core plugin development

```{toctree}
:maxdepth: 1

fundamentals/index
data/index
actions/index
communication/index
```

## Execution, state, and failures

```{toctree}
:maxdepth: 1

tasks/index
persistence/index
diagnostics/index
```

## Application integration

```{toctree}
:maxdepth: 1

drag_and_drop/index
icons
creation_policy/index
global_settings/index
status_bar/index
learning_center/index
qt_considerations/index
```

```{toctree}
:hidden:

types
structure
learning_center
drag_and_drop
global_settings
status_bar
qt_considerations
limit_creation
```
