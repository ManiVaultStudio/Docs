# Jupyter notebooks

## Getting started

1. Create a Python environment whose major and minor version is supported by an installed JupyterPlugin build.
2. In ManiVault Studio, open the Jupyter launcher near the lower-right taskbar and choose **Start Jupyter Kernel and Lab** for that Python version.
3. Select the environment's Python interpreter when prompted. The launcher can remember this choice in **File → Settings → Plugin: Jupyter Launcher**.
4. Allow the launcher to install the matching ManiVault Python wheels and Jupyter kernel specification when they are not already present.
5. Open a notebook in the Jupyter environment and import the bridge:

```python
import mvstudio.data

hierarchy = mvstudio.data.Hierarchy()
print(hierarchy)
```

The upstream setup tutorial notes that notebook-specific dependencies are not necessarily part of the bridge environment. Install the requirements for an example before running it; for example, the current `demo_data_loading.ipynb` uses NumPy, scikit-image, and Matplotlib.

## Working with data

The usual workflow is to create a `Hierarchy`, retrieve an `Item`, inspect or transform its NumPy data, and optionally add the result back to ManiVault Studio. The hierarchy index printed by `print(hierarchy)` is convenient for exploration; dataset IDs are more stable when a notebook needs to refer to a particular dataset.

```python
import mvstudio.data

hierarchy = mvstudio.data.Hierarchy()
points = hierarchy.getItemByName("My points")

if points is not None:
    selected = points.getSelectedPoints(dimensions=[0, 1])
    current_selection = points.getSelection()
```

For a complete round trip, consult the upstream [demo data-loading notebook](https://github.com/ManiVaultStudio/JupyterPlugin/blob/main/examples/demo_data_loading.ipynb), which demonstrates image creation, hierarchy lookup, point access, and clusters.

## Boundaries

The notebook kernel is associated with the ManiVault Studio instance that launched it. Keep the notebook running while using bridge objects, and refresh the `Hierarchy` after application-side changes when a current tree is needed.
