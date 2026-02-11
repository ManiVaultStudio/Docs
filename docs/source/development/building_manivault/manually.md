# Setting up the build IDE Manually

This pages describes how to build **ManiVault** from source.

You can download ManiVault's source code from the repository on GitHub in any way you like, but the simplest is:

```git clone git@github.com:ManiVaultStudio/core.git```

## Dependencies

ManiVault uses [git](https://git-scm.com/) and [CMake](https://cmake.org/) for version control and as a meta-build system respectively.

The main build dependency that you need to set up is [Qt 6.8.0+](https://www.qt.io/download) with the additional libraries **Qt WebEngine**, **Qt WebChannel**, **Qt Positioning** and the {ref}`Qt5 Compatibility Module<notes>`. **ManiVault** plugins might make use of other additional libraries as well, e.g. the image loader plugin uses the **Qt Imaging Formats library**.

**ManiVault** is written in [C++20](https://en.cppreference.com/w/cpp/20.html) and requires a compatible compiler:

- **Windows**  
[Visual Studio 2022](app.vssps.visualstudio.com/_signin?realm=my.visualstudio.com&reply_to=https%3A%2F%2Fmy.visualstudio.com%2FDownloads%3Fq%3DVisual%2520Studio%25202022&redirect=1&mkt=nl-NL&protocol=cookieless&context=eyJodCI6MywiaGlkIjoiN2QxNmE5OTUtMDA0Mi1kMGZhLWRhZGQtYTQ4YzUzYWRkYjllIiwicXMiOnt9LCJyciI6IiIsInZoIjoiIiwiY3YiOiIiLCJjcyI6IiJ90&lltid=821f1bf6-c396-45a9-8def-49b9e346bb59#ctx=eyJTaWduSW5Db29raWVEb21haW5zIjpbImh0dHBzOi8vbG9naW4ud2luZG93cy5uZXQiLCJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20iXX01)
- **Mac**  
[Xcode 12.4](https://xcodereleases.com/) with [Apple Clang 12](https://releases.llvm.org/12.0.1/tools/clang/docs/ReleaseNotes.html) or newer
- **Linux**  
[gcc 11](https://gcc.gnu.org/gcc-11/) or newer

```{note}
Several build-dependencies are downloaded during the CMake configuration and include: [zlib](https://en.wikipedia.org/wiki/Zlib), [QuaZip](https://quazip.sourceforge.net/), [Qt-Advanced-Docking-System](https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System) and [biovault_bfloat16](https://github.com/N-Dekker/biovault_bfloat16). These are automatically set up and installed when compiling ManiVault.
```

<details>
<summary><strong>Windows</strong></summary>

To fully set up Qt:

- Add a `QT_DIR` environment variable to your Qt install path (e.g. `C:\Qt\6.8.2\msvc2019_64\`) so that CMake can link ManiVault to Qt for a successful build.
- Add the location of the installed Qt libraries (e.g. `C:\Qt\6.8.2\msvc2019_64\bin`) to the user or system path variable so that the installed **.exe** might find these runtime libraries when you start it.

</details>

<details>
<summary><strong>Linux</strong></summary>  

Tried on Ubuntu 24.04 using gcc 13.3.0 and CMake 3.28.3. Install build dependencies (building infrastructure, Qt packages, zlib):

```
sudo apt install build-essential cmake qt6-base-dev qt6-base-private-dev qt6-webengine-dev qt6-wayland qt6-svg-dev qt6-5compat-dev zlib1g libgl1-mesa-dev libxkbcommon-dev libtbb-dev libxcursor-dev libxcomposite-dev libxi-dev libnss3-dev libnspr4-dev libfreetype-dev libfontconfig1-dev libxtst-dev libasound2-dev libdbus-1-dev libxkbfile-dev libxcb-cursor0
```

<details>
<summary><strong>Ubuntu 22.04 (not recommended)</strong></summary>

```
sudo apt install build-essential libxkbcommon-dev libxkbfile-dev libtbb-dev libglew-dev fonts-font-awesome libgomp1 libgl1 libegl1 libcups2 libopengl0 libnss3-dev libasound2-dev libxkbcommon-x11-dev
```

</details>

</details>

## Project Configuration

### Install location

Building the plugin system library requires setting an installation path where you would like the executable and library to be installed to. **ManiVault** uses [CMake](https://cmake.org/) as it's build system. You'll need to set the variable `MV_INSTALL_DIR` to your install directory when configurating the CMake project, e.g. `D:/Documents/ManiVault/install/` or `/home/USERNAME/ManiVault/install/`.

### CMake GUI
1. Launch the **CMake GUI**
2. In the source code field browse to the local folder to which you cloned the ManiVault core repo, e.g. `D:/Documents/ManiVault/core`
3. In the build field copy the source code field but append `/Build` at the end. This will generate a new folder for all files necessary for building the project.s
4. Set the `MV_INSTALL_DIR` variable to your install directory, e.g. `D:/Documents/ManiVault/install`.
5. Press **Configure** and select the generator for your IDE of choice with the platform of **x64**. Press **Finish** to configure the project.
6. A lot of red paths should now appear. Check that the ones pointing to Qt directories seem correct and then press **Generate** to generate the solution for your given IDE.
7. Press **Open Project** to launch the IDE and the project.

## Compilation

<details>
<summary><strong>Windows (Visual Studio)</strong></summary>

You selected Visual Studio as the generator in the CMake GUI. After opening the project:
- At the top of Visual Studio set the build mode (where it says Debug) to Release.
- Right click the solution and press Build Solution, if this does not produce errors, continue to the next step.
- Right click the project MV_Application in the Solution Explorer and select "Set as Startup Project".
- Run the project with `Ctrl+F5` to launch **ManiVault**.

</details>

<details>
<summary><strong>Linux</strong></summary>

This recipe is for **Ubuntu 23.04** using **gcc 12.2.0** and **CMake 3.26.4**. In the cloned ManiVault core folder:

```bash
mkdir build
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DMV_INSTALL_DIR=/home/USERNAME/ManiVault/install -G "Unix Makefiles"
cmake --build build --config Release
```

Depending on your memory constraints, you can always append `-j N` with e.g. `N=4` as the number of parallel build jobs to the last command or use another generator like e.g. `-G "Ninja"`.

</details>

(notes)=
## Notes
- Both code and setup instructions might still reference *HDPS*, the placeholder development name of **ManiVault**.
- After first time compiling on macOS it might be necessary to manually moc the MainWindow.ui file:
```uic MainWindow.ui -o ui_MainWindow.h mv ui_MainWindow.h ../Build/```
- **ManiVault Studio** might not run properly on integrated/old graphics hardware (in some cases the application crashes). The solution is to run on high-performance (recent) graphics hardware. [This](https://pureinfotech.com/set-gpu-app-windows-10/) link demontrates how to do this.
- Check for **Qt5 Compatibility Module** to be available, if not, **Quazip** won't be available to CMake.
