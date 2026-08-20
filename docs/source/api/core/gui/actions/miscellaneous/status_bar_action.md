# StatusBarAction

**Qualified name:** `mv::gui::StatusBarAction`

`StatusBarAction` is the application-level base for a compact inline action group with optional popup and menu content. Construction registers the action in the core's live status-action collection; destruction removes it.

Plugin factories normally register the specialized {doc}`PluginStatusBarAction <plugin_status_bar_action>`. See {doc}`Status-bar integration <../../../../../development/building_plugins/status_bar/index>` for startup timing, positioning, ownership, and content guidance.

```{doxygenclass} mv::gui::StatusBarAction
:members:
:protected-members:
```
