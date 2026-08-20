# Content and interaction

## Inline actions

Add compact `WidgetAction` children to `getBarGroupAction()`:

```cpp
getBarGroupAction().addAction(&_stateAction);
getBarGroupAction().addAction(&_countAction);
getBarGroupAction().addAction(&_refreshAction);
```

Prefer a short label, icon-only trigger, toggle, progress summary, or badge. Disable a display-only action so it does not suggest editability, and give every interactive action a tooltip and accessible title.

If the status-bar action has an icon, `getBarIconStringAction()` exposes the icon-bearing string action. Its badge can carry a small count:

```cpp
auto& badge = getBarIconStringAction().getBadge();
badge.setEnabled(numberOfPendingItems > 0);
badge.setNumber(numberOfPendingItems);
```

Use badges for small, quickly interpreted quantities. Put the exact meaning in the status item's tooltip or popup.

## Popup content

Assign one action as the main popup:

```cpp
setPopupAction(&_detailsAction);
_detailsAction.setPopupSizeHint(QSize(420, 260));
```

The popup action remains owned by its existing QObject parent; `setPopupAction()` stores a pointer and configures the status-bar tool button. Parent it to the status-bar action or another object with the same lifetime.

Use a group, hierarchy, or list action when details need structure. Keep destructive or ambiguous commands out of a click target that users may invoke accidentally.

## Menu actions

Menu commands can be added and removed independently:

```cpp
addMenuAction(&_openPluginAction);
addMenuAction(&_clearAction);
```

`addMenuAction()` does not establish QObject ownership. Keep each menu action alive until it is removed or the status-bar action is destroyed. Call `removeMenuAction()` before destroying a dynamically owned command.

## StatusAction

`StatusAction` represents an informational message with `Undefined`, `Info`, `Warning`, or `Error` severity and renders it in a disabled line edit. It can be placed inside a status-bar group, but the class is explicitly marked work in progress. Prefer a `StringAction` for a simple stable summary unless the severity presentation is useful and tested for every transition.

`setMessage(message, true)` clears the message after the built-in 1.5-second interval. Avoid rapid overlapping transient messages: an earlier timer can clear a newer message. Notifications or logging are better for events that users may need to notice or review.

## Progress and long-running operations

Do not execute work from the status-bar update itself. For new substantial operations, use the {doc}`workflow-backed execution path <../tasks/choosing_an_execution_model>`. The core background-tasks item already aggregates task progress and exposes task details.

A plugin status-bar item may summarize a persistent queue or service state, but the workflow result remains authoritative for success, failure, cancellation, and diagnostics.
