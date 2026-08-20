# Building on Linux

The reference Linux build uses Ubuntu 24.04 and GCC 13 on x86-64. Other modern distributions can work with equivalent development packages.

On Ubuntu, install the compiler, CMake/Ninja, Git, and the native libraries required by the core and Qt WebEngine:

```console
sudo apt update
sudo apt install build-essential gcc-13 g++-13 cmake ninja-build git \
  libgl1-mesa-dev libxkbcommon-x11-0 libxcb-cursor0 libxcb-xinerama0 \
  libdbus-1-3 libnss3 libasound2-dev libpulse-dev
```

Install Qt 6.8 or newer separately using the Qt installer; the distribution's default Qt can be older than the required baseline. Include the modules listed in {doc}`../prerequisites`.

Configure with GCC 13 and Ninja:

```console
CC=gcc-13 CXX=g++-13 cmake -S core -B core-build -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DMV_INSTALL_DIR=/absolute/path/to/manivault-install \
  -DCMAKE_PREFIX_PATH=/absolute/path/to/Qt/6.x/gcc_64

cmake --build core-build --target MV_Application --parallel
```

```{toctree}
:maxdepth: 1

clion
vscode
```
