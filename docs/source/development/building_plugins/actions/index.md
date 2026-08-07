# Plugin actions and settings

Actions are ManiVault's reusable controls for plugin parameters and commands. An action owns state independently of any one widget, emits typed change signals, can create one or more widget representations, and participates in persistence and parameter sharing.

## Recommended path

For a new plugin, begin with the lifecycle and change-handling pages. Continue with project serialization before relying on restored settings. The final pages cover application-wide settings and visual composition.

```{toctree}
:maxdepth: 1

what_are_actions
how_actions_work
lifecycle
reacting_to_changes
serialization
settings_scopes
use_in_manivault
adding
customizing
```

For exact signatures and the catalogue of concrete controls, see the {doc}`actions API reference <../../../api/core/gui/actions/index>`.
