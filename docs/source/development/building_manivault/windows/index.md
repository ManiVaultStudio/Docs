# Building on Windows

The reference Windows build uses Visual Studio 2022 on Windows Server 2022. Install:

- Visual Studio 2022 with **Desktop development with C++**;
- CMake support and a recent Windows SDK;
- a Qt 6.8-or-newer MSVC desktop kit with the modules listed in {doc}`../prerequisites`;
- Git.

From a Developer PowerShell, configure and build with the Visual Studio generator:

```powershell
cmake -S core -B core-build -G "Visual Studio 17 2022" -A x64 `
  -DMV_INSTALL_DIR=D:/ManiVault/install `
  -DCMAKE_PREFIX_PATH=C:/Qt/6.10.3/msvc2022_64

cmake --build core-build --target MV_Application --config Release --parallel
```

Forward slashes avoid quoting and escaping surprises in CMake values. Substitute your actual Qt and install paths.

```{toctree}
:maxdepth: 1

visual_studio
```
