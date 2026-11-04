# Python views

The experimental [Python View Plugin](https://github.com/ManiVaultStudio/PythonViewPlugin) hosts a native PySide6 widget inside a ManiVault view. Its current example accepts one points dataset: drag it from the data hierarchy onto the view, and the plugin passes its `dataset_id` and `dataset_name` to the Python script.

The installed example script is `examples/PythonViewPlugin/basic_view.py`. It defines `create_view(context)` and returns a `PySide6.QtWidgets.QWidget`. The example reads the point matrix through the embedded `mvstudio_core` bindings and draws a scatterplot with PySide6. A script can raise an exception when data is missing or incompatible; the plugin displays the resulting Python error in the view.

```python
import mvstudio_core
from PySide6.QtWidgets import QLabel


def create_view(context):
    dataset_id = context["dataset_id"]
    points = mvstudio_core.get_data_for_item(dataset_id)
    return QLabel(f"{points.shape[0]:,} points loaded")
```

The Python interpreter is selected when the plugin is configured and built. The runtime adds that interpreter's user site-packages directory, so required packages such as PySide6 and NumPy must be available to that Python installation. Follow the plugin repository's current build instructions when setting up or packaging it.

This plugin is separate from Jupyter and Python script extensions. It uses the lower-level `mvstudio_core` bindings and the `create_view(context)` widget contract; notebooks and script extensions use `mvstudio.data`. For notebook setup and the higher-level data API, see {doc}`Jupyter <jupyter>` and {doc}`Python API <api>`. For a complete widget example, see [`basic_view.py`](https://github.com/ManiVaultStudio/PythonViewPlugin/blob/main/examples/basic_view.py).

The plugin repository's README still describes an earlier HTML-returning `render(context)` interface. The current plugin implementation and bundled example use `create_view(context)` and return a PySide6 widget; check the code for the version you build.
