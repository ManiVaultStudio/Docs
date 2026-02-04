# Raw data
 
Raw data is a crucial part of the dataset API. During its lifetime, raw data is tracked by the global {cpp:class}`mv::AbstractDataManager` with the use of dedicated models. The classes below are used to store, present and filter raw data.

```{note}
This API is **stable** and intended for use by **core developers**. Plugin developers should not interact with it directly, as it is fully wrapped by the data manager.
```

```{toctree}
:maxdepth: 1

raw_data_model
raw_data_filter_model
```

