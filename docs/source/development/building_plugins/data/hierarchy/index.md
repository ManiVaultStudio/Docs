# Interacting with the data hierarchy

The data hierarchy is ManiVault's project-wide tree of registered datasets. Each dataset has one `DataHierarchyItem` that stores presentation state and connects the dataset to hierarchy views, selection, attached actions, and context menus.

## Choose the right abstraction

| Need | Use |
| --- | --- |
| Read semantic dataset relationships | `Dataset<T>` methods such as `getParent()` and `getChildren()` |
| Find or select rows across the application hierarchy | `mv::dataHierarchy()` |
| Change visibility, expansion, or row selection | `DataHierarchyItem` |
| Offer a dataset-specific operation | Attach a long-lived `WidgetAction` to the item |
| Build a specialized hierarchy view | Hierarchy tree and filter models |

```{important}
Hierarchy selection selects dataset rows in the application interface. It does not change the elements selected inside any dataset.
```

```{toctree}
:maxdepth: 1

navigating
selection_and_presentation
parenting_and_lifetime
attached_actions
custom_views
```

Hierarchy placement describes presentation and navigation. For derived, full, subset, and proxy relationships, continue with {doc}`Hierarchy, derived data, and subsets <../hierarchy_derived_and_subsets>`.

For exact signatures, see the {doc}`hierarchy manager API <../../../../api/core/managers/abstract_data_hierarchy_manager>` and {doc}`DataHierarchyItem API <../../../../api/core/data/data_hierarchy_item>`.
