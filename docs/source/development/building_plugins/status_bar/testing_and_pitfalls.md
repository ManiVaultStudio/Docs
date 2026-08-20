# Testing and pitfalls

## Verification checklist

Test status-bar integration with:

- no project, a new project, and a restored project;
- the application status bar enabled and disabled;
- zero, one, and several plugin instances;
- creation and removal of the last plugin instance;
- failed plugin creation and bulk project teardown;
- every inline control, menu command, and popup action;
- long and empty text, large counts, and narrow windows;
- disabled actions and warning-to-info severity transitions;
- light and dark themes and high-DPI scaling;
- workflow completion, failure, cancellation, and rapid restart;
- plugin destruction while asynchronous work is completing.

## Common pitfalls

### The item never appears

Register it in the factory's `initialize()` method, before main-window status-bar construction. Confirm that the plugin kind is valid, a project is open, the application status bar is enabled, and conditional visibility agrees with the current instance count.

### Changing the factory pointer has no visible effect

The main window does not dynamically insert or remove plugin status-bar widgets when `statusBarActionChanged()` is emitted. Configure one long-lived action at startup and mutate its state or visibility instead.

### The item is in an unexpected position

Call `setIndex()` before the main window is shown. Zero appends at the right, negative values insert relative to the right, and positive values insert from the left. Test alongside the core's built-in items; their number and stretch factors affect the final layout.

### The last instance leaves stale status

Recompute from the authoritative plugin collection or factory count, and test the final-destruction transition explicitly. Do not retain an instance pointer in the factory-owned action.

### The status bar becomes crowded

Remove labels that repeat an icon or tooltip, combine related values, and move detail into a popup. If content belongs to one view, move it into that view instead of competing for application-wide space.

### Progress is duplicated

Use workflows and tasks for operation progress. A plugin status item should add a distinct aggregate or persistent service state, not echo the same task percentage.

### A transient message disappears incorrectly

Avoid overlapping `StatusAction::setMessage(..., true)` timers. Use a notification for a brief user-facing event or logging for reviewable history.

### A popup or menu action crashes after teardown

`setPopupAction()` and `addMenuAction()` keep non-owning pointers. Parent supplied actions to the status-bar action or another equally long-lived owner, and remove dynamically destroyed menu actions first.
