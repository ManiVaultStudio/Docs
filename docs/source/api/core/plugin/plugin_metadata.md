# PluginMetadata

This container holds the user-facing metadata supplied by a plugin factory, including its description, summary, authors and affiliations, copyright, license, shortcut map, and third-party dependency licenses. For its relationship to `PluginInfo.json`, Qt metadata, and CMake packaging, see {doc}`Metadata and build integration <../../../development/building_plugins/fundamentals/metadata_and_build>`. For about, README, repository, and help integration, see {doc}`Help and metadata <../../../development/building_plugins/learning_center/help_and_metadata>`.

## Third-party dependency licenses

`mv::plugin::ThirdPartyLicense` contains a dependency `name`, a `license` identifier or name, and an optional `url`. `mv::plugin::ThirdPartyLicenses` is the corresponding `std::vector` alias. Entries compare by all three fields.

`PluginMetadata` exposes the following operations:

```cpp
ThirdPartyLicenses getThirdPartyLicenses() const;
void setThirdPartyLicenses(const ThirdPartyLicenses& licenses);
void addThirdPartyLicense(const ThirdPartyLicense& license);
bool removeThirdPartyLicense(const ThirdPartyLicense& license);
bool hasThirdPartyLicenses() const;
```

Use `addThirdPartyLicense()` when incrementally registering a dependency; duplicate entries are ignored. Changes emit `thirdPartyLicensesChanged(previous, current)`. Entries declared in the `thirdPartyLicenses` array of `PluginInfo.json` are copied into this metadata during plugin factory loading.

**Qualified name:** `mv::plugin::PluginMetadata`

```{doxygenclass} mv::plugin::PluginMetadata
:members:
:protected-members:
