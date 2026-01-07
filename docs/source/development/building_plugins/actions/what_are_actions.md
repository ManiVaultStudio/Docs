# What Are Action GUI Building Blocks?

Action GUI building blocks (simply called “actions”) are the fundamental interactive elements for **ManiVault** plugins. Each action represents a specific type of user interface control combined with logic to handle a parameter or command. Under the hood, actions wrap standard Qt widgets with additional functionality. ManiVault provides a library of built-in actions for common UI needs [1](https://ieeexplore.ieee.org/document/10290921), including:

- **StringAction** – a text input field (single-line or multi-line) for string parameters.-
- **DecimalAction** and **IntegralAction** – numeric inputs for floats or integers (with spinboxes, sliders, or both for adjusting values).
- **OptionsAction** – a drop-down or list selector for choosing among multiple options.
- **ToggleAction** – a boolean toggle (e.g. a checkbox or switch) for on/off settings.
- **TriggerAction** – a push-button to trigger an action or event.
- **ColorAction** / **ColormapAction** – color picker controls (single colors or entire color maps).
- **FilePickerAction** (and **DirectoryPickerAction**) – file dialog launchers for selecting files or folders.
- **SelectionAction** – a specialized widget for selecting data points (with modes like brush, lasso, etc., often used in visual analytics)
- **DimensionPickerAction** – a UI for picking one or multiple data dimensions (e.g. selecting which dimensions of a dataset to use).
- **GroupAction** – a container that groups other actions under a collapsible panel or section (useful for organizing related controls).