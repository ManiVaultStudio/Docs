# CodecActionBinding

**Qualified name:** `mv::util::CodecActionBinding`

`CodecActionBinding` safely associates a {doc}`BlobCodec <blob_codec>` with its {doc}`CodecSettingsAction <../../gui/actions/miscellaneous/codec_settings_action>`. It deliberately avoids making the GUI action a child of a codec that may live or be destroyed on a worker thread. When the codec is destroyed, the action is scheduled for deletion in the GUI thread.

This is primarily an ownership utility for codec implementations and factories; ordinary serializers do not need to create bindings themselves.

```{doxygenclass} mv::util::CodecActionBinding
:members:
:protected-members:
```
