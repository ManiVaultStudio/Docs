# Serialization

This section documents utility functions used for serializing and deserializing raw data and Qt variant types, including support for disk-backed storage of large data payloads.

## Functions

```{doxygenfunction} mv::util::saveRawDataToBinaryFile
```

```{doxygenfunction} mv::util::loadRawDataFromBinaryFile
```

```{doxygenfunction} mv::util::rawDataToVariantMap
```

```{doxygenfunction} mv::util::populateDataBufferFromVariantMap
```

```{doxygenfunction} mv::util::variantMapMustContain
```

```{doxygenfunction} mv::util::storeQVariant
```

```{doxygenfunction} mv::util::loadQVariant
```

```{doxygenfunction} mv::util::storeOnDisk(const QStringList& list)
```

```{doxygenfunction} mv::util::storeOnDisk(const QVector<uint32_t>& vec)
```

```{doxygenfunction} mv::util::loadFromDisk(const QVariantMap& variantMap, QStringList& list)
```

```{doxygenfunction} mv::util::loadFromDisk(const QVariantMap& variantMap, QVector<uint32_t>& vec)
```
