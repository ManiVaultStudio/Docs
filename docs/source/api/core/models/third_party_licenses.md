# Third-party license models

These models expose the aggregated third-party dependency licenses used by ManiVault Core and plugins. They are primarily intended for Core and application UI code; plugin authors normally declare their entries in `PluginInfo.json` and use the plugin metadata API.

The aggregation API was introduced in [core PR #1340](https://github.com/ManiVaultStudio/core/pull/1340).

## Usage record

`mv::ThirdPartyLicenseUsage` combines one `mv::plugin::ThirdPartyLicense` with its usage context:

```cpp
struct ThirdPartyLicenseUsage {
    plugin::ThirdPartyLicense license;
    bool isCore;
    QStringList availablePlugins;
    QStringList loadedPlugins;
};
using ThirdPartyLicenseUsages = std::vector<ThirdPartyLicenseUsage>;
```

`isCore` identifies dependencies supplied by Core. `availablePlugins` lists plugin factories that declare the dependency, while `loadedPlugins` lists instantiated plugin instances currently using it.

## `AbstractThirdPartyLicensesModel`

The base model stores one row per aggregated dependency and exposes four columns through `Column::Name`, `Column::License`, `Column::Core`, and `Column::Plugins`. Its public operations are:

```cpp
void setLicenseUsages(const ThirdPartyLicenseUsages& usages);
ThirdPartyLicenseUsages getLicenseUsages() const;
ThirdPartyLicenseUsage getLicenseUsage(const QModelIndex& index) const;
```

Rows retain the complete usage record. The nested `Item`, `NameItem`, `LicenseItem`, `CoreItem`, and `PluginsItem` classes provide item storage and column header behavior.

## `ThirdPartyLicensesListModel`

`ThirdPartyLicensesListModel` derives from the abstract model and adds:

```cpp
void populateFromPluginManager();
```

Calling this repopulates the model from Core's license resource and the plugin manager's available and loaded plugin metadata. Matching dependency records are consolidated while their usage context is retained.

## `ThirdPartyLicensesFilterModel`

`ThirdPartyLicensesFilterModel` is a sorting and filtering proxy model. Its `PluginState` controls whether the source includes all available plugin declarations or only dependencies used by loaded plugin instances:

```cpp
enum class PluginState { AllAvailable, LoadedOnly };

PluginState getPluginState() const;
void setPluginState(PluginState state);
bool getShowCoreLicenses() const;
void setShowCoreLicenses(bool show);
bool getShowPluginLicenses() const;
void setShowPluginLicenses(bool show);
```

The inherited filter regular expression can be used to search dependency names and license identifiers. Sorting compares the displayed source rows.

`mv::AbstractHelpManager::getThirdPartyLicensesModel()` returns the application's aggregate list model. See {doc}`AbstractHelpManager <../managers/abstract_help_manager>` and the {doc}`user guide <../../../user_guide/third_party_licenses>` for the application-facing entry point.
