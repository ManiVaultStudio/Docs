# CodecSettingsAction

**Qualified name:** `mv::gui::CodecSettingsAction`

This action contains the user-facing settings for one blob codec: its codec key and block size. A {doc}`BlobCodecFactory <../../../util/serialization/blob_codec_factory>` creates the appropriate settings action, and {doc}`ProjectCompressionAction <../project/project_compression_action>` exposes it as part of the project's compression configuration.

See {doc}`Serialization <../../../util/serialization/index>` for the complete persistence pipeline and the distinction between plugin serialization and application-level codec integration.

```{doxygenclass} mv::gui::CodecSettingsAction
:members:
:protected-members:
```
