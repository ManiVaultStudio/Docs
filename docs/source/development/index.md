# Development

Use ManiVault as an extensible host, as the foundation of a customized application, or as a framework you build and contribute to directly. The guides here explain those different routes and the shared execution facilities available to plugin and application developers.

## Choose a route

| Goal | Start here |
| --- | --- |
| Add a loader, analysis, transformation, visualization, writer, or data type | {doc}`Building plugins <building_plugins/index>` |
| Configure and distribute a purpose-built ManiVault application | {doc}`Building applications <building_applications/index>` |
| Set up a development environment or build the core application | {doc}`Building ManiVault <building_manivault/index>` |
| Schedule concurrent or staged operations | {doc}`Parallel execution <parallel_execution/index>` |

Plugins are the normal extension mechanism for functionality that should integrate into an existing installation. Build an application when ManiVault is the foundation for a controlled product with its own identity, configuration, and feature set. The parallel-execution guide is a supporting resource for both routes, not a separate extension model.

## Extend and customize

```{toctree}
:maxdepth: 1

building_plugins/index
building_applications/index
```

## Build and execute

```{toctree}
:maxdepth: 1

building_manivault/index
parallel_execution/index
```
