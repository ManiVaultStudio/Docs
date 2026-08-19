# View-plugin Learning Center overlay

Every `ViewPlugin` receives a `PluginLearningCenterAction` and an overlay widget from the base class. The overlay exposes whichever facilities are available for that plugin:

- Related videos and tutorials, with count badges
- Plugin documentation when `hasHelp()` is true
- About information from `PluginMetadata`
- The categorized shortcut map when it is non-empty
- A repository link when the factory returns a valid URL
- Navigation to the global Learning Center

Do not construct `PluginLearningCenterAction` or `ViewPluginLearningCenterOverlayWidget` yourself. Configure the objects available through `getLearningCenterAction()`.

## Targeting the main content widget

By default, the overlay belongs to the view plugin's widget. If the view contains toolbars or side panels, target the central canvas so the Learning Center control does not cover unrelated UI:

```cpp
#include <widgets/ViewPluginLearningCenterOverlayWidget.h>

void ExampleViewPlugin::init()
{
    // Construct the layout and add _canvas first.

    if (auto* overlay =
            getLearningCenterAction().getViewPluginOverlayWidget()) {
        overlay->setTargetWidget(&_canvas);
    }
}
```

The target widget must remain alive while the overlay refers to it. If a view replaces its rendering widget dynamically, retarget the overlay as part of the same change.

## Visibility and alignment

The Learning Center action exposes the standard overlay controls:

```cpp
auto& learningCenter = getLearningCenterAction();

learningCenter.getToolbarVisibleAction().setChecked(true);
learningCenter.setAlignment(Qt::AlignBottom | Qt::AlignLeft);
```

Supported alignments are the four corners. Users can change visibility and alignment from the Learning Center context menu. The base plugin serialization stores these action values, so derived plugins should not duplicate them in their own project state.

Hide the overlay by default only for a deliberate product reason, such as a dedicated tutorial view where the control would be redundant. Users otherwise benefit from a consistent location for help across views.

## Non-view plugins

Analysis, transformation, loader, writer, and data plugins have a `PluginLearningCenterAction` through the common `Plugin` base, but they do not receive the in-view overlay. Their factory documentation can appear under **Help → Plugins** when `hasHelp()` returns true, and their tutorials and videos remain available through the global Learning Center.

For the underlying members, see the {doc}`PluginLearningCenterAction API <../../../api/core/gui/actions/internal/plugin_learning_center_action>` and {doc}`ViewPluginLearningCenterOverlayWidget API <../../../api/core/gui/widgets/internal/view_plugin_learning_center_overlay_widget>`.
