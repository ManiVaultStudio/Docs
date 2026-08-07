# How actions work

The action object is the source of truth. A generated widget observes and updates that object; it does not own a separate copy of the parameter.

```text
plugin logic  <->  action state  <->  one or more widgets
                          |
                          +-> serialization and settings
                          +-> optional shared-parameter connection
```

This model has several practical consequences:

- changing the action programmatically updates its widget representations;
- user interaction changes the action and emits its signals;
- multiple widgets created from one action remain synchronized;
- enabled, visible, and read-only behavior can be controlled centrally;
- serialization operates on the action, not on QWidget state;
- a compatible public-action connection can synchronize state across plugins.

Actions also form a QObject hierarchy. Group actions use child actions to compose layouts and menus, while the core can use ownership and location information for discovery and parameter sharing. Visual grouping does not automatically decide which children a plugin persists; project serialization remains explicit.

Continue with {doc}`Action ownership and lifecycle <lifecycle>` for the construction pattern and {doc}`Saving and restoring action state <serialization>` for persistence.
