# Exceptions and diagnostic context

Use `std::exception` types for ordinary C++ API failures. Use `mv::ManiVaultException` when the error needs ManiVault severity, separate user and technical text, structured details, source context, a diagnostic ID, and captured stack metadata.

```cpp
throw mv::ManiVaultException(
    mv::util::SeverityLevel::Error,
    tr("The dataset could not be imported."),
    QString::fromUtf8(exception.what()),
    __FUNCTION__,
    {
        { "Plugin kind", getKind() },
        { "File", filePath }
    });
```

Severity describes impact:

- `Info` communicates a non-failure outcome through diagnostic infrastructure;
- `Warning` indicates a recoverable degraded result;
- `Error` means the requested operation failed;
- `Fatal` is reserved for a state from which the application cannot safely continue.

Do not label routine input validation as fatal.

## Add context without losing the cause

When a `ManiVaultException` crosses a layer, `withAddedDetails()` can enrich a copy while preserving its diagnostic identity and existing evidence:

```cpp
catch (const mv::ManiVaultException& exception) {
    throw exception.withAddedDetails({
        { "Dataset ID", dataset.getDatasetId() }
    });
}
```

For a standard exception, wrap it once with a concise user message and retain `what()` as the technical cause.

## Present only at the owning boundary

`mv::util::exceptionMessageBox()` is a modal presentation API. Call it only at a GUI interaction boundary that has decided to consume the failure. Do not show a dialog and then rethrow the same exception, and do not call modal UI from worker threads.

Library-style helpers should throw or return a result rather than deciding how the application presents an error.
