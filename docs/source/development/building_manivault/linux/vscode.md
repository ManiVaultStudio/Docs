# Building with Visual Studio Code

Install the Microsoft **C/C++** and **CMake Tools** extensions, then open the core source directory. After completing {doc}`Linux prerequisites <index>`, select a kit with a C++20-capable compiler.

Add the required cache values to the workspace's CMake settings, using your actual paths:

```json
{
  "cmake.generator": "Ninja",
  "cmake.buildDirectory": "${workspaceFolder}/../core-build",
  "cmake.configureSettings": {
    "CMAKE_BUILD_TYPE": "Debug",
    "MV_INSTALL_DIR": "/absolute/path/to/manivault-install",
    "CMAKE_PREFIX_PATH": "/absolute/path/to/Qt/6.x/gcc_64"
  }
}
```

Run **CMake: Configure**, select `MV_Application` as the build target, and run **CMake: Build**. Configure the debugger to launch the installed executable beneath `MV_INSTALL_DIR`. Match the executable and plugin configuration to the active CMake build type.
