# Meta-object and build integration

Qt's meta-object compiler generates code for signals, slots, properties, runtime type information, and plugin metadata. The plugin target must expose every relevant declaration to AUTOMOC.

## Q_OBJECT

Add `Q_OBJECT` to a QObject-derived class when it declares signals, slots, or properties, uses class-specific meta-object features, or serves as the exported Qt plugin factory:

```cpp
class ExampleViewPluginFactory final
    : public mv::plugin::ViewPluginFactory
{
    Q_OBJECT
    Q_INTERFACES(mv::plugin::ViewPluginFactory
                 mv::plugin::PluginFactory)
    Q_PLUGIN_METADATA(IID  "studio.manivault.ExampleViewPlugin"
                      FILE "PluginInfo.json")

    // ...
};
```

A subclass that merely inherits QObject behavior does not need `Q_OBJECT`, but adding signals later changes that decision. QObject-derived types are identity objects: do not make them copyable or store them in containers by value.

## AUTOMOC and target sources

Enable AUTOMOC on the plugin target and ensure headers containing `Q_OBJECT`, `Q_GADGET`, or `Q_PLUGIN_METADATA` are visible to that target:

```cmake
set_target_properties(${PLUGIN_TARGET} PROPERTIES
    AUTOMOC ON
)

target_sources(${PLUGIN_TARGET} PRIVATE
    ExampleViewPlugin.h
    ExampleViewPlugin.cpp
    PluginInfo.json
)
```

Link the Qt modules actually used and the ManiVault core target. The current core requires Qt 6.8; build plugins against the Qt and compiler toolchain supplied by the matching ManiVault development bundle to avoid binary incompatibilities.

Use `mv_handle_plugin_config(${PLUGIN_TARGET})` for the standard plugin metadata and output-name processing. See {doc}`Metadata and build integration <../fundamentals/metadata_and_build>` for `PluginInfo.json`, the IID, and runtime metadata.

Do not manually include generated MOC files in ordinary header-defined classes when AUTOMOC already handles them. Source-local QObject declarations can require a source MOC include; follow CMake's diagnostic rather than adding duplicate generation pre-emptively.

## Custom types in signals and QVariant

Types transported through queued signals or stored in Qt's generic type facilities may need meta-type declaration and registration:

```cpp
struct ResultSummary
{
    QString label;
    qsizetype count = 0;
};

Q_DECLARE_METATYPE(ResultSummary)

// During initialization, before the first queued use:
qRegisterMetaType<ResultSummary>("ResultSummary");
```

Place `Q_DECLARE_METATYPE` where the complete type is visible and register the same spelling used by name-based APIs. Prefer values with clear copy or move semantics. For lifetime-sensitive domain objects, sending a stable ID or ManiVault handle is usually safer than registering and queuing a borrowed raw pointer.

An error such as “Cannot queue arguments of type …” means the queued boundary was reached without suitable meta-type support; it is not safe to silence by forcing a direct connection across threads.
