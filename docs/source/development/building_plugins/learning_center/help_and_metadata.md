# Help, about information, and repository links

The factory is the source of help shared by every instance of a plugin kind. Configure its `PluginMetadata` in the factory constructor and provide repository or README URLs through the factory overrides.

```cpp
ExampleViewPluginFactory::ExampleViewPluginFactory() :
    ViewPluginFactory(false)
{
    auto& metadata = getPluginMetadata();

    metadata.setDescription("Explore point datasets interactively");
    metadata.setSummary(
        "Shows point datasets and provides selection and navigation tools.");
    metadata.setAuthors({
        { "A. Developer", { "Developer" }, { "EX" } }
    });
    metadata.setOrganizations({
        { "EX", "Example Institute", "https://example.org" }
    });
    metadata.setLicenseText("Distributed under the LGPL v3.0.");
}

QUrl ExampleViewPluginFactory::getRepositoryUrl() const
{
    return QUrl("https://github.com/example/example-view");
}

QString ExampleViewPluginFactory::getDefaultBranch() const
{
    return "main";
}
```

The about dialog uses the metadata container. A valid repository URL enables the repository item in a view's Learning Center overlay. The base `getReadmeMarkdownUrl()` derives a raw GitHub README URL from `getRepositoryUrl()` and `getDefaultBranch()`; override it when documentation lives elsewhere or the repository layout differs.

The base default branch is `master`. Override it for repositories whose README is on `main` or another branch.

For all supported metadata fields, see {doc}`Metadata and build integration <../fundamentals/metadata_and_build>`.

## Making plugin documentation available

`PluginFactory::hasHelp()` returns `false` by default. Override it and connect the factory metadata's help trigger when the plugin supplies documentation. The same trigger is used by the Help menu and the view overlay.

```cpp
class ExampleViewPluginFactory final : public mv::plugin::ViewPluginFactory
{
    // ...

    bool hasHelp() const override { return true; }
    QUrl getReadmeMarkdownUrl() const override;

private:
    QPointer<mv::util::MarkdownDialog> _helpDialog;
};
```

```cpp
#include <widgets/MarkdownDialog.h>

ExampleViewPluginFactory::ExampleViewPluginFactory() :
    ViewPluginFactory(false)
{
    auto& helpAction = getPluginMetadata().getTriggerHelpAction();

    connect(&helpAction, &mv::gui::TriggerAction::triggered,
            this, [this]() {
        if (!getReadmeMarkdownUrl().isValid() || _helpDialog)
            return;

        _helpDialog = new mv::util::MarkdownDialog(getReadmeMarkdownUrl());
        _helpDialog->setWindowTitle(getKind());
        _helpDialog->setAttribute(Qt::WA_DeleteOnClose);
        _helpDialog->setWindowModality(Qt::NonModal);
        _helpDialog->show();
    });
}
```

Use `QPointer` because the dialog deletes itself when closed. Guard against opening multiple copies and validate the URL before constructing the dialog. For bundled or generated documentation, connect the same trigger to the appropriate viewer instead of forcing it through a remote README.

## What appears where

- About information is available in the view overlay for every view plugin.
- Repository access appears when `getRepositoryUrl()` is valid.
- Documentation appears when `hasHelp()` is true and the help trigger is connected.
- Non-view plugins with `hasHelp()` also appear under **Help → Plugins**.
- Videos, tutorials, and shortcuts appear only when the plugin has associated entries.

Keep the short description useful in compact surfaces. Put fuller context in the summary and operational instructions in the README or tutorials.
