# BlobCodec

**Qualified name:** `mv::util::BlobCodec`

`BlobCodec` is the abstract binary encoder and decoder used by project blob storage. A codec can encode to memory or a file, decode into a new or existing buffer, declare its file extension, and indicate whether its encoded data may be stored inline.

Codecs are created from settings by the {doc}`CodecRegistry <codec_registry>` rather than constructed directly by plugin serialization code. The associated {doc}`CodecSettingsAction <../../gui/actions/miscellaneous/codec_settings_action>` remains a GUI object; {doc}`CodecActionBinding <codec_action_binding>` manages the lifetime boundary when codec work runs on another thread.

```{doxygenclass} mv::util::BlobCodec
:members:
:protected-members:
```
