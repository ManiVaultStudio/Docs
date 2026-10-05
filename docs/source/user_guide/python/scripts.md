# Python script extensions

Python scripts let users add ManiVault operations without writing and compiling a conventional C++ plugin. A script can load data, analyze or transform it, set selections, or write/export results. The JupyterPlugin runs the script in its embedded Python interpreter, so scripts can use the same `mvstudio.data` bridge as notebooks.

## Extension layout

A script extension normally consists of a Python script, a JSON descriptor, and optionally a requirements file:

```text
my_operation.py
my_operation.json
my_operation_requirements.txt
```

The descriptor requires `script`, `name`, and `type`. Supported operation types include `Loader`, `Writer`, `Analysis`, `Transformation`, and `View`. Optional `description`, `requirements`, and `input-datatypes` fields control discovery and placement in the ManiVault UI.

The `arguments` array describes the automatically generated input dialog. Its entries have `name`, `argument`, `type`, and `required`; argument types are `int`, `float`, `str`, `file-in`, `file-out`, and `mv-data-in`. File arguments can specify dialog and extension metadata. `mv-data-in` arguments can restrict accepted dataset types with `datatypes` and pass a dataset GUID to the script.

For scripts with a requirements file, the launcher checks the requirements in the selected Python environment. Missing requirements prevent the script from being loaded; they are not a substitute for distributing a separate environment.

## Script structure

Use `argparse` to parse the command-line arguments described by the JSON file. Keep application work in a `main(args)` function and import `mvstudio.data` there when the script needs to access ManiVault data. The launcher sets `sys.argv`, executes the script, and reports Python exceptions through the ManiVault logging path.

The upstream [Python script guide](https://github.com/ManiVaultStudio/JupyterPlugin/blob/main/docs/Python_scripts_for_ManiVault.md) is the source of truth for descriptor fields and UI argument behavior. The upstream [script examples](https://github.com/ManiVaultStudio/JupyterPlugin/tree/main/examples/scripts) show loader, writer, and analysis extensions.
