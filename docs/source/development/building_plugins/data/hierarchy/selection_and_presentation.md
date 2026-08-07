# Selection and presentation state

Hierarchy items store row selection, visibility, expansion, and a facade over dataset locking. These states serve different purposes.

## Select hierarchy rows

Select one or more rows through the manager:

```cpp
auto* first  = mv::dataHierarchy().getItem(firstDataset.getDatasetId());
auto* second = mv::dataHierarchy().getItem(secondDataset.getDatasetId());

mv::DataHierarchyItems items;
if (first)
    items << first;
if (second)
    items << second;

mv::dataHierarchy().select(items); // clears the previous row selection
```

Pass `false` as the second argument to add to the current selection. `clearSelection()`, `selectAll()`, and `getSelectedItems()` provide hierarchy-wide operations. Observe `selectedItemsChanged(...)` when a component follows application row selection.

Element selection inside a dataset uses its selection dataset and `DatasetDataSelectionChanged`; see {doc}`Selections and linked data <../selections_and_linked_data>`.

## Visibility

`DataHierarchyItem::setVisible(visible, recursively)` controls appearance in the hierarchy UI:

- hiding an item deselects it;
- recursive hiding also hides descendants;
- showing an item ensures its ancestors are visible;
- recursive showing also shows descendants.

The recursive argument defaults to `true`. Pass `false` for a targeted change, understanding that ancestors may still be shown to make a visible child reachable.

## Expansion

`setExpanded()` records whether a branch is expanded in hierarchy views. It does not change visibility, load or unload data, or affect descendants. Observe `expandedChanged(...)` when implementing a view that mirrors item state.

## Locking

The item's lock methods forward to the dataset. Locking is operational state used to protect data while work is in progress; it is not an access-control mechanism. The optional cache flag supports temporarily changing lock state and later calling `restoreLockedFromCache()`.

Prefer scoped operation utilities where available so every exit path restores locking correctly.
