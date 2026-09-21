# Plugin

All ManiVault plugin instances descend from this base class. For the factory–instance model, initialization order, destruction, and state ownership, see {doc}`Plugin lifecycle <../../../development/building_plugins/fundamentals/lifecycle>`.

The plugin facade also provides access to its factory's UI-backed global settings and to UI-less application preferences. See {doc}`Global plugin settings <../../../development/building_plugins/global_settings/index>` before choosing these over project-owned instance state.

`Plugin::getThirdPartyLicenses()` provides the dependency license records associated with the plugin's factory. Use this when code working with a plugin instance needs to inspect the plugin's declared third-party dependencies.

**Qualified name:** `mv::plugin::Plugin`

```{doxygenclass} mv::plugin::Plugin
:members:
:protected-members:
