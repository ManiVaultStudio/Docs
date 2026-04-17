# Building on Windows

## Installing environment variables
- Add a `QT_DIR` environment variable to your Qt install path (e.g. `C:\Qt\<QT_VERSION>\msvc2019_64\`) so that CMake can link ManiVault to Qt for a successful build.
- Add the location of the installed Qt libraries (e.g. `C:\Qt\<QT_VERSION>\msvc2019_64\bin`) to the user or system path variable so that the installed .exe might find these runtime libraries when you start it.

```{toctree}
:maxdepth: 1

xcode
```