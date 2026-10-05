# Python bridge

The JupyterPlugin embeds a Python interpreter in ManiVault Studio and exposes low-level application bindings through `mvstudio_core`. The higher-level `mvstudio.data` package wraps those bindings in Python classes for navigating ManiVault's data hierarchy and exchanging NumPy arrays with the application.

The bridge is live: a `mvstudio.data.Hierarchy` reflects the data hierarchy of the connected ManiVault Studio instance. It can locate existing items by hierarchy ID, dataset ID, name, or index, and it can add points, image, derived-points, and cluster datasets. Item objects expose metadata, point and image data, selections, properties, and links between point datasets.

The same bridge is available when a script extension is executed by the JupyterPlugin. A script receives its configured command-line arguments, imports `mvstudio.data`, and communicates with the running application through the bridge.

## Connection model

When the Jupyter launcher starts a compatible Python environment, ManiVault Studio installs or checks the versioned `mvstudio.kernel` and `mvstudio.data` wheels and registers the ManiVault kernel with Jupyter. The kernel is connected to the embedded bridge; an ordinary Python process is not automatically connected to a running application.

The Python major and minor version must match a JupyterPlugin build available in the ManiVault installation. The selected interpreter and notebook working directory can be configured in the Jupyter Launcher settings.

For current implementation-specific details, see the upstream [JupyterPlugin architecture documentation](https://github.com/ManiVaultStudio/JupyterPlugin/blob/main/docs/Architecture.md) and [kernel manager documentation](https://github.com/ManiVaultStudio/JupyterPlugin/blob/main/docs/Kernel_manager.md).
