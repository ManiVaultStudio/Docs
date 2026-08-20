# Building with DevBundle

[DevBundle](https://github.com/ManiVaultStudio/DevBundle) is the primary way to create a ManiVault development environment. It assembles the core, a chosen set of plugins, and their compatible prebuilt binary dependencies into one CMake workspace. In the normal DevBundle workflow, you do **not** install and configure Qt separately: DevBundle downloads the configured Qt package and tells CMake and the debugger where to find it.

This makes DevBundle more than a repository-cloning script. It captures the build environment shared by the selected projects and removes much of the version and path coordination that a manual build requires.

## What DevBundle automates

A bundle definition describes the repositories, branches or tags, project relationships, and binary dependencies that belong together. When you select a bundle, DevBundle:

1. Creates a self-contained development directory with `source`, `build`, and `install` subdirectories.
2. Clones the core and selected plugin repositories at the revisions named by the bundle.
3. Determines the union of prebuilt binaries required by those repositories.
4. Downloads the package for the current operating system and extracts it into DevBundle's shared `binaries` directory.
5. Generates a top-level `CMakeLists.txt` that adds the repositories in dependency order.
6. Sets `MV_INSTALL_DIR` to the bundle's own `install` directory.
7. Adds dependency-specific CMake variables such as `CMAKE_PREFIX_PATH`, `Qt6_DIR`, and any plugin-library package paths.
8. Adds binary directories to the debugger environment where required, so the built application can locate runtime libraries.
9. Sets `MV_Application` as the Visual Studio startup project.

The resulting workspace has a predictable layout:

```text
DevBundle/
├── binaries/                 shared prebuilt packages
└── basic/                    one isolated development bundle
    ├── source/
    │   ├── CMakeLists.txt    generated umbrella project
    │   ├── core/
    │   ├── CsvLoader/
    │   └── Scatterplot/
    ├── build/                generated build tree
    └── install/              runnable ManiVault and plugin SDK
```

Different bundles can live side by side without sharing build or install trees. Their downloaded binary packages are cached centrally so another compatible bundle does not need to download the same archive again.

## What you still install locally

DevBundle supplies configured binary packages such as Qt; it does not replace the native development toolchain. Install:

- Git;
- Python with the `gitpython` and `requests` packages;
- CMake 3.22 or newer;
- a C++20-capable compiler and its platform SDK;
- system libraries required by the platform, particularly on Linux.

You only need a separate Qt installation when you intentionally skip the configured Qt binary or cannot access the binary service. See {doc}`prerequisites` for the compiler and platform baseline.

## Install DevBundle

Clone the repository and install its Python dependencies:

```console
git clone https://github.com/ManiVaultStudio/DevBundle.git
cd DevBundle
python -m pip install -r requirements.txt
```

You can also install the two direct Python requirements individually:

```console
python -m pip install gitpython requests
```

All following commands are run from the DevBundle checkout.

## Inspect the available bundles

List the configured environments:

```console
python makeproject.py list
```

Inspect one definition before creating it:

```console
python makeproject.py list basic
```

The detailed output identifies the target directory, repositories and revisions, and required binaries. This is useful for confirming exactly what DevBundle will obtain before it changes the workspace.

The current `basic` bundle is a good starting point for most ManiVault development. It combines:

- the ManiVault core;
- the CSV loader;
- the scatterplot plugin;
- the configured platform-specific Qt package required by the core.

The broader `allmain` bundle combines the core with the main branches of many first-party plugins. Bundle membership changes as the project develops, so use `list` and the current [`config.json`](https://github.com/ManiVaultStudio/DevBundle/blob/master/config.json) instead of relying on a copied list.

## Create the bundle

Create the `basic` environment with HTTPS Git URLs:

```console
python makeproject.py use basic
```

DevBundle creates the directory selected by the bundle's `build_dir` setting inside the DevBundle checkout. During this operation it reports each cloned repository and each binary download. For the current `basic` configuration, the core declares the versioned Qt package as a binary dependency, so Qt is downloaded and wired into the generated CMake project automatically.

Use SSH repository URLs if that matches your GitHub setup:

```console
python makeproject.py use basic --ssh
```

For a faster initial clone when repository history is unnecessary, add `--shallow`:

```console
python makeproject.py use basic --shallow
```

## Configure and build

DevBundle prepares the workspace; CMake still performs the configure, generate, and build stages. The quickest graphical route is:

```console
python makeproject.py use basic --cmake
```

The `--cmake` option opens CMake GUI with `basic/source` and `basic/build` already selected. Configure with the desired platform generator, generate the project, and build `MV_Application`. The generated umbrella project already contains `MV_INSTALL_DIR` and the CMake paths for the downloaded Qt package, so you should not need to locate Qt manually.

For a single-configuration Ninja build, use:

```console
cmake -S basic/source -B basic/build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build basic/build --target MV_Application --config Release --parallel
```

For a multi-configuration generator, select the configuration at build time:

```console
cmake -S basic/source -B basic/build -G "Visual Studio 17 2022" -A x64
cmake --build basic/build --target MV_Application --config Release --parallel
```

On macOS, replace the Visual Studio generator and architecture with `-G Xcode`.

Building `MV_Application` installs the application, core SDK, and built plugins into `basic/install/<configuration>`. Run ManiVault from that installed tree. Because the core and plugins are part of one umbrella project, CMake also sees their intended build order and shared configuration.

## How prebuilt binaries are selected

The `repo_info` section of `config.json` associates repositories with named binary packages. The core currently requests a Qt package; plugins can add packages of their own—for example, a volume-rendering plugin can request a compatible VTK build. DevBundle gathers these requirements across the entire selected bundle, downloads each package once, and generates the package-specific CMake settings.

Each binary entry can provide different archives and settings for Windows, Linux, and macOS. For Qt, the generated settings include the package prefix and Qt CMake directory. A binary can also publish a runtime `bin` path, which DevBundle adds to the generated debugger environment.

This is the main reason to prefer DevBundle: the bundle configuration names the binary versions known to work with that collection of repositories. Developers do not independently choose a Qt or VTK build and then reproduce all associated CMake and runtime paths.

```{note}
The prebuilt packages are hosted by the ManiVault project on its Artifactory service. Access may require project credentials. If you do not have access, use the {doc}`manual CMake build <manually>` with a public Qt installation, or skip an individual DevBundle binary and provide a compatible local installation.
```

## Reuse your own Qt or another dependency

Skipping a binary is an advanced override, not the normal setup. Read the exact binary identifier from `python makeproject.py list <bundle>` or `config.json`, then pass it to `--skip_binary`. For example:

```console
python makeproject.py use basic --skip_binary QT6103
```

The generated project will no longer define the CMake variables or runtime path supplied by that Qt package. You must then configure `CMAKE_PREFIX_PATH` or `Qt6_DIR` yourself and ensure that the compiler, architecture, Qt version, modules, and runtime libraries are compatible.

## Work with an existing local repository

A custom bundle can refer to an existing checkout through a repository's `local` property. DevBundle adds that directory to the umbrella project without cloning or updating it. This is useful when developing a new plugin alongside the core:

```json
{
  "name": "my_plugin",
  "build_dir": "my_plugin",
  "mv_repos": [
    { "repo": "core", "branch": "master" },
    {
      "repo": "MyPlugin",
      "branch": "main",
      "local": "D:/Projects/MyPlugin"
    }
  ]
}
```

Copy the default configuration to a separate file rather than editing the shared definition, then select it with `--cfg_file`:

```console
python makeproject.py use --cfg_file D:/ManiVault/my-config.json my_plugin
```

The custom configuration must also contain the corresponding `repo_info` and `prebuilt_binaries` definitions needed by its repositories.

## Pass shared CMake options

Use `-D` or its long form, `--define_cmake_var`, to write a cache variable into the generated umbrella project:

```console
python makeproject.py use basic \
  -D MV_UNITY_BUILD ON \
  -D MV_USE_AVX OFF
```

These values become visible to every subproject. See {doc}`configuration` for core options; plugins may define additional settings.

## Regenerate or update an existing bundle

DevBundle currently supports three modes:

| Mode | Behavior |
|---|---|
| `clean` | Default. Recreates the bundle and clones its repositories again. |
| `cmake_only` | Preserves repository checkouts and regenerates only the umbrella `CMakeLists.txt`. |
| `update_only` | Pulls updates for the repositories without recreating the bundle. |

Regenerate CMake after changing a custom configuration:

```console
python makeproject.py use --cfg_file D:/ManiVault/my-config.json my_plugin --mode cmake_only
```

Update the configured repositories:

```console
python makeproject.py use basic --mode update_only
```

```{warning}
The default `clean` mode recreates the bundle directory, including its build and install trees. DevBundle checks cloned repositories for local or untracked changes and refuses to clean when it finds them, but you should still commit or back up important work before deliberately recreating an environment.
```

For all supported switches and the configuration schema, consult the current [DevBundle README](https://github.com/ManiVaultStudio/DevBundle). After a successful build, continue with {doc}`running_and_next_steps`.
