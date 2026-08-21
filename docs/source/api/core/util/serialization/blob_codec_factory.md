# BlobCodecFactory

**Qualified name:** `mv::util::BlobCodecFactory`

A factory describes one codec type, creates its default GUI settings, and creates configured codec instances. Factories are registered with the {doc}`CodecRegistry <codec_registry>` by the application integration layer.

Factory objects are expected to live on the main thread because they create {doc}`CodecSettingsAction <../../gui/actions/miscellaneous/codec_settings_action>` instances. The codecs they produce may subsequently perform encoding or decoding in workflow worker threads.

```{doxygenclass} mv::util::BlobCodecFactory
:members:
:protected-members:
```
