# Defining and registering an item

## Derive a typed action

A plugin-specific subclass keeps inline and popup actions together and gives plugin code typed access to them:

```cpp
#include <actions/PluginStatusBarAction.h>
#include <actions/StringAction.h>
#include <actions/VerticalGroupAction.h>

class ExampleStatusBarAction final
    : public mv::gui::PluginStatusBarAction
{
public:
    ExampleStatusBarAction(QObject* parent, const QString& pluginKind) :
        PluginStatusBarAction(parent, "Example status", pluginKind),
        _summaryAction(this, "Summary", "Ready"),
        _detailsAction(this, "Example details")
    {
        setToolTip("Inspect Example plugin status");

        _summaryAction.setEnabled(false);
        _summaryAction.setDefaultWidgetFlags(
            mv::gui::StringAction::Label);

        getBarGroupAction().addAction(&_summaryAction);
        setPopupAction(&_detailsAction);
    }

    mv::gui::StringAction& getSummaryAction()
    {
        return _summaryAction;
    }

private:
    mv::gui::StringAction        _summaryAction;
    mv::gui::VerticalGroupAction _detailsAction;
};
```

Inline actions belong in `getBarGroupAction()`. The bar group suppresses labels by default and uses compact margins, so select child widget flags that remain legible at status-bar height.

## Register during factory initialization

Create, configure, and register the action before the main window constructs its status bar:

```cpp
void ExampleViewPluginFactory::initialize()
{
    ViewPluginFactory::initialize();

    auto* statusBarAction =
        new ExampleStatusBarAction(this, getKind());

    statusBarAction->setIndex(-1);
    setStatusBarAction(statusBarAction);
}
```

The action requires a valid, already loaded plugin kind. It uses that factory for its icon and instance count.

The factory stores a raw pointer; `setStatusBarAction()` does not reparent or take ownership. Parent the action to the factory so it remains alive for the complete application session.

## Registration timing

During main-window initialization, the core enumerates loaded plugin factories, reads each registered status-bar action, and creates its widget. It does not currently listen to `statusBarActionChanged()` to insert or remove widgets later. Consequently:

- register in the factory's `initialize()` implementation;
- configure index and stretch before the main window is shown;
- do not replace the registered action dynamically;
- do not use `setStatusBarAction(nullptr)` as a runtime removal mechanism.

Change the existing action's visibility, enabled state, text, badge, or child values when its runtime presentation must change.
