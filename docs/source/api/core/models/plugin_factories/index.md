# Plugin Factories
 
Plugin factories are used to create instances of plugins. The core keeps track of which plugin factories are loaded, for which below model classes are used. These models are also used in the **plugin browser**.

```{note}
This API is **stable** and intended for use by **core developers**. Plugin developers do not need to interact with it directly, as the core tracks its **plugin factories** internally.
```

```{toctree}
:maxdepth: 1

abstract_plugin_factories_model
plugin_factories_tree_model
plugin_factories_list_model
plugin_factories_filter_model
```