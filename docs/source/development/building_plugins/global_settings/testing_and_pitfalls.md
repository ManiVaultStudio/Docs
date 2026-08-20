# Testing and pitfalls

## Verification checklist

Test global settings with:

- a clean application settings store;
- a previously stored value and a full application restart;
- zero, one, and several active plugin instances;
- a settings change while instances and projects are open;
- project save and restore on an installation with different global defaults;
- missing and malformed UI-less values;
- old serialization names or paths when migration is supported;
- plugin unload or application shutdown;
- rapid repeated changes when a setting starts asynchronous work;
- light and dark themes, long labels, and narrow settings-dialog layouts.

## Common pitfalls

### The setting appears but is not restored

Ensure the child action is parented to the global settings group and has its serialization name before `addAction()`. The group assigns persistence only to actions in its QObject child hierarchy.

### A stored preference always returns to its default

Do not set the default again after `addAction()` has loaded stored state. Also confirm that the plugin kind and action serialization name have not changed.

### Existing instances do not update

Registration provides persistence and settings-dialog presentation; it does not define plugin behavior. For a live policy, each instance must apply the current value and observe the child action's change signal.

### Existing instances update when they should not

A default for new instances should be copied once into instance-owned state. Do not connect it as a live policy, and serialize the local value with the project.

### One project changes behavior in another project

The value is probably global when it should be instance or project state. Move the authority to an instance-owned action and project serialization rather than duplicating it in both places.

### UI-less settings disagree between instances

`getSetting()` and `setSetting()` provide storage, not notification. Introduce an action or a dedicated shared object with a change signal if active instances must synchronize immediately.

### The factory leaks or loses its settings group

`setGlobalSettingsGroupAction()` stores a raw pointer. Parent the group to the factory, as in `new ExampleGlobalSettingsAction(this, this)`, so their lifetimes match.

### A settings change freezes the interface

Do not perform substantial work directly in a value-change handler. Use the workflow engine for long operations, or a task when only progress and cancellation integration are needed. See {doc}`Tasks and workflows <../tasks/index>`.
