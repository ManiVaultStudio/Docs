# Dataset handles

`mv::Dataset<T>` is a typed, event-aware reference to a core-owned dataset implementation.

```cpp
#include <Dataset.h>
#include <PointData/PointData.h>

mv::Dataset<Points> points;
```

## Validity and access

Check validity before using `operator->`, dereferencing, or calling `get()`:

```cpp
if (!points.isValid())
    return;

const auto name = points->getGuiName();
```

`operator->` and `get()` can return `nullptr`; they do not create or recover a missing dataset. Dereferencing an invalid handle is an error.

Handles compare by dataset identifier through their `DatasetPrivate` state. Two handles can therefore identify the same dataset even when created independently.

## Typed conversion

An untyped handle uses `DatasetImpl`:

```cpp
mv::Dataset<mv::DatasetImpl> dataset = obtainDataset();
mv::Dataset<Points> points(dataset);

if (!points.isValid())
    return;
```

Only convert when the concrete type is known from the data type, plugin contract, or another reliable check. A template argument documents the expected implementation; it does not perform user-facing type negotiation.

## Retaining handles

Store the handle itself as a member when a plugin or action observes a dataset:

```cpp
class DatasetConsumer : public QObject
{
    Q_OBJECT

public:
    void setDataset(const mv::Dataset<Points>& points);

private:
    mv::Dataset<Points> _points;
};
```

Keeping a raw `Points*` would bypass automatic invalidation. Keeping only an ID is appropriate for serialized references, but normal runtime access is safer through `Dataset<T>`.

## Signals

Dataset handles expose signals including `dataChanged`, `dataDimensionsChanged`, `dataSelectionChanged`, `guiNameChanged`, `childAdded`, `childRemoved`, `aboutToBeRemoved`, and `removed`.

The handle registers for core events when these signals gain connections. Keep the handle object alive for as long as its connections are required. When replacing a stored handle, disconnect callbacks tied to the old handle before assigning the new one.

```cpp
disconnect(&_points, nullptr, this, nullptr);
_points = points;

connect(&_points, &mv::Dataset<Points>::dataChanged,
        this, &DatasetConsumer::updateFromData);
```
