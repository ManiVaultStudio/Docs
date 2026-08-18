# Notifications and status

For plugin-originated messages, prefer `Plugin::addNotification()`. It supplies the plugin name and icon automatically:

```cpp
addNotification(
    tr("The selected dataset contains no usable dimensions."),
    mv::util::Notification::DurationType::Calculated);
```

Use `Fixed` for a short predictable display, and `Calculated` when reading time should follow message length. Task-backed notifications are created from a `Task`; setting `DurationType::Task` on an ordinary text notification does not associate a task with it.

Use the global `mv::help().addNotification(...)` only when the message belongs to the application or another non-plugin service and therefore needs an explicit title and icon.

## Notifications are not failure control flow

Showing a notification does not abort an operation, mark a task failed, or prevent invalid state. Perform the required control-flow action separately:

```cpp
if (!_input.isValid()) {
    addNotification(tr("The input dataset is no longer available."));
    return;
}
```

Avoid repeated notifications inside loops, polling callbacks, or rapidly emitted value signals. Aggregate repeated issues or notify once when the operation completes.

## Persistent status

`StatusAction` represents an info, warning, or error message inside an action-based interface. `PluginStatusBarAction` is for compact plugin-kind state in the application status bar and can appear only while instances of that plugin exist.

Neither is a substitute for operation progress. For new long-running work, prefer workflow-backed execution and project its progress into a task when GUI feedback is needed. Manage a task directly only when execution is already owned elsewhere. See {doc}`Choosing an execution model <../tasks/choosing_an_execution_model>` and {doc}`Status bar integration <../status_bar>`.
