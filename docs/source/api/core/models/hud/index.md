# Heads-up-display

A **heads-up-display** is used by **ManiVault** to overlay (textual) information on view plugins. The model classes below are for storing and filtering {cpp:class}`mv::util::HeadsUpDisplayItem`.

```{note}
This API is considered a **WIP**. Plugin developers typically do not need to interact with the models directly as it is wrapped by the {cpp:class}`mv::gui::ViewPluginHeadsUpDisplayAction`. This action is a member of the {cpp:class}`mv::plugin::ViewPlugin`: {cpp:func}`mv::plugin::ViewPlugin::getHeadsUpDisplayAction`.
```

```{toctree}
:maxdepth: 1

abstract_heads_up_display_model
heads_up_display_tree_model
heads_up_display_filter_model
```