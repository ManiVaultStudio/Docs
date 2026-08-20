# Building with CLion

Open the core source directory in CLion after completing {doc}`Linux prerequisites <index>`. In **Settings | Build, Execution, Deployment | CMake**, create a profile with:

- **Build type:** `Release` or `Debug`;
- **Toolchain:** a C++20-capable GCC or Clang toolchain;
- **Generator:** Ninja is recommended;
- **CMake options:** `-DMV_INSTALL_DIR=/absolute/install/path -DCMAKE_PREFIX_PATH=/absolute/Qt/6.x/gcc_64`.

Reload the CMake project and confirm in the configure log that CLion selected the intended Qt kit and compiler. Build the `MV_Application` target.

For running and debugging, create a configuration that launches the installed executable beneath `MV_INSTALL_DIR`, rather than an intermediate binary in CLion's build directory. If you change compiler or Qt kit, use a new CMake profile and build directory.
