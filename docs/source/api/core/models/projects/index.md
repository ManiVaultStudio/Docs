# Projects

**ManiVault** manages the lifetime of projects through the {cpp:class}`mv::AbstractProjectManager`. Projects are tracked in dedicated **list** and **tree** models, which are primarily used by the UI. The model classes below are for storing and filtering projects.

```{note}
This API is **stable** and intended for use by **core developers**. Plugin developers typically do not need to interact with it directly, as it is fully wrapped by the projects manager.
```

```{toctree}
:maxdepth: 1

abstract_projects_model
projects_tree_model
projects_list_model
projects_filter_model
projects_model_visibility_controller
abstract_projects_model
```

