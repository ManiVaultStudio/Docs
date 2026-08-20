# Accepting datasets

## Set up the target

`DropWidget` observes the target through an event filter. The target itself must accept drops, and the region-producing callback must be installed before a drag can reach it:

```cpp
#include <DatasetsMimeData.h>
#include <PointData/PointData.h>
#include <widgets/DropWidget.h>

using mv::gui::DropWidget;

void ExampleViewPlugin::init()
{
    auto* target = &getWidget();
    target->setAcceptDrops(true);

    _dropWidget = new DropWidget(target);
    _dropWidget->initialize(
        [this](const QMimeData* mimeData) -> DropWidget::DropRegions {
            // Validate the payload and return applicable regions here.
            return {};
        });
}
```

Keep the `DropWidget` as a member when other plugin code needs to change its indicator or visibility. Qt owns it through the target widget, so the member is non-owning.

## Inspect and validate the payload

Data-hierarchy drags use `mv::DatasetsMimeData`. Reject unrelated Qt drags by returning no regions. Then validate cardinality and data type before constructing a typed handle:

```cpp
_dropWidget->initialize(
    [this](const QMimeData* mimeData) -> DropWidget::DropRegions {
        const auto* datasetsMimeData =
            dynamic_cast<const mv::DatasetsMimeData*>(mimeData);

        if (datasetsMimeData == nullptr ||
            datasetsMimeData->getDatasetsCount() != 1)
            return {};

        const auto& dataset = datasetsMimeData->getDatasetsRef().first();

        if (!dataset.isValid() || dataset->getDataType() != PointType)
            return {};

        const mv::Dataset<Points> points(dataset);

        if (!points.isValid())
            return {};

        return {
            new DropWidget::DropRegion(
                _dropWidget,
                "Use points",
                QString("Visualize %1").arg(points->getGuiName()),
                "file-import",
                true,
                [this, points]() { setPoints(points); })
        };
    });
```

Check `getDataType()` before converting the untyped handle. `Dataset<T>` documents and provides typed access; it is not a substitute for negotiating the incoming type. For more about handles, see {doc}`Dataset handles <../data/dataset_handles>`.

Use `getDatasetsRef()` while inspecting the payload to avoid copying its vector of handles. Use `getDatasetsCount()` when only the cardinality matters.

## Retain the handle, not a raw pointer

The drop callback should normally pass or store an `mv::Dataset<T>`:

```cpp
void ExampleViewPlugin::setPoints(const mv::Dataset<Points>& points)
{
    if (!points.isValid())
        return;

    _points = points;
    updateView();
}
```

A dataset may be removed later, so code that uses the stored handle must continue to check `isValid()`. If a drop starts asynchronous work, validate the captured handle again when that work actually reads from or publishes to the dataset.
