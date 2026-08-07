# Attached actions and context menus

A hierarchy item can expose dataset-specific operations by attaching `WidgetAction` objects. The hierarchy UI incorporates each attached action's context menu.

```cpp
_exportAction.setToolTip("Export this dataset");

dataset->getDataHierarchyItem().addAction(_exportAction);
```

An attached action should describe behavior owned by your plugin or data implementation. `TriggerAction`, grouped actions, and settings actions can expose commands or controls without coupling the hierarchy UI to the implementing component.

`getActions()` returns the attached actions. `getContextMenu()` creates a menu containing their context menus, while `populateContextMenu(menu)` adds them to an existing menu. Actions configured with `WidgetAction::ConfigurationFlag::HiddenInActionContextMenu` are skipped.

## Ownership is not transferred

`addAction()` stores a non-owning pointer. The hierarchy item does not take QObject ownership and does not provide a public removal operation. Attach only an action guaranteed to outlive the hierarchy item.

This usually means:

- a dataset-owned action attached to that dataset's item; or
- another action whose owner and teardown ordering guarantee that the dataset is removed first.

Attaching an ordinary plugin-instance member to a dataset that may outlive the plugin can leave a dangling pointer. When the lifetimes do not naturally align, expose the operation through plugin triggers or another discovery mechanism instead.

## Keep callbacks removal-safe

An action callback should retrieve or validate its target dataset when invoked:

```cpp
connect(&_exportAction, &QAction::triggered, this, [this]() {
    if (!_dataset.isValid())
        return;

    exportDataset(_dataset);
});
```

Disable or hide the action when the operation is unavailable, and detach plugin state during the dataset's `aboutToBeRemoved` phase.
