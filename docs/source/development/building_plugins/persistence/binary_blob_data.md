# Persisting binary data as blob variant maps

Use a blob variant map when plugin-owned state contains a binary buffer, numerical array, image payload, or another sizeable byte sequence that must survive project save and restore. The blob utilities preserve the ordinary `QVariantMap` serialization contract while letting Core apply the project's block-size and compression settings.

The result of `bytesToBlobVariantMap()` is itself a `QVariantMap`. Store it under a stable key in the plugin's parent map. On restoration, pass that nested map back to a blob restore helper. Do not copy its internal block schema into plugin code or manipulate fields such as block paths and encoded data directly.

## Save a buffer from `toVariantMap()`

The default storage location writes encoded blocks as files in the project archive:

```cpp
QVariantMap ExampleViewPlugin::toVariantMap() const
{
    auto map = ViewPlugin::toVariantMap();

    if (!_weights.empty()) {
        map["Weights"] = mv::util::bytesToBlobVariantMap(
            reinterpret_cast<const char*>(_weights.data()),
            static_cast<std::uint64_t>(_weights.size() * sizeof(float)));
    }

    return map;
}
```

Always call the direct base implementation first. The helper requires an open project because it obtains the codec, block size, and save location from the current project. It encodes the supplied bytes immediately, so the synchronous call is suitable only when the work is acceptably bounded.

The example omits the key for an empty vector. That makes empty state explicit and avoids asking the allocating restore helper to decode a zero-byte blob.

## Restore the buffer from `fromVariantMap()`

`bytesFromBlobVariantMap()` allocates a `QByteArray` of the recorded decoded size and restores all blocks into it:

```cpp
void ExampleViewPlugin::fromVariantMap(const QVariantMap& map)
{
    ViewPlugin::fromVariantMap(map);

    _weights.clear();

    if (!map.contains("Weights"))
        return;

    const auto bytes = mv::util::bytesFromBlobVariantMap(
        map.value("Weights").toMap());

    if (bytes.size() % static_cast<qsizetype>(sizeof(float)) != 0)
        throw std::runtime_error("Stored weight data has an invalid size");

    _weights.resize(
        static_cast<std::size_t>(bytes.size()) / sizeof(float));

    std::memcpy(_weights.data(), bytes.constData(),
                static_cast<std::size_t>(bytes.size()));
}
```

Validate the decoded byte count before interpreting it as typed data. Also persist any semantic metadata needed to interpret the bytes—such as dimensions, element type, row count, or a format version—as ordinary fields beside the blob. The blob records byte layout and codec information, not the meaning assigned by the plugin.

When the destination storage already exists, `populateBytesFromBlobMap()` avoids the intermediate `QByteArray`:

```cpp
mv::util::populateBytesFromBlobMap(
    map.value("Weights").toMap(),
    reinterpret_cast<char*>(_weights.data()),
    static_cast<std::uint64_t>(_weights.size() * sizeof(float)));
```

Size and initialize the destination from validated plugin metadata before calling this overload.

## Choose where encoded blocks are stored

`BlobStorageLocation` offers two representations:

| Location | Representation | Prefer it when |
| --- | --- | --- |
| `FileInProject` | Encoded block files in the project archive; the blob map contains relative references | The payload is large or the project JSON should remain compact |
| `InlineInProjectJson` | Encoded blocks stored as base64 data directly in the blob map | The nested map should be self-contained and the payload is small enough for JSON storage |

File storage is the default. Select inline storage explicitly:

```cpp
map["Preview"] = mv::util::bytesToBlobVariantMap(
    previewBytes.constData(),
    static_cast<std::uint64_t>(previewBytes.size()),
    mv::util::BlobStorageLocation::InlineInProjectJson);
```

Inline data is still encoded with the active project codec before it is converted to base64. It therefore remains subject to project compression settings, while base64 and JSON representation add size and memory overhead. Restoration is identical for both locations: `bytesFromBlobVariantMap()` and `populateBytesFromBlobMap()` detect the representation from the blob map.

Do not use inline storage merely to obtain a single project file: ManiVault's project archive already packages file-backed blocks with the project. Choose inline storage when the JSON-level representation itself needs to contain the payload.

## Use workflow serialization for substantial data

`bytesToBlobVariantMapWorkflow()` creates a workflow plan that encodes blocks in parallel and publishes the completed blob map as workflow output. `populateBytesFromBlobMapWorkflow()` provides the corresponding parallel decode plan. Use these forms when the payload is large enough that synchronous plugin serialization would be undesirable.

Workflow helpers construct plans; they do not execute them. Compose the returned plan into the plugin's `toVariantMapWorkflow()` or `fromVariantMapWorkflow()` implementation, then let project orchestration execute it. Keep the source or destination buffer alive and unchanged until the composed workflow finishes because the plan operates on the supplied raw pointer.

See {doc}`Synchronous and workflow serialization <synchronous_and_workflow>` for the plugin contract, {doc}`Nested workflows <../../workflows/nested_workflows>` for composition, and the {doc}`blob serialization API <../../../api/core/util/serialization/serialization>` for exact signatures.

## Compatibility and testing

- Keep the parent-map key stable, or migrate older keys deliberately.
- Store a schema or element-format version when the interpretation may evolve.
- Validate byte counts and dimensions before allocating or copying.
- Test both storage locations if plugin code exposes or changes the choice.
- Round-trip projects with the compression codecs the application supports.
- Test missing, empty, truncated, and malformed blob maps at the owning plugin boundary.

Blob helpers report malformed layouts and decoding failures through Core exceptions. Add plugin-specific context when useful, but do not silently accept a partially restored buffer.
