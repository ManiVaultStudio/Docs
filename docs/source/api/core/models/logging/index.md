# Logging

These models present the structured records captured by the application {doc}`Logger <../../util/logging/logger>`. `LoggingModel` incrementally exposes new records, while `LoggingFilterModel` supplies severity and text filtering plus sorting for user interfaces.

The models do not form the plugin logging entry point. Plugins emit Qt log messages; the global logger captures them and owns the underlying records. See {doc}`Core logging <../../util/logging/index>` for the complete pipeline.

```{toctree}
:maxdepth: 1

logging_model
logging_filter_model
```
