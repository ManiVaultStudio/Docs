# Plugins

**ManiVault** manages the lifetime of all plugins through the {cpp:class}`mv::AbstractPluginsManager`. Plugins are tracked in dedicated **list** and **tree** models, which are primarily used by the UI to present plugin state and structure (for example in the plugin browser). The model classes below are for storing and filtering plugins.

```{note}
This API is **stable** and intended for use by **core developers**. Plugin developers typically do not need to interact with it directly, as it is fully wrapped by the plugins manager.
```

```{toctree}
:maxdepth: 1

abstract_plugins_model
plugins_tree_model
plugins_list_model
plugins_filter_model
```

