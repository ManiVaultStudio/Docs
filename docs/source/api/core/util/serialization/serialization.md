# Serialization

This section documents utility functions for encoding byte buffers as project blobs, restoring those buffers, and serializing Qt variant maps. Large encode and decode operations can be expressed as workflow plans so that they use the core workflow execution, progress, and cancellation infrastructure.

Blob encoding uses the active project's {doc}`compression configuration <../../gui/actions/project/project_compression_action>` and creates the selected {doc}`BlobCodec <blob_codec>` through the {doc}`CodecRegistry <codec_registry>`. Use these helpers instead of coupling plugin serialization directly to a concrete compression library or archive layout.

The encode helpers require an open project because the project supplies the codec settings and persistence context. A serialized blob carries the codec information required for restoration.

## Storage location

`BlobStorageLocation` controls where each encoded block is stored:

- `FileInProject` writes block files into the project archive and stores relative references in the blob map. It is the default and is normally the better choice for large payloads.
- `InlineInProjectJson` stores the encoded bytes as base64 data directly in the project JSON. It produces a self-contained variant-map representation, at the cost of a larger JSON document and base64 overhead.

Both forms use the active project's codec and block-size settings. The restore helpers accept either representation without a separate storage-location argument. Treat the returned blob map as opaque rather than depending on its internal block fields.

For plugin-oriented examples, see {doc}`Persisting binary data as blob variant maps <../../../../development/building_plugins/persistence/binary_blob_data>`.

## Functions

```{doxygenfunction} mv::util::bytesToBlobVariantMap
```

```{doxygenfunction} mv::util::bytesToBlobVariantMapWorkflow
```

```{doxygenfunction} mv::util::populateBytesFromBlobMap
```

```{doxygenfunction} mv::util::populateBytesFromBlobMapWorkflow
```

```{doxygenfunction} mv::util::bytesFromBlobVariantMap
```

```{doxygenfunction} mv::util::variantMapMustContain
```

```{doxygenfunction} mv::util::estimateRawBlockTotalSize
```

```{doxygenfunction} mv::util::serializeVariantMap
```

```{doxygenfunction} mv::util::deserializeVariantMap
```

```{doxygenfunction} mv::util::storeOnDisk(const QStringList& list)
```

```{doxygenfunction} mv::util::storeOnDisk(const QVector<uint32_t>& vec)
```

```{doxygenfunction} mv::util::loadFromDisk(const QVariantMap& variantMap, QStringList& list)
```

```{doxygenfunction} mv::util::loadFromDisk(const QVariantMap& variantMap, QVector<uint32_t>& vec)
```
