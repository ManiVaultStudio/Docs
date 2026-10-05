# Documentation maintenance instructions

## Python, Jupyter, and scripting documentation

The implementation-specific source of truth for ManiVault Studio's Python functionality is the `ManiVaultStudio/JupyterPlugin` repository. Before creating, reviewing, or modifying documentation about Python, Jupyter, Python scripts, script extensions, or the Python bridge, inspect the current upstream versions of:

- `tutorials/notebook_setup.md`
- `docs/Available_functions.md`
- `docs/Python_scripts_for_ManiVault.md`
- `examples/demo_data_loading.ipynb`
- `examples/scripts/`

Also inspect relevant JupyterPlugin source when documentation and implementation appear inconsistent. Prefer verified implementation behavior over stale prose and call out significant discrepancies.

The reconciliation workflow is:

1. Read the relevant upstream documentation and examples.
2. Compare them with the affected ManiVault documentation.
3. Check exposed APIs, signatures, behavior, setup and installation, bridge behavior, script-extension configuration, terminology, examples, and recommended usage.
4. Reconcile all affected ManiVault pages, examples, and cross-references.
5. Keep the ManiVault documentation higher-level and integrated with the rest of this site. Do not mechanically mirror upstream pages or create a competing source of truth.

When the requested change is broad (for example, “update the Python documentation”), inspect all of the sources above and consider pages beyond the one that first appears relevant.
