---
name: manivault-docs-sync
description: Audit and synchronize the ManiVault documentation with current project functionality and authoritative upstream sources. Use when asked to sync, update, review, or find gaps in ManiVault documentation.
---

# ManiVault documentation synchronization

Use this skill for documentation maintenance across the entire ManiVault Docs site: user guides, plugin and application development guides, parallel execution and workflow guides, and the API reference. Python/Jupyter is one specialized area, not the boundary of the skill. Unless the user explicitly asks for an audit or review only, audit first and then make the necessary updates.

## Workflow

1. Read `AGENTS.md`, inspect the site configuration and toctrees, and check `git status`. Preserve unrelated changes.
2. Define the review scope. For a named topic, trace its local pages and cross-references. For a broad "sync the docs" request, survey the site navigation and page inventory across user guides, development topics, API reference, and release notes; identify gaps and stale claims rather than assuming one section represents the whole site.
3. Map each affected documentation area to its authoritative implementation and examples. Start with available checkouts and submodules such as `external/core`, then use repository links, project metadata, and the GitHub connector to locate separate plugin, application, or tooling repositories where needed. Typical mappings include core API pages to the ManiVault core source, plugin-development concepts to core plus the relevant example or built-in plugin implementations, application and DevBundle guides to their source repositories, and Python/Jupyter pages to JupyterPlugin. Treat this as discovery guidance, not a fixed exhaustive catalogue.
4. Read the relevant current source, examples, configuration, and release or migration notes. Inspect implementation when prose is incomplete, ambiguous, or inconsistent. Record each repository and revision examined; do not imply that uninspected repositories or site sections were audited.
5. Compare source behavior with all affected ManiVault pages, examples, navigation, and cross-references. Look for missing concepts or workflows, changed APIs and signatures, behavior and lifecycle changes, setup or configuration drift, terminology, outdated examples, broken links, and topics present in code but absent from the docs. Use a concise change map (source change or capability -> affected local pages -> action) to track multi-page impact.
6. Unless the user explicitly asked for audit-only, implement the smallest coherent set of updates. Keep the documentation integrated with the site and at the right level: use implementation references for detailed API contracts, explain broader concepts locally, and avoid duplicating independently maintained upstream manuals.
7. If an authoritative repository or revision cannot be accessed, continue independent review where useful, but mark that portion unverified. Do not claim a full-site or full-source synchronization when the review was partial; state the limitation and the next useful source to inspect.
8. Validate affected toctrees, references, examples, and the practical Sphinx build when available. Fix issues introduced by the edits and distinguish existing warnings from new ones.
9. Do not commit, push, publish, or modify upstream repositories unless explicitly requested.

## Audit-only requests

When the user explicitly asks to audit, review, assess, or find missing documentation without asking for updates, inspect and report findings without editing files. Include the scope covered, repositories and revisions examined, and a concise change map of source or capability, affected local pages, and recommended action.

## Completion report

Summarize the review scope; repositories and revisions examined; local areas and pages reviewed or changed; gaps found; validation performed; and unresolved discrepancies or follow-up opportunities. If coverage was partial, name the unreviewed areas. If no changes are needed, say what was checked and why.
