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
