# Data hierarchy models

These models present and filter the project data hierarchy for specialized Qt item views. Most plugin code should use `Dataset<T>`, `DataHierarchyItem`, and `mv::dataHierarchy()` directly.

For guidance on when to use a model and how to avoid duplicating hierarchy state, see {doc}`Building a custom hierarchy view <../../../../development/building_plugins/data/hierarchy/custom_views>`.

```{toctree}
:maxdepth: 1

abstract_data_hierarchy_model
data_hierarchy_tree_model
data_hierarchy_filter_model
```

`ActionsListModel` is an actions model and is documented separately from the hierarchy model family.
