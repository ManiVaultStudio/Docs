# Icons

Use icons to make plugin kinds and common operations recognizable across menus, toolbars, settings, notifications, and the data hierarchy. ManiVault's named icons are the preferred starting point: they scale cleanly and adapt to the active light or dark theme.

## Choose the right mechanism

| Need | Preferred mechanism |
| --- | --- |
| Set the icon of a plugin factory or action | `setIconByName()` |
| Pass an icon to a Qt widget, dialog, model, or notification | `mv::util::StyledIcon` |
| Select a regular or brand glyph explicitly | `StyledIcon::fromFontAwesomeRegular()` or `fromFontAwesomeBrandsRegular()` |
| Add a modifier, fixed semantic color, or icon badge | Configure a `StyledIcon` |
| Preserve a multicolored logo or illustration | A `QIcon` loaded from a Qt resource |
| Build an icon from a generated pixmap or combine existing icons | Helpers in `util/Icon.h` |

For complete signatures, see the {doc}`icon API reference <../../api/core/util/icon/index>` and {doc}`WidgetAction API reference <../../api/core/gui/actions/widget_action>`.

## Plugin and action icons

Factories and actions derive from `WidgetAction`, so the most direct API is `setIconByName()`:

```cpp
ExampleViewPluginFactory::ExampleViewPluginFactory() :
    ViewPluginFactory(false)
{
    setIconByName("braille");
}

ExampleSettingsAction::ExampleSettingsAction(QObject* parent) :
    VerticalGroupAction(parent, "Example settings"),
    _exportAction(this, "Export")
{
    setIconByName("sliders");

    _exportAction.setIconByName("file-export");
    _exportAction.setToolTip("Export the current result");
}
```

The factory icon becomes the visual identity of that plugin kind and is reused by several parts of the application. Choose a stable icon that describes the plugin's purpose rather than its current state. Use state-specific icons on the actions that perform or represent those state changes.

Named icons use the Font Awesome Free resources bundled with the core. Supply the glyph name without a `fa-` prefix, for example `database`, `file-export`, `triangle-exclamation`, or `braille`. The default font and version follow the core. Avoid pinning them in ordinary plugin code so the core can apply its normal version fallback.

If a name cannot be resolved, the icon will be empty and the core writes a warning to the application log. Check icon-bearing menus and toolbars during development; a missing glyph is easy to overlook when the action also has a label.

## Using `StyledIcon`

Construct a `StyledIcon` when an API expects a `QIcon` or when the icon needs additional styling. It converts implicitly to `QIcon`:

```cpp
#include <util/StyledIcon.h>

using mv::util::StyledIcon;

dialog.setWindowIcon(StyledIcon("chart-line"));
button->setIcon(StyledIcon("play"));
mv::help().addNotification(
    "Import complete",
    "The dataset is ready.",
    StyledIcon("circle-check")
);
```

The default `ThemeAware` mode recolors the glyph using the application palette whenever Qt asks for a pixmap. This lets the same icon remain legible in light and dark themes and in normal, active, and disabled UI states.

### Font variants

The default constructor requests the solid Font Awesome variant and can fall back to compatible bundled variants. Select a variant explicitly when its visual meaning matters:

```cpp
_emptyCircleAction.setIcon(
    StyledIcon::fromFontAwesomeRegular("circle")
);

_repositoryAction.setIcon(
    StyledIcon::fromFontAwesomeBrandsRegular("github")
);
```

Brand icons should be used for the service they identify, not as generic operation icons.

### Fixed colors

Use a fixed color only when color itself carries a stable semantic meaning, such as a warning or failure state:

```cpp
_warningAction.setIcon(
    StyledIcon("triangle-exclamation").withColor(QColor("#c4621e"))
);
```

`withColor()` changes the icon to `FixedColor` mode, so it no longer adapts to the theme. Test the result against both light and dark backgrounds. Do not use color as the only indication of state; retain a distinct glyph, label, tooltip, or status message.

For specialized surfaces, `withColorGroups()` and `withColorRoles()` select the palette group and role used in each theme without switching to a fixed color. Prefer that approach when the desired color already has an application-palette meaning.

### Modifiers and badges

A modifier places a smaller glyph over the lower-right part of the base icon:

```cpp
_addDatasetAction.setIcon(
    StyledIcon("database").withModifier("plus")
);
```

Use modifiers for a compact, familiar combination. If the result needs explanation at normal toolbar size, choose a single clearer icon and put the detail in the action text or tooltip.

For a live count on a `WidgetAction`, prefer the action's badge:

```cpp
auto& badge = _messagesAction.getBadge();
badge.setNumber(numberOfUnreadMessages);
badge.setEnabled(numberOfUnreadMessages > 0);
```

`StyledIcon::withBadge()` is available when the badge must be part of the `QIcon` itself. See the {doc}`Badge API reference <../../api/core/util/badge/badge>` for its number, colors, alignment, scale, and custom-pixmap options.

## Custom image icons

Use a custom image when a named monochrome glyph cannot express the identity, or when preserving a product or organization logo is important. Package the asset in the plugin's Qt resource file rather than depending on a path outside the plugin:

```xml
<RCC>
  <qresource prefix="/ExamplePlugin">
    <file>icons/example-logo.svg</file>
  </qresource>
</RCC>
```

Load a multicolored asset directly as a `QIcon` so its colors are preserved:

```cpp
_aboutAction.setIcon(
    QIcon(":/ExamplePlugin/icons/example-logo.svg")
);
```

For a monochrome custom asset that should follow the application palette, wrap it instead:

```cpp
const QIcon sourceIcon(":/ExamplePlugin/icons/custom-tool.svg");

_customToolAction.setIcon(
    StyledIcon::fromQIcon(sourceIcon)
);
```

The theme-aware wrapper recolors the source silhouette. It is therefore unsuitable for multicolored artwork, gradients, or an image whose internal colors carry meaning.

Prefer SVG for simple scalable artwork. If the source is a runtime-generated `QPixmap`, `mv::gui::createIcon()` creates the standard icon sizes. The same utility header provides `combineIcons()`, `createOverlayIcon()`, and `combineIconsHorizontally()` for cases that cannot be expressed by a `StyledIcon` modifier.

## Design and accessibility guidance

- Reuse an existing icon for an existing concept. Consistency matters more than novelty.
- Use operation glyphs for actions and noun-like glyphs for plugin identities or objects.
- Pair unfamiliar or destructive icons with a visible label or clear tooltip.
- Do not distinguish states only by color; change the glyph or text as well.
- Check icons at their actual small UI size, not only in an enlarged preview.
- Verify normal, hovered, disabled, light-theme, and dark-theme rendering.
- Avoid changing an established plugin icon without a reason, because users learn it as part of the plugin's identity.

## Common problems

An empty icon usually means the glyph name is absent from the bundled metadata or was written with the `fa-` prefix. A custom icon that becomes a single-color silhouette was probably wrapped in a theme-aware `StyledIcon`; assign the original `QIcon` directly when its colors must survive. Conversely, a black custom icon that disappears in dark mode should be supplied as a monochrome asset and wrapped with `StyledIcon::fromQIcon()`.

If a fixed-color icon is readable in one theme but not the other, return to theme-aware mode or choose palette roles instead of a literal color. If a composite icon becomes visually dense, simplify it: small controls leave little room for multiple equally important symbols.
