# Persistent plugin settings

The preferred way of saving/restoring persistent plugin settings is to call `hdps::Plugin::setSetting(const QString& path, const QVariant& value)` and `hdps::Plugin::getSetting(const QString& path, const QVariant& defaultValue = QVariant())` from the plugin base class (see examples below). The `path` variable represents the location of the setting (setting groups are established using forward slashes).

### Saving a setting**  
`plugin->setSetting("General/Computation/NumberOfIterations", 32)`

### Loading a setting
`const auto numberOfIterations= plugin->getSetting("General/Computation/NumberOfIterations").toInt()`