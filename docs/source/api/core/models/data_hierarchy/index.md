# Data Hierarchy

The data hierarchy represents the structured organization of data elements within **ManiVault**, typically exposed as tree or list views in the UI. The classes below are used to store, present, and filter data hierarchy elements.

```{note}
This API is **stable** and intended for use by **core developers**. Plugin developers typically do not need to interact with it directly, as it is fully wrapped by the {cpp:class}`data hierarchy manager <mv::AbstractDataHierarchyManager>`.
```

```{toctree}
:maxdepth: 1

abstract_data_hierarchy_model
data_hierarchy_tree_model
data_hierarchy_list_model
data_hierarchy_filter_model
```