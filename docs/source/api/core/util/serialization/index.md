# Serialization

ManiVault persistence has three related layers:

1. **Object state** — a {doc}`Serializable <serializable>` object converts its state to and from a `QVariantMap`.
2. **Binary payloads** — the {doc}`serialization helpers <serialization>` partition large byte buffers into blocks and represent those blocks in the object's variant map.
3. **Encoding** — the active project's {doc}`compression settings <../../gui/actions/project/project_compression_action>` select a codec through the {doc}`CodecRegistry <codec_registry>`. A {doc}`BlobCodec <blob_codec>` then encodes or decodes each block.

This separation lets a plugin describe *what* must be persisted without taking responsibility for project-archive layout or the concrete compression implementation. On restoration, each blob records the codec needed to decode it; the registry supplies the matching implementation.

Start with {doc}`Project serialization and restoration <../../../../development/building_plugins/persistence/index>` for the plugin contract, workflow boundary, identity rules, and compatibility guidance. The pages below provide the exact low-level APIs.

## Which API should I use?

| If you are… | Start with… |
| --- | --- |
| Persisting plugin or model state | {doc}`Serializable <serializable>` and the plugin persistence guide |
| Storing a large binary buffer | {doc}`Blob serialization functions <serialization>` |
| Configuring project compression | {doc}`ProjectCompressionAction <../../gui/actions/project/project_compression_action>` and {doc}`CodecSettingsAction <../../gui/actions/miscellaneous/codec_settings_action>` |
| Integrating another codec into the application | {doc}`BlobCodec <blob_codec>`, {doc}`BlobCodecFactory <blob_codec_factory>`, and {doc}`CodecRegistry <codec_registry>` |

Prefer the workflow forms of serialization and blob processing for long-running operations. They integrate with ManiVault's workflow execution, progress reporting, and cancellation. The synchronous APIs remain useful for small, bounded state.

## Blob encoding pipeline

The blob helpers obtain the current project's codec settings, divide the input into blocks, and create codecs through the registry. `BlobStorageLocation` explicitly chooses whether `bytesToBlobVariantMap()` and `bytesToBlobVariantMapWorkflow()` store the encoded blocks as project-archive files or as base64 payloads inside the project JSON. File storage is the default. Decoding recognizes both representations and follows the codec metadata stored with the blob rather than assuming the project's current selection.

For an end-to-end plugin example and guidance on choosing a storage location, see {doc}`Persisting binary data as blob variant maps <../../../../development/building_plugins/persistence/binary_blob_data>`.

`CodecActionBinding` is the ownership bridge between a codec and its GUI settings action. It avoids unsafe cross-thread `QObject` parenting when codec work runs outside the GUI thread.

`PropertiesSerializer` is a specialized internal workflow helper for property maps. It is not the general entry point for plugin persistence.

## Reference

```{toctree}
:maxdepth: 1

serializable
serialization
blob_codec
blob_codec_factory
codec_registry
codec_action_binding
properties_serializer
```
