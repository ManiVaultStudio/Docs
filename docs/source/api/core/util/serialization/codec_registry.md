# CodecRegistry

**Qualified name:** `mv::util::CodecRegistry`

`CodecRegistry` maps stable codec types and keys to {doc}`BlobCodecFactory <blob_codec_factory>` instances. Project restoration uses this mapping to recreate the codec named in stored blob metadata, while project compression settings use it to enumerate and create available codecs.

Registration belongs to the application/Core integration layer. Plugin persistence code should use the {doc}`blob serialization helpers <serialization>` and should not depend on a particular registered codec.

```{doxygenclass} mv::util::CodecRegistry
:members:
:protected-members:
```

```{doxygenfunction} mv::util::codecRegistry
```
