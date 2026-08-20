# Build configuration options

The root CMake project exposes several options. Defaults shown here come from the current core repository.

| Option | Default | Purpose |
|---|---:|---|
| `MV_USE_GTEST` | `OFF` | Build GoogleTest-based tests |
| `MV_USE_AVX` | `OFF` | Enable AVX-specific compilation where supported |
| `MV_USE_ERROR_LOGGING` | `OFF` | Enable error-reporting integration |
| `MV_PRECOMPILE_HEADERS` | `ON` | Use precompiled headers to reduce normal build time |
| `MV_UNITY_BUILD` | `OFF` | Combine sources into unity translation units |
| `MV_WARNINGS_AS_ERRORS` | `ON` | Treat compiler warnings as errors |
| `MV_ENABLE_CPPTRACE` | `ON` | Enable stack-trace support through cpptrace |

Pass options during configuration:

```console
cmake -S core -B core-build \
  -DMV_INSTALL_DIR=/absolute/path/to/manivault-install \
  -DCMAKE_PREFIX_PATH=/absolute/path/to/Qt/6.x/compiler-kit \
  -DMV_USE_GTEST=ON
```

Keep the defaults unless you have a concrete reason to change them. In particular, AVX narrows CPU compatibility, and unity builds can change diagnostics and memory behavior. If warnings from an unsupported compiler prevent local exploration, disabling `MV_WARNINGS_AS_ERRORS` can be useful, but address the warnings before contributing code.

## Qt discovery

Prefer `CMAKE_PREFIX_PATH` when one Qt kit should be discoverable as a package prefix. Use `Qt6_DIR` when you need to point directly at `lib/cmake/Qt6`:

```console
cmake -S core -B core-build \
  -DMV_INSTALL_DIR=/absolute/path/to/manivault-install \
  -DQt6_DIR=/absolute/path/to/Qt/6.x/compiler-kit/lib/cmake/Qt6
```

Do not mix Qt kits built for different compilers or architectures in one build directory.

## Configuring plugins

The installed core exports its CMake package under:

```text
<MV_INSTALL_DIR>/cmake/mv
```

When configuring a plugin separately, point `ManiVault_DIR` at that directory and use the same build configuration, compiler, architecture, and Qt kit as the core. The configuration-specific headers and libraries live in the corresponding `Release`, `Debug`, or other install subtree.

