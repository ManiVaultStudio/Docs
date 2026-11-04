# Python examples

Use the upstream examples as executable references rather than copying them into this documentation. They are maintained with the JupyterPlugin implementation and exercise the current bridge.

- [Interactive data-loading notebook](https://github.com/ManiVaultStudio/JupyterPlugin/blob/main/examples/demo_data_loading.ipynb): creates image data, looks up items, reads arrays, and creates clusters.
- [Cell image and mask loader](https://github.com/ManiVaultStudio/JupyterPlugin/tree/main/examples/scripts): a loader using file arguments and the data bridge.
- [Image PNG writer](https://github.com/ManiVaultStudio/JupyterPlugin/blob/main/examples/scripts/write_image_as_png.py): a writer using a dataset argument and an output-file argument.
- [Image-mask selection analysis](https://github.com/ManiVaultStudio/JupyterPlugin/blob/main/examples/scripts/select_image_mask.py): demonstrates passing dataset IDs and a threshold to an analysis script. Its call to `setSelection()` currently reaches the implementation discrepancy described in the {doc}`Python API notes <api>`, so verify against the plugin version in use before running it.

Before running notebook examples, follow the upstream [notebook setup tutorial](https://github.com/ManiVaultStudio/JupyterPlugin/blob/main/tutorials/notebook_setup.md) and install the example requirements in the selected environment.
