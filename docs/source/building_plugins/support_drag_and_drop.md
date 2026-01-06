# Supporing data drag-and-drop on your view plugin
The easiest way to allow users to deal with datasets in your plugin is to allow them to drag and drop a dataset onto the plugin widget.
The ManiVault library provides a DropWidget class to make this process easier. In order to add it into your custom plugin, add the DropWidget as a class member.

The DropWidget can be instantiated with the QWidget derivative that the user should drop their dataset on.
```Cpp
_dropWidget = new DropWidget(_someWidget);
```

The DropWidget can then be initialized with a lambda function that returns a number of DropRegions which allow the user to drop their datasets for different purposes.
```Cpp
_dropWidget->initialize([this](const QMimeData* mimeData) -> DropWidget::DropRegions {
    DropWidget::DropRegions dropRegions;
    return dropRegions;
});
```

## Minimal Implementation Example
A rough minimal example of how to allow your plugin to accept dropped datasets is given below. For a more full working example, see the [ExampleViewPlugin](https://github.com/ManiVaultStudio/ExamplePlugins/blob/master/ExampleView/src/ExampleViewPlugin.cpp).
```Cpp
#include <ViewPlugin.h>
#include <widgets/DropWidget.h>
#include <PointData/PointData.h>
#include <DatasetsMimeData.h>
#include <QLabel>

using namespace mv;

class ExampleViewPlugin: public ViewPlugin
    Q_OBJECT
{
    ExampleViewPlugin(const PluginFactory* factory) :
        ViewPlugin(factory),
        _dropWidget(nullptr),
        _currentDataset(),
        _currentDatasetNameLabel(new QLabel())
    {
        // Set the drop widget to accept drag and drop behaviour
        _currentDatasetNameLabel->setAcceptDrops(true);
    }

    /** This function is called by the core after the view plugin has been created */
    void init() override
    {
        // Make a new layout, add the widget on which we will drop datasets to it, and set the layout as the plugin widget layout
        auto layout = new QVBoxLayout();
        layout->addWidget(_currentDatasetNameLabel);
        getWidget().setLayout(layout);

        // Initialize the drop widget
        _dropWidget = new DropWidget(_currentDatasetNameLabel);

        // Set the drop indicator widget (the widget that indicates that the view is eligible for data dropping)
        _dropWidget->setDropIndicatorWidget(new DropWidget::DropIndicatorWidget(&getWidget(), "No data loaded", "Drag an item from the data hierarchy and drop it here..."));

        // Initialize the drop regions
        _dropWidget->initialize([this](const QMimeData* mimeData) -> DropWidget::DropRegions {
            const auto datasetsMimeData = dynamic_cast<const DatasetsMimeData*>(mimeData);

            // Test if the drag & drop mime data is valid
            if (datasetsMimeData == nullptr)
                return dropRegions;

            // Test whether the drag & drop mime data contains at least one dataset
            if (datasetsMimeData->getDatasets().count() > 1)
                    return dropRegions;

            // Gather information about the dataset about to be dropped
            const auto dataset = datasetsMimeData->getDatasets().first();
            const auto datasetId = dataset->getId();

            // Get the points dataset from core, we assume here a points dataset is dropped, should be checked!
            auto candidateDataset = _core->requestDataset<Points>(datasetId);

            // Add the drop region saying the dataset can be dropped here, and if it is, store it in _currentDataset
            dropRegions << new DropWidget::DropRegion(this, "Points", description, "map-marker-alt", true, [this, candidateDataset]() {
                _currentDataset = candidateDataset;
            });

            return dropRegions;
        });
    }

    DropWidget*            _dropWidget;                // Widget for drag and drop behavior
    hdps::Dataset<Points>  _currentDataset;            // Where we store the dropped dataset
    QLabel*                _currentDatasetNameLabel;   // Some widget on which the dataset must be dropped
}
```


