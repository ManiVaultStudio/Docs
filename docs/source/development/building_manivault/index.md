# Building ManiVault

Building ManiVault produces both the desktop application and the development files that plugins use. This section takes you from a source checkout to a runnable installation, then points you to plugin examples that build against it.

## Choose a build path

| Goal | Recommended path |
|---|---|
| Set up a complete ManiVault development environment | {doc}`DevBundle <dev_bundle>` — recommended |
| Build the public core repository with standard CMake | {doc}`Manual CMake build <manually>` |
| Work on the core in an IDE | Follow the manual build, then use the relevant platform page |
| Use ManiVault without changing its source | Install a published binary release |

DevBundle is the primary build path. It coordinates compatible core and plugin revisions, downloads the configured prebuilt dependencies—including Qt—and generates the CMake and runtime paths required by the complete workspace. This avoids independently installing and matching each binary dependency. Access to the project's binary service may require credentials.

The public manual route remains available when you only need the core, want complete control over dependency installations, or cannot use the configured binary service. In that workflow, you install Qt and provide its location to CMake yourself.

## The build model

Keep three locations distinct:

- **Source directory** — the `core` Git checkout.
- **Build directory** — generated files and compiler output; keep this outside the source tree.
- **Install directory** — the runnable ManiVault tree and public development files, selected with `MV_INSTALL_DIR`.

The `MV_Application` target performs the installation step after it builds. Run the application from the install directory, not from an intermediate compiler-output directory.

```text
core source ──configure──> build directory ──build MV_Application──> MV_INSTALL_DIR
                                                                    ├── application
                                                                    ├── libraries
                                                                    ├── headers
                                                                    └── cmake/mv
```

The repository README previously pointed to a GitHub Installation wiki page. That page is no longer a dependable entry point, so the maintained procedure lives here and is checked against the current CMake project and CI configuration.

```{toctree}
:maxdepth: 2

prerequisites
dev_bundle
manually
windows/index
linux/index
macos/index
configuration
running_and_next_steps
troubleshooting
```

## Authoritative references

- [ManiVault core repository](https://github.com/ManiVaultStudio/core)
- [DevBundle repository](https://github.com/ManiVaultStudio/DevBundle)
- [ExamplePlugins repository](https://github.com/ManiVaultStudio/ExamplePlugins)
- [Qt installation documentation](https://doc.qt.io/qt-6/get-and-install-qt.html)
