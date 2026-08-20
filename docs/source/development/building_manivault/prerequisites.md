# Prerequisites

The exact tool versions used by ManiVault evolve. Treat the root `CMakeLists.txt`, the DevBundle `config.json`, and the continuous-integration matrix as the source of truth. At the time of writing, the core requires the following baseline.

| Requirement | Current baseline |
|---|---|
| CMake | 3.22 or newer |
| C++ compiler | C++20 support |
| C compiler | C17 support |
| Qt | 6.8 or newer |
| Git | Required to clone sources and fetch CMake dependencies |
| Network access | Required during initial configuration unless dependencies are cached |

The default CI jobs exercise:

- Windows Server 2022 with Visual Studio 2022;
- Ubuntu 24.04 with GCC 13 on x86-64;
- macOS 15 with Xcode 16.2 / Apple Clang 16 on ARM64.

These are tested configurations, not the only possible ones. A compiler with compatible C++20 and Qt support may work, but older combinations require additional validation.

## Install Qt

For desktop development, Qt recommends its online installer. Install a desktop kit for your compiler and include these modules:

- Qt Core and Widgets;
- Qt OpenGL and OpenGL Widgets;
- Qt WebEngine Widgets;
- Qt Concurrent.

The kit architecture must match the compiler and the architecture you intend to build. Plugins can require further Qt modules.

If CMake cannot locate Qt, point `CMAKE_PREFIX_PATH` at the Qt kit directory. For example:

```text
C:/Qt/6.10.3/msvc2022_64
/opt/Qt/6.10.3/gcc_64
/Users/me/Qt/6.10.3/macos
```

Alternatively, set `Qt6_DIR` to that kit's `lib/cmake/Qt6` directory.

## Dependency downloads

The core uses CPM/CMake to obtain third-party libraries such as Taskflow, nlohmann/json, QuaZip, zstd, Valijson, and Advanced Docking System. The first configure can therefore take longer and requires access to their upstream repositories. Subsequent configurations normally reuse the local cache.

Allow sufficient disk space for Qt, the source tree, a build tree, downloaded dependencies, and the installed application. On memory-constrained machines, reduce the number of parallel compiler jobs; see {doc}`troubleshooting`.

