# Heads-up-display

A **heads-up-display** is used by **ManiVault** to overlay (textual) information on view plugins. The model classes below are for storing and filtering {cpp:class}`heads-up-display items <mv::util::HeadsUpDisplayItem>`.

```{note}
This API is considered a **WIP**. Plugin developers typically do not need to interact with the models directly as it is wrapped by the {cpp:class}`heads-up-display action <mv::gui::ViewPluginHeadsUpDisplayAction>`. This action is a member of the {cpp:class}`view plugin <mv::plugin::ViewPlugin>`: {cpp:func}`viewPlugin->getHeadsUpDisplayAction() <mv::plugin::ViewPlugin::getHeadsUpDisplayAction>`.
```

```{toctree}
:maxdepth: 1

abstract_heads_up_display_model
heads_up_display_list_model
heads_up_display_filter_model
```