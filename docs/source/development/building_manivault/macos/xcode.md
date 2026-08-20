# Building with Xcode

Complete the {doc}`macOS prerequisites <index>` and make sure the intended Xcode installation is active:

```console
xcode-select -p
```

Generate the project:

```console
cmake -S core -B core-build -G Xcode \
  -DMV_INSTALL_DIR=/absolute/path/to/manivault-install \
  -DCMAKE_PREFIX_PATH=/Users/me/Qt/6.x/macos

open core-build/ManiVault.xcodeproj
```

If the generated project has a different filename, open the `.xcodeproj` in `core-build`. Select the `MV_Application` scheme and the desired build configuration, then build. The target installs the application into the matching configuration subtree beneath `MV_INSTALL_DIR`.

For debugging, launch the installed application bundle. Ensure that Xcode, Qt, and any plugin dependencies all target the same architecture. Use a fresh build directory when switching between ARM64 and x86-64 or between Qt kits.
