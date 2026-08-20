# Building manually with CMake

This route builds the public [core repository](https://github.com/ManiVaultStudio/core) directly. Complete {doc}`prerequisites` first.

## 1. Clone the source

```console
git clone https://github.com/ManiVaultStudio/core.git
```

Use `git@github.com:ManiVaultStudio/core.git` instead if your GitHub account is configured for SSH. Create separate build and install directories; keeping them outside the checkout makes it easy to discard generated state without touching source files.

## 2. Configure

For a single-configuration generator such as Ninja:

```console
cmake -S core -B core-build -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DMV_INSTALL_DIR=/absolute/path/to/manivault-install \
  -DCMAKE_PREFIX_PATH=/absolute/path/to/Qt/6.x/compiler-kit
```

For a multi-configuration generator such as Visual Studio or Xcode, omit `CMAKE_BUILD_TYPE`:

```console
cmake -S core -B core-build \
  -DMV_INSTALL_DIR=/absolute/path/to/manivault-install \
  -DCMAKE_PREFIX_PATH=/absolute/path/to/Qt/6.x/compiler-kit
```

`MV_INSTALL_DIR` is required. Use absolute paths to avoid ambiguity between the source, build, and install trees. The first configuration downloads third-party dependencies and can take several minutes.

Before proceeding, confirm that configuration ends successfully and that CMake selected the expected compiler and Qt kit. If either is wrong, correct the command and use a fresh build directory.

## 3. Build and install

```console
cmake --build core-build --target MV_Application --config Release --parallel
```

`--config Release` matters for Visual Studio and Xcode and is harmless with most single-configuration workflows. Building `MV_Application` triggers the post-build installation into `MV_INSTALL_DIR`. To limit memory use, replace `--parallel` with a job count, for example `--parallel 4`.

## 4. Run the installed application

The exact executable path is platform-specific and configuration-specific. Typical locations are:

- Windows: `<MV_INSTALL_DIR>/Release/ManiVault Studio.exe`
- Linux: `<MV_INSTALL_DIR>/Release/ManiVault Studio`
- macOS: an application bundle under `<MV_INSTALL_DIR>/Release`

Inspect the generated install tree if the platform's packaging conventions produce a slightly different name. Run this installed copy so that its libraries, resources, and plugins are resolved consistently.

For platform and IDE details, continue with {doc}`windows/index`, {doc}`linux/index`, or {doc}`macos/index`. For optional build switches, see {doc}`configuration`.
