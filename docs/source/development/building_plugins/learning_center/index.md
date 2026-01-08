Learning Center
===============

The **Learning Center** provides **contextual, plugin-specific guidance** while users work with ManiVault.

Instead of a static help system, it surfaces **just-in-time information** that is relevant to the currently available plugins, views, and interactions.

![Learning center](../../assets/learning_center.gif)

*The Learning Center provides plugin-specific onboarding content.*

---

## Purpose

The Learning Center is designed to:

- Support **onboarding** for new users
- Improve **discoverability** of features and shortcuts
- Provide **consistent guidance** across plugins

It complements full documentation by focusing on **practical usage** rather than exhaustive explanations.

---

## Plugin-driven content

Learning Center content is **defined by plugins** through their plugin factories.

Plugins can contribute:
- Metadata (contributors, affiliations)
- Summaries of **keyboard and mouse shortcuts**
- Links to additional documentation or tutorials

This ensures that guidance is relevant, accurate, and closely aligned with plugin behavior.

---

## Design principles

The Learning Center is:

- **Contextual** — scoped to a specific plugin or interaction
- **Non-intrusive** — it does not interrupt workflows
- **Optional** — consulted when needed

It is intended for both first-time users and experienced users who need a quick reference.

---

## Responsibilities

- **Plugins** define Learning Center content
- **Plugin factories** register Learning Center actions
- The **core** handles presentation and integration

Content is lightweight and does not affect plugin behavior.

---

## Summary

- The Learning Center provides contextual, plugin-specific guidance
- Content is supplied by plugins and registered via their factories
- Shortcut summaries are a core feature
- UI integration and lifecycle are handled by the core

The Learning Center helps users learn *what matters, when it matters*.

```{toctree}
:maxdepth: 1

shortcuts
