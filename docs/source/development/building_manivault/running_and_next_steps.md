# Running ManiVault and next steps

## Verify the installation

Run ManiVault from the configuration directory below `MV_INSTALL_DIR`. A successful first launch confirms that the executable can find the matching Qt libraries, ManiVault libraries, resources, and installed plugins.

If you built only the core, the application can contain fewer data loaders and views than a packaged release. That is expected: most user-facing capabilities are plugins in separate repositories. DevBundle's `basic` bundle includes a CSV loader and scatterplot view and is therefore a convenient minimal integration build.

## Build an example plugin

The [ExamplePlugins repository](https://github.com/ManiVaultStudio/ExamplePlugins) is the recommended next source checkout. Its examples demonstrate the plugin categories and give you small targets to compare with your own code.

Configure an example against the CMake package installed by the core:

```console
cmake -S ExamplePlugins -B examples-build \
  -DManiVault_DIR=/absolute/path/to/manivault-install/cmake/mv
```

Use the same compiler, architecture, Qt kit, and build configuration that you used for ManiVault. See {doc}`../building_plugins/fundamentals/index` for the conceptual plugin-development guide.

## Update a source build

Pull changes in each repository, reconfigure CMake, and rebuild `MV_Application`. Reconfiguration is important because dependencies, generated files, and build options can change. For a DevBundle workspace, follow DevBundle's update workflow so that repository revisions remain coordinated.

