# QObject lifetime and ownership

Qt parentage and C++ storage duration are separate mechanisms. Choose both deliberately.

## Common patterns

| Pattern | Appropriate when |
| --- | --- |
| QObject member, optionally parented to `this` | Fixed helper whose lifetime exactly matches the enclosing object and which is never reparented or deferred-deleted |
| `new Child(this)` | Dynamically created child that the parent should delete |
| Unparented object with explicit C++ ownership | A non-Qt owner such as `std::unique_ptr` controls a fixed-thread object |
| Borrowed raw pointer or reference | The owner is unambiguous and the pointer is used only within its guaranteed lifetime |
| `QPointer<T>` | A QObject may disappear independently and observers need automatic nulling |
| ManiVault `Dataset<T>` | Code retains a non-owning, invalidation-aware dataset handle |

Never infer ownership from a raw pointer alone. Document whether an API stores, borrows, reparents, or deletes the object.

## QObject members in ManiVault

ManiVault commonly embeds actions, models, timers, and other helpers as members:

```cpp
class ExampleViewPlugin final : public mv::plugin::ViewPlugin
{
    Q_OBJECT

public:
    explicit ExampleViewPlugin(
        const mv::plugin::PluginFactory* factory);

private:
    mv::gui::ToggleAction _showLabelsAction;
    QTimer                _refreshTimer;
};

ExampleViewPlugin::ExampleViewPlugin(
    const mv::plugin::PluginFactory* factory) :
    ViewPlugin(factory),
    _showLabelsAction(this, "Show labels"),
    _refreshTimer(this)
{
}
```

This is safe because members are destroyed before the enclosing QObject base destructor. A member parented to the enclosing object removes itself from that parent's child list during its own destruction.

The pattern remains safe only while the member:

- is never reparented;
- is never deleted directly or through `deleteLater()`;
- is not handed to an API that takes ownership;
- is not moved to another thread;
- does not need to outlive the enclosing object;
- cannot be destroyed independently of the enclosing object.

Parenting a member to `this` supports QObject ancestry and connection cleanup, but C++ member lifetime remains authoritative. If any code may reparent or delete it, use a heap-allocated child instead.

## Association is not necessarily ownership

Many APIs merely retain a pointer. Examples in ManiVault include `GroupAction::addAction()`, hierarchy attached actions, popup actions, and status-bar menu actions. Qt's `QWidget::addAction(QAction*)` and `QMenu::addAction(QAction*)` also associate an existing action without promising ownership transfer.

Other APIs do change parentage. A widget placed in a widget layout is normally reparented to the layout's containing widget, and an explicit `setParent()` changes QObject ownership. Constructors that create and return a new action may have a different contract from overloads accepting an existing action.

Check the exact overload and keep the original owner alive. Do not parent one member object to another component merely because that component displays it.

## Heap allocation

Use a parent-owned heap object when the number of children is dynamic, the object must participate in ownership transfer, or independent destruction is part of the design:

```cpp
auto* dialog = new DetailsDialog(&getWidget());
dialog->setAttribute(Qt::WA_DeleteOnClose);
dialog->open();
```

Retain such an independently closing object through `QPointer` when callbacks or commands may refer to it later.

Heap allocation alone does not solve lifetime problems. It still needs one clear deleter: a QObject parent, explicit C++ ownership, or a documented `deleteLater()` chain—never several competing owners.
