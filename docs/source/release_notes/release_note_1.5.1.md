# Release 1.5.1

**Published:** 2026-09-02  
**Upstream release:** https://github.com/ManiVaultStudio/core/releases/tag/v1.5.1

Installers for the most recent version of ManiVault can always be found on [manivault.studio/downloads](https://www.manivault.studio/downloads/).
All available installers are listed [here](https://github.com/ManiVaultStudio/Releases/releases).

## Major changes

- Add high-level parallel workflow utilities and cooperative cancellation.
- Add configurable point Z ordering and non-selectable point rendering.
- Add configurable inline or project-file storage for serialized binary blobs.
- Improve view-plugin state restoration diagnostics and allow the remaining workspace to load after an isolated view restoration error.
- Restore project publishing with workflow-based serialization and allow authors to open published projects for editing explicitly.
- Add a heads-up display toggle to view-plugin settings.
- Improve Sentry crash reporting, user feedback, and developer testing.

This maintenance release also includes fixes for point-data locking and serialization, selection restoration, subset dimension extraction, platform-specific deployment and compilation, plugin action state, and view-loading presentation.

**Full Changelog:** https://github.com/ManiVaultStudio/core/compare/v1.5.0...v1.5.1
