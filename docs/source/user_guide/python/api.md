# Python data API

The public high-level API is provided by `mvstudio.data`. The list below is a practical orientation, not a replacement for the upstream API reference.

## Hierarchy

```python
import mvstudio.data

dh = mvstudio.data.Hierarchy()
```

The current Python source constructs `Hierarchy()` with `Item.LoadOption.Immediate`; this means point matrices are loaded while the hierarchy is built. The upstream API page currently describes delayed loading as the default. Treat the source behavior as authoritative for the installed plugin version and verify this default when upgrading.

`Hierarchy` supports `refresh()`, `children()`, and recursive lookup with `getItem(itemId)`, `getItemByDataID(datasetId)`, `getItemByName(name)`, and `getItemByIndex(index)`.

Datasets can be created with:

- `addPointsItem(data, name, parentDataId="", dimensionNames=[])` for a two-dimensional, C-contiguous NumPy array;
- `addDerivedPointsItem(data, name, sourceDataId, dimensionNames=[])` for points derived from an existing dataset with the same number of rows;
- `addImageItem(data, name, dimensionNames=[])` for a two- or three-dimensional image array;
- `addClusterItem(parent, indices, name, **kwargs)` for clusters described by point-index arrays, with optional `names` and `colors`.

## Items

All items provide `itemId`, `datasetId`, `name`, `type`, `rawname`, `rawsize`, `children()`, `getSelection()`, and `setLinkedData()`. Point items additionally provide `points`, `numpoints`, `numdimensions`, `dimensionNames`, `properties`, `getProperty(name)`, `getPoints(rows=None, dimensions=None)`, and `getSelectedPoints(dimensions=None)`.

`getPoints` returns a two-dimensional NumPy array. `None` selects an entire axis; supplied row and dimension indices must be one-dimensional, nonnegative integers. Use `np.uint32` for selection IDs. Point arrays passed to creation methods must be C-contiguous.

The upstream API page also lists `setSelection(selectionIDs)`. The current Python source contains an undefined-variable check in that method before it reaches the bridge call, so selection writing should be treated as a known implementation discrepancy and verified against the installed plugin version.

`ClusterItem.cluster` exposes ordered `names`, `indices`, `cluster_guids`, and `colors`. `ImageItem.image` exposes the image array and caches it after the first access.

The authoritative, version-specific API list is the upstream [`Available_functions.md`](https://github.com/ManiVaultStudio/JupyterPlugin/blob/main/docs/Available_functions.md). Check that document and the Python source before documenting a new method or relying on a default.
