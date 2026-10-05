# Python in ManiVault Studio

ManiVault Studio provides a Python bridge for accessing and extending a running application. The bridge is the common foundation for two workflows:

- **Jupyter and interactive Python** connect to a running ManiVault Studio instance so that you can inspect, manipulate, and create data from a notebook.
- **Python scripts** package Python code as ManiVault operations such as loaders, analyses, transformations, writers, and views.

Interactive notebooks and script extensions use the same `mvstudio.data` data model. Choose the workflow that matches the task: use a notebook for exploration and iteration, or a script extension when functionality should appear as a repeatable ManiVault operation.

```{toctree}
:maxdepth: 1

bridge
jupyter
api
scripts
examples
```
