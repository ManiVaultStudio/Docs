# Building with Visual Studio

Visual Studio can open a generated solution or consume the source directory as a CMake project. Generating a solution keeps the command-line and IDE workflows identical and is the easiest setup to diagnose.

## Generate and open the solution

Complete the {doc}`Windows prerequisites <index>`, then run:

```powershell
cmake -S core -B core-build -G "Visual Studio 17 2022" -A x64 `
  -DMV_INSTALL_DIR=D:/ManiVault/install `
  -DCMAKE_PREFIX_PATH=C:/Qt/6.10.3/msvc2022_64

Start-Process core-build/ManiVault.sln
```

If the solution filename differs, open the `.sln` generated in `core-build`.

The same values can be entered through CMake GUI: select the source and build directories, configure with the Visual Studio 2022 x64 generator, set `MV_INSTALL_DIR` and `CMAKE_PREFIX_PATH`, then generate.

## Build and debug

Select `Release` or `Debug`, build the `MV_Application` target, and run the installed executable under the matching subdirectory of `MV_INSTALL_DIR`. The project supplies debugger properties for the installed application and its Qt runtime paths.

Do not mix configurations: a Debug plugin must be used with the compatible Debug core installation, and likewise for Release.

When changing the Visual Studio toolset, target architecture, or Qt kit, generate a fresh build directory. Those choices are foundational CMake cache entries.
