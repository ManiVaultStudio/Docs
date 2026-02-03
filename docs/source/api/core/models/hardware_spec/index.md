# Hardware Specs

A {cpp:class}`mv::util::HardwareSpec` is used by **ManiVault** to describe the system requirements of a project, including CPU capabilities, available memory, and disk capacity.

This specification can be extended to define both minimum and recommended hardware requirements. When a project is loaded, ManiVault can evaluate the current system against these requirements and notify the user if the available hardware does not meet the minimum specification, or if it falls below the recommended level.

The model classes below are for storing and filtering hardware specs.

```{toctree}
:maxdepth: 1

abstract_hardware_spec_model
hardware_spec_tree_model
hardware_spec_filter_model
```