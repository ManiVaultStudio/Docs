# Action ownership and lifecycle

Treat an action as the long-lived model for a control, not as the control widget itself. The usual plugin lifecycle is:

1. Construct actions as plugin members.
2. Configure ranges, options, defaults, tooltips, and connections.
3. Create widget representations in `Plugin::init()`.
4. Restore project state into the already-existing actions.
5. Let QObject ownership destroy actions with the plugin.

## Prefer member actions

Member actions have a stable lifetime, exist when project restoration occurs, and can safely be referenced by signal connections:

```cpp
class ExampleViewPlugin : public mv::plugin::ViewPlugin
{
    Q_OBJECT

public:
    ExampleViewPlugin(const mv::plugin::PluginFactory* factory);
    void init() override;

private:
    mv::gui::DecimalAction _pointSizeAction;
    mv::gui::ToggleAction  _showLabelsAction;
};

ExampleViewPlugin::ExampleViewPlugin(const PluginFactory* factory) :
    ViewPlugin(factory),
    _pointSizeAction(this, "Point size"),
    _showLabelsAction(this, "Show labels")
{
    _pointSizeAction.setToolTip("Size used to draw each point");
}
```

Passing `this` as the QObject parent ties the actions to the plugin. The action registers with the core action manager when it is constructed in an initialized core and unregisters when destroyed.

These actions are C++ members as well as QObject children. This is an intentional ManiVault pattern with strict non-reparenting and non-deferred-deletion rules; see {doc}`QObject lifetime and ownership <../qt_considerations/qobject_ownership>`.

Avoid temporary actions whose widgets or callbacks outlive them. When an action must be allocated dynamically, give it an appropriate QObject owner and retain a clear path to it.

## Create widgets in `init()`

An action can create multiple synchronized widgets. Build the plugin UI from the existing action members in `init()`:

```cpp
void ExampleViewPlugin::init()
{
    auto* layout = new QVBoxLayout();
    layout->addWidget(_pointSizeAction.createWidget(&getWidget()));
    layout->addWidget(_showLabelsAction.createWidget(&getWidget()));
    getWidget().setLayout(layout);
}
```

Creating a widget does not transfer ownership of the action or create a second setting. Every representation reads and changes the same action state.

## Configure before restoration

Populate option lists, ranges, filters, and signal connections during construction so the action is ready before serialized values are applied. Do not replace a member action during restoration; restore state into the existing instance.

Visual details belong to widget creation and {doc}`widget customization <customizing>`. Persistent identity and value semantics belong to the action itself.
