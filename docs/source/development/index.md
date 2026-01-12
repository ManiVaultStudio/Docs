Development
==================

This section describes the two primary ways of extending and integrating with the ManiVault ecosystem: by developing plugins or by building standalone applications on top of the core framework.

Plugins are the preferred mechanism for adding new functionality to an existing ManiVault installation. They allow features, tools, and visualizations to be developed, distributed, and maintained independently, while seamlessly integrating into the host application at runtime.

Building applications, on the other hand, is intended for scenarios where ManiVault is used as a foundation rather than a host. This approach enables the creation of fully customized executables that embed ManiVault components, apply application-specific branding and configuration, and define a controlled feature set tailored to a particular use case.

The following sections provide guidance for both workflows, outlining their respective build processes, project structures, and recommended practices, so you can choose the approach that best fits your development goals.

```{toctree}
:maxdepth: 1

   building_plugins/index
   building_applications/index
