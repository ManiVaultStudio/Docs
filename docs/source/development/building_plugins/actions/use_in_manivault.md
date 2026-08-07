# What actions enable in ManiVault Studio

Actions provide more than a uniform collection of widgets. Their shared state model lets the core and plugins reason about parameters without depending on a particular UI representation.

## Consistent plugin interfaces

Concrete actions provide standard controls, validation, tooltips, enabled and visible state, and widget variants. The same action can appear in a settings panel, toolbar, collapsed popup, or group while retaining one value.

## Project state

Actions implement ManiVault's serialization contract, making them natural units of plugin state. A plugin still chooses which instance actions belong in a project and includes those actions explicitly in its serialization overrides. See {doc}`Saving and restoring action state <serialization>`.

## Shared parameters

Private actions can be published and connected to compatible public actions. Once connected, action state can be synchronized between plugins without either plugin knowing the other's concrete implementation.

Publishing is an intentional operation, not an automatic consequence of creating an action. Connection permissions and Studio mode determine which publishing, connecting, and disconnecting operations are available through the UI or API.

Keep serialization identity separate from the public name shown to users: a serialization name is a persistent storage key, while the publication name identifies a shared parameter.

## Discoverable operations

Actions can also expose capabilities outside a plugin's main settings panel. Group and trigger actions are commonly embedded in toolbars, context menus, dataset-oriented interfaces, and other plugins. QObject ownership remains with the component that implements the behavior; consumers create or present a suitable widget or menu representation.

This separation makes actions useful as small integration points: the producer owns state and behavior, while a consumer decides where and how to present it.
