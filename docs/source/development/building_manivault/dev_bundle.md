## Using the DEV bundle tool

![DEV Bundle](../../assets/dev_bundle.png)  
*The DEV Bundle in action*

The preferred approach to building the **ManiVault** core and plugins is by using our [DevBundle](https://github.com/ManiVaultStudio/DevBundle) tool. This cross-platform tool creates self-contained development environments using build configurations in `JSON` format. Since the build environments are self-contained, multiple build environments can exist side-by-side. The major advantage of using **DevBundle** is that it will remove much of the configuration overhead by:

- Cloning repositories from the build configuration (with the branch specified in the build configuration)
- Downloading related binary dependencies from our Artifactory server (and adding/configuring paths in the `CMakeLists.txt`)
- Setting up an umbrella `CMakeLists.txt` which consists of all projects from the build configuration

```{note}
The allmain build config in the DevBundle config.json contains an example of how to add the core and plugins to a build configuration.
```

