# Testing and common pitfalls

Learning content crosses plugin, UI, network, and project-lifecycle boundaries. Verify it as part of the plugin rather than treating it as an external website concern.

## Verification checklist

- Open the plugin with the network available and unavailable.
- Check that documentation appears only when the help trigger works.
- Open the README, repository, about dialog, tutorials, and videos from every advertised entry point.
- Verify tutorial tags using their exact spelling and capitalization.
- Confirm tutorial project URLs and every name in the required-plugin list.
- Test custom GIF resources in an installed build, not only from the build tree.
- Confirm every shortcut both performs the documented behavior and appears in the intended category.
- Test shortcut scope with two view plugins focused in turn.
- Inspect the overlay on small views and after docking, floating, resizing, and replacing its target widget.
- Save and restore a project with non-default overlay visibility and alignment.

## Common pitfalls

### The help button does nothing

Returning `true` from `hasHelp()` only makes the entry visible. Connect `getPluginMetadata().getTriggerHelpAction()` to a working viewer and validate its source URL.

### The README URL points to a missing branch

The base `getDefaultBranch()` returns `master`. Override it when the repository uses `main`, or override `getReadmeMarkdownUrl()` with the exact documentation location.

### A shortcut appears but does not work

The shortcut map is documentation only. Install the same `QKeySequence` on a Qt action or implement the input handling, and choose an appropriate shortcut context.

### A shortcut works in the wrong view

Application-wide shortcuts are active beyond one plugin instance. Prefer `Qt::WidgetShortcut` or `Qt::WidgetWithChildrenShortcut` for view-local operations and associate the action with the relevant widget.

### Content is missing despite matching tags

Tag lookup is case-sensitive and remote catalogs are asynchronous. Check when the association runs, inspect the global models, and confirm that at least one supplied tag matches. Multiple supplied tags are alternatives, not an all-tags requirement.

### Content appears more than once

Instance association methods append entries. Call them once or compare against the current association before adding later asynchronous results. Tutorial titles are deduplicated globally, but plugin associations and global video registration should still be managed deliberately.

### A tutorial or video pointer becomes invalid

The plugin action does not own associated content. Register shared objects with `mv::help()` so the global model owns them, or provide an explicitly longer-lived owner.

### The overlay covers plugin controls

Target the central content widget and choose a corner that does not obscure primary interaction. Do not work around overlap with hard-coded pixel offsets; alignment and target geometry are already managed by the overlay.

## Content quality

Keep tutorials task-oriented and version-aware. Prefer a short path to a successful result, followed by optional detail. Videos should have a descriptive title and summary so users can decide whether opening them is worthwhile. Shortcut descriptions should state the visible outcome and stay synchronized with the actual interaction.

When the plugin behavior changes, review code, README, tutorial feeds, tutorial projects, videos, and shortcut descriptions together. Stale onboarding is often more confusing than absent onboarding.
