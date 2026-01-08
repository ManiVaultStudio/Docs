Learning center
==================

The **Learning Center** is ManiVault’s central mechanism for providing **contextual, plugin-specific guidance** to users while they work with the application.

Rather than acting as a static help system, the Learning Center surfaces **just-in-time information** that is directly relevant to the plugins, views, and interactions available in the current context.

![Learning center](../../assets/learning_center.png)

*The learning Center provides plugin specific onboarding content.*


---

## Purpose and scope

The Learning Center is designed to:

- Support **onboarding** by helping new users understand plugins and interactions.
- Improve **discoverability** of features, shortcuts, and interaction patterns.
- Provide **consistent guidance** across all plugins.

It complements full documentation and tutorials by focusing on **practical usage** and **immediate interaction**, rather than exhaustive explanations.

---

## Plugin-driven content

Learning Center content is **defined and owned by plugins** through their plugin factories.

Each plugin can contribute:
- Meta data such as contributors and their affilitations
- A summary of relevant **keyboard and mouse shortcuts**
- Optional references to additional documentation or tutorials

This approach ensures that:
- Only relevant content is shown to the user
- Guidance reflects the actual capabilities of installed plugins
- Documentation remains close to the code that defines behavior

---

## Contextual and non-intrusive design

The Learning Center is intentionally designed to be:

- **Contextual** — scoped to a specific plugin or interaction
- **Non-intrusive** — it does not interrupt ongoing workflows
- **Optional** — users consult it when needed

This makes it equally useful for first-time users and experienced users who need a quick reminder.

---

## Responsibilities and lifecycle

- **Plugins** define the content shown in the Learning Center.
- **Plugin factories** register Learning Center actions during initialization.
- The **core** handles presentation, layout, and integration into the application UI.

Learning Center content is lightweight and static. It does not affect plugin behavior and can be extended safely as plugins evolve.

---

## Summary

- The Learning Center provides contextual, plugin-specific guidance.
- Content is supplied by plugins and registered via their factories.
- Shortcut summaries are a first-class feature.
- Presentation and lifecycle are handled by the core.
- The Learning Center improves usability without adding UI complexity.

By keeping guidance close to the plugins that define behavior, the Learning Center helps users learn *what matters, when it matters*.


```{toctree}
:maxdepth: 1

shortcuts
