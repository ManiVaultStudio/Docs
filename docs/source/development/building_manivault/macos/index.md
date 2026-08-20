# Building on macOS

The reference macOS build uses macOS 15, Xcode 16.2 / Apple Clang 16, and ARM64. Apple Silicon is therefore part of the tested CI matrix.

Install:

- Xcode and its command-line tools;
- CMake and Git;
- a Qt 6.8-or-newer macOS kit with the modules listed in {doc}`../prerequisites`.

The core does not require a separate OpenMP installation. Plugins that use OpenMP or another compute framework can add their own dependency requirements.

Generate an Xcode project and build it:

```console
cmake -S core -B core-build -G Xcode \
  -DMV_INSTALL_DIR=/absolute/path/to/manivault-install \
  -DCMAKE_PREFIX_PATH=/Users/me/Qt/6.x/macos

cmake --build core-build --target MV_Application --config Release --parallel
```

```{toctree}
:maxdepth: 1

xcode
```
