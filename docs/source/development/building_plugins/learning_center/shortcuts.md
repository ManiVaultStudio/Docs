# Documenting plugin shortcuts

`PluginShortcuts` is a facade over the shortcut map stored in the factory's metadata. The map drives the categorized shortcut dialog and the shortcut count in a view's Learning Center overlay.

```{important}
Adding an entry to the shortcut map does not install a keyboard shortcut. Bind the shortcut to an action or handle the input separately, then document that existing behavior in the map.
```

## Bind and document the same sequence

```cpp
ExampleViewPlugin::ExampleViewPlugin(
    const mv::plugin::PluginFactory* factory) :
    ViewPlugin(factory),
    _selectAllAction(this, "Select all")
{
    const QKeySequence selectAll(QKeySequence::SelectAll);

    _selectAllAction.setShortcut(selectAll);
    _selectAllAction.setShortcutContext(Qt::WidgetWithChildrenShortcut);
    getWidget().addAction(&_selectAllAction);

    getShortcuts().add({ selectAll, "Selection", "Select all points" });
}
```

The Qt action performs the behavior; `getShortcuts().add()` adds the user-facing reference. Choose the narrowest appropriate `Qt::ShortcutContext` so the key sequence does not unexpectedly affect other views.

Use `QKeySequence::StandardKey` values such as `SelectAll`, `Copy`, or `Save` when the operation has a platform-standard binding. For plugin-specific keys, construct the sequence explicitly:

```cpp
getShortcuts().add({
    QKeySequence(Qt::Key_R),
    "Selection tools",
    "Activate rectangle selection"
});
```

## Factory-wide map

The underlying map belongs to `PluginMetadata`, so it is shared by all instances of one plugin kind. Stable shortcut documentation may be registered directly in the factory constructor:

```cpp
auto& shortcuts = getPluginMetadata().getShortcutMap();

shortcuts.addShortcut({
    QKeySequence(Qt::Key_R),
    "Selection tools",
    "Activate rectangle selection"
});
```

Using the instance facade is also valid and is common when the binding is established by that instance. Exact duplicate entries are ignored. Remember that removing an entry through one instance changes the shared map for every instance.

View plugins already document the standard F2 screenshot and F12 editor shortcuts; ordinary non-system views also document F3 view isolation. Do not add duplicate descriptions for those base-class bindings.

## Categories and wording

Use a small set of stable, task-oriented categories such as `Selection`, `Navigation`, `Rendering`, or `General`. Category spelling and capitalization determine grouping, so `Selection` and `selection` become separate groups.

Describe the result, not the implementation. Prefer “Zoom to the current selection” over “Call zoomSelection()”. If a shortcut modifies a mouse interaction, state both parts, for example “Shift + left drag — add points to selection.”

## Dynamic shortcuts

Only document a shortcut while it is actually available. If a mode enables or changes a binding, add and remove the matching `ShortcutMap::Shortcut` together with that mode. Store the exact shortcut value so removal uses the same key sequence, category, and title; equality compares all three fields.

Avoid instance-specific descriptions in the shared map. If two live instances can expose different bindings, standardize the keys or design a separate instance-local explanation instead of presenting one factory-wide map as universally true.

See the {doc}`PluginShortcuts API <../../../api/core/plugin/plugin_shortcuts>` and {doc}`ShortcutMap API <../../../api/core/util/shortcut_map/shortcut_map>` for filtering, categories, signals, and removal.
