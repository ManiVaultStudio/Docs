# Widgets

This section documents the reusable widget components provided by the core UI framework. These widgets are designed to cover common interaction patterns and visual elements used throughout the application and its plugins, ranging from basic UI helpers to more specialized components.

Most widgets documented here are safe to use and are intended to support custom views, tools, and plugin interfaces. They follow the same architectural and styling conventions as the rest of the GUI framework and are maintained as part of the public API.

In addition, the framework contains a set of widgets that are exposed publicly but primarily serve internal implementation needs. These are documented separately under the [internal widgets](internal/index) section and are used extensively by the core system and selected plugins. While they are accessible, they should generally be treated as implementation details rather than stable extension points.

```{toctree}
:maxdepth: 1

drop_widget
opengl_widget
file_dialog
elided_label