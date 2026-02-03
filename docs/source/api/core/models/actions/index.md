# Actions
 
Actions are re-usable GUI building blocks. During their lifetime, actions are tracked in a global {cpp:class}`actions manager <mv::AbstractActionsManager>` with the use of dedicated actions models. The classes below are used to store, present and filter actions.

```{toctree}
:maxdepth: 1

abstract_actions_model
actions_hierarchy_model
actions_list_model
actions_filter_model
```

```{note}
This API is **stable** and intended for use by **core developers**. Plugin developers typically do not need to interact with it directly, as it is fully wrapped by the actions manager.
```