# Building with DevBundle

[DevBundle](https://github.com/ManiVaultStudio/DevBundle) creates a coordinated workspace containing the ManiVault core and selected plugins. Use it when you want to develop several ManiVault repositories together rather than clone and configure each repository separately.

```{important}
DevBundle's default configuration obtains binary dependencies from the ManiVault Artifactory service. Access can require project credentials. If you do not have access, use the {doc}`public manual CMake route <manually>` with your own Qt installation.
```

## Install and inspect the tool

Clone DevBundle, enter its directory, and install its Python requirements as described in its README. Then inspect the available bundles:

```console
python makeproject.py list
```

The current `basic` bundle is a useful starting point: it combines the core, CSV loader, and scatterplot plugin. Bundle membership is defined by DevBundle's `config.json` and can change over time.

## Create a workspace

Run DevBundle from the parent directory in which its configured bundle directory should be created:

```console
python makeproject.py use basic
```

DevBundle clones the selected repositories and writes an umbrella CMake project. The bundle's `build_dir` in `config.json` determines the output directory relative to where the script runs. Add `--ssh` if your GitHub setup uses SSH URLs:

```console
python makeproject.py use basic --ssh
```

Add `--cmake` to open CMake GUI after DevBundle creates the workspace. Configure and generate from there, or open the generated workspace with another CMake-aware IDE.

If you already maintain a compatible Qt installation, skip DevBundle's Qt binary and configure the generated project with your Qt path. The binary identifier is versioned, so read its current name from `config.json`; for example:

```console
python makeproject.py use basic --skip_binary QT6103
```

## Use local repositories or a custom bundle

DevBundle supports a custom configuration file:

```console
python makeproject.py use --cfg_file D:/ManiVault/my-config.json my_bundle
```

This is useful for pinning forks, branches, or a different set of plugins. Its `cmake_only` mode can regenerate the aggregate CMake project without cloning repositories again:

```console
python makeproject.py use --cfg_file D:/ManiVault/my-config.json my_bundle --mode cmake_only
```

Shared CMake options can be added with `-D`, for example `-D MV_UNITY_BUILD ON`. Consult [DevBundle's README](https://github.com/ManiVaultStudio/DevBundle) for its complete command-line interface. Consult its current [`config.json`](https://github.com/ManiVaultStudio/DevBundle/blob/master/config.json) rather than copying version identifiers from old tutorials.

## Configure the generated project

If you supply your own Qt installation, make sure the generated project can find it through `CMAKE_PREFIX_PATH` or `Qt6_DIR`. The same ManiVault build options described in {doc}`configuration` apply to the core inside the bundle.

After configuration, build `MV_Application`. The resulting executable and SDK are placed under the configured install directory. Continue with {doc}`running_and_next_steps`.
