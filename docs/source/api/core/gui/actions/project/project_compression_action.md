# ProjectCompressionAction

**Qualified name:** `mv::ProjectCompressionAction`

This action owns the compression choice for the active project and exposes its {doc}`codec settings <../miscellaneous/codec_settings_action>`. The blob serialization helpers use it to create a configured codec; ordinary plugin serializers should normally call those helpers rather than instantiate codecs themselves.

See {doc}`Serialization <../../../util/serialization/index>` for the complete object-state, blob-storage, and codec pipeline.

```{doxygenclass} mv::ProjectCompressionAction
:members:
:protected-members:
```
