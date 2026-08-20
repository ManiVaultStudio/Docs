# Build troubleshooting

## `MV_INSTALL_DIR` is missing

The core requires an explicit install directory. Reconfigure with an absolute path:

```console
cmake -S core -B core-build -DMV_INSTALL_DIR=/absolute/path/to/manivault-install
```

## CMake cannot find Qt

Confirm that Qt 6.8 or newer is installed with Core, Widgets, OpenGL, OpenGL Widgets, WebEngine Widgets, and Concurrent. Then set `CMAKE_PREFIX_PATH` to the compiler-specific Qt kit, or set `Qt6_DIR` to its `lib/cmake/Qt6` directory. Delete and recreate the build directory if CMake cached a different Qt installation.

## A dependency fails during configuration

The first configure downloads third-party source archives and repositories. Check network, proxy, certificate, and GitHub access. Retry after fixing connectivity; CPM normally reuses successful downloads. Do not manually edit generated dependency sources as a permanent fix.

## The compiler rejects C++20 code

Verify which compiler CMake selected in its configure output. Install a current toolchain, or select the intended compiler before creating the build directory. A build directory configured with one compiler should not be reused with another.

## Compilation runs out of memory

Limit parallel jobs:

```console
cmake --build core-build --target MV_Application --config Release --parallel 4
```

Reduce the number further if necessary. `MV_UNITY_BUILD` can improve throughput in some environments but may increase peak memory for individual translation units.

## ManiVault starts without expected functionality

The core alone does not provide every loader, analysis, or visualization. Build and install the required plugin repositories, or use a suitable DevBundle bundle. Ensure plugins were built against the same core configuration and were installed into the same ManiVault tree.

## The IDE launches the wrong executable

Point the run configuration at the installed application under `MV_INSTALL_DIR`, not an intermediate executable in the build tree. Use the corresponding configuration directory (`Release`, `Debug`, and so on) as the working environment.

## Cached configuration behaves unexpectedly

First rerun CMake configuration. If you changed compiler, generator, architecture, or Qt kit, create a new build directory rather than trying to repair the old cache. Preserve the source and install directories; only the generated build directory needs replacement.

