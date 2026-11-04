# Python in ManiVault Studio

ManiVault Studio supports several Python workflows, maintained in separate repositories:

- **Jupyter and interactive Python** connect to a running ManiVault Studio instance so that you can inspect, manipulate, and create data from a notebook. See {doc}`Jupyter and interactive Python <jupyter>`.
- **Python script extensions** package Python code as ManiVault operations such as loaders, analyses, transformations, writers, and views. See {doc}`Python script extensions <scripts>`.
- **Python View Plugin** embeds a PySide6 widget written in Python as a ManiVault view. This is a separate experimental plugin; see {doc}`Python views <views>`.

Jupyter notebooks and script extensions use the `mvstudio.data` package. Python View Plugin currently uses the lower-level `mvstudio_core` bindings and a `create_view(context)` entry point. Choose the workflow that matches the task: a notebook for exploration, a script extension for a repeatable operation, or a Python view for a custom interactive visualization.

```{toctree}
:maxdepth: 1

bridge
jupyter
api
scripts
examples
views
```
