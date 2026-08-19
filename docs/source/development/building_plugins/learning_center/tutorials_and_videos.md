# Tutorials and videos

Tutorials and videos live in global catalogs managed by `mv::help()`. A plugin instance associates relevant catalog entries with itself through `getLearningCenterAction()`. The view overlay then presents those entries without copying their content.

## Associate existing content by tag

The common path is to tag centrally registered content with the plugin kind and select it in the plugin constructor:

```cpp
ExampleViewPlugin::ExampleViewPlugin(
    const mv::plugin::PluginFactory* factory) :
    ViewPlugin(factory)
{
    auto& learningCenter = getLearningCenterAction();

    learningCenter.addTutorials({ "GettingStarted", "ExampleView" });
    learningCenter.addVideos({ "Practitioner", "ExampleView" });
}
```

An entry is selected when it has any of the supplied tags. Tag matching is case-sensitive, so establish a stable vocabulary and include a plugin-specific tag to avoid associating every general-purpose item accidentally.

Call these methods once during instance setup. They append pointers to the instance association and do not remove duplicates introduced by repeated calls.

## Supplying tutorials from a DSN

A plugin factory can contribute a remote JSON data source to the global tutorial catalog:

```cpp
ExampleViewPluginFactory::ExampleViewPluginFactory() :
    ViewPluginFactory(false)
{
    getTutorialsDsnsAction().addString(
        "https://example.org/manivault/learning-center.json"
    );
}
```

The core combines and deduplicates factory-provided DSNs, downloads them asynchronously, validates their `tutorials` array, and adds tutorials to the global model. Tutorial titles must be unique in that model.

A minimal feed has this shape:

```json
{
  "tutorials": [
    {
      "title": "Getting started with Example View",
      "tags": ["GettingStarted", "ExampleView"],
      "date": "2026-08-19",
      "icon": "braille",
      "summary": "Open a point dataset and configure the view.",
      "fullpost": "<h1>Example View</h1><p>Start by opening...</p>",
      "url": "https://example.org/tutorials/example-view",
      "project": null,
      "minimum-version-major": 1,
      "minimum-version-minor": 5,
      "plugins": ["Example View", "Points"]
    }
  ]
}
```

`fullpost` contains the rendered tutorial HTML. `project` may be a URL to a tutorial project or `null`. List every required plugin kind in `plugins`; the core uses that information to identify tutorials that cannot be opened in the current installation. Use a valid bundled icon name as described in {doc}`Icons <../icons>`.

The project-catalog DSNs exposed by `getProjectsDsnsAction()` serve a different purpose. Do not add ordinary project feeds to the tutorial DSN list unless they also implement the tutorial schema.

## Videos

The standard global video catalog is populated by the core's Learning Center feed. Associate videos by their tags with `addVideos()` as shown above. A YouTube entry stores the eleven-character video identifier; a GIF entry stores its resource path.

Core or application integrations can register content programmatically:

```cpp
auto* video = new mv::util::LearningCenterVideo(
    mv::util::LearningCenterVideo::Type::GIF,
    "Selecting points",
    { "ExampleView", "Selection" },
    "2026-08-19",
    "Demonstrates rectangle and lasso selection.",
    ":/ExampleView/tutorials/selection.gif"
);

mv::help().addVideo(video);
```

Register a global item exactly once, during application or catalog initialization. The global model reparents and owns the object. Plugin instances should then retrieve it by tag or receive its stable pointer through `addVideo()`.

`PluginLearningCenterAction::addVideo()` and `addTutorial()` store non-owning pointers; they do not adopt content created solely for one instance. Register the object with `mv::help()` first or otherwise guarantee that its lifetime exceeds every plugin association.

## Asynchronous availability

Remote catalogs load asynchronously. Tag lookup returns the items currently present; an association is not automatically refreshed merely because matching remote content arrives later. Arrange registration early enough, or react to the relevant catalog/model population signal and add newly available entries once. Avoid re-adding the entire result set without checking what the instance already holds.

Design help to degrade gracefully when the application is offline: the plugin itself should remain usable when a README, video thumbnail, or remote tutorial feed cannot be downloaded.

See the {doc}`LearningCenterTutorial API <../../../api/core/util/learning_center/learning_center_tutorial>` and {doc}`LearningCenterVideo API <../../../api/core/util/learning_center/learning_center_video>` for the complete data objects.
