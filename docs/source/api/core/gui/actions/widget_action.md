# Widget action

`WidgetAction` is the common state, widget-creation, parameter-sharing, settings, and serialization base for ManiVault action controls. Prefer a concrete typed action in plugin code and consult this class for behavior shared across all action types.

For practical lifecycle and persistence patterns, see the {doc}`plugin actions and settings guide <../../../../development/building_plugins/actions/index>`.

```{doxygenclass} mv::gui::WidgetAction
:members:
:protected-members:
```
