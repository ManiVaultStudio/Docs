# Project lifecycle

Opening a project replaces the active project and can restore its workspace and plugin instances. Importing a project brings in data only. Saving writes the current project; publishing is a separate application-distribution operation.

Use the project manager for user-facing operations:

```cpp
mv::projects().saveProject(filePath);
```

The manager exposes state queries such as `isOpeningProject()`, `isImportingProject()`, `isSavingProject()`, and `isPublishingProject()`. These are useful when behavior genuinely differs during orchestration; they should not replace correct serialization methods.

Lifecycle signals have before and after phases, including `projectAboutToBeOpened` / `projectOpened`, `projectAboutToBeImported` / `projectImported`, and `projectAboutToBeSaved` / `projectSaved`.

Use an “about to” signal to stop transient work or flush state that is not already represented by the serialization contract. Use the completion signal to refresh project-wide caches after all restored objects are available. Avoid performing another project operation recursively from these signals.

Plugins normally should not parse project archives or call their own restoration methods. The project and plugin managers create instances, supply dataset context, and invoke the appropriate persistence contract.

## Degraded view-state restoration

Workspace restoration isolates the state restoration of individual view plugins. If one view plugin throws, Core records a structured workflow warning containing its GUI name, kind, ID, exception information, and available stack evidence, then continues with the other views. This is a degraded restoration, not necessarily a failed project-open result.

Plugin restoration code should still throw when it cannot establish valid state; it should not swallow the problem merely to keep loading. Prefer validating serialized values before modifying live state, and leave the plugin at a safe default if restoration cannot be completed. Use `mv::ManiVaultException` when structured severity, user-facing context, and diagnostic details should be preserved by the workspace boundary. See {doc}`Compatibility and round-trip testing <compatibility_and_testing>` and {doc}`Exceptions and diagnostic context <../diagnostics/exceptions>`.
