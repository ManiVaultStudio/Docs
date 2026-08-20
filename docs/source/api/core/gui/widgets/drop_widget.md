# DropWidget

**Qualified name:** `mv::gui::DropWidget`

`DropWidget` adds dataset-aware drag-and-drop regions to an existing Qt widget without requiring a custom widget subclass. The target supplies a callback that inspects the incoming MIME data and returns the operations applicable to that drag.

For setup, validation, ownership, and complete plugin-side patterns, begin with {doc}`Dataset drag and drop <../../../../development/building_plugins/drag_and_drop/index>`. Dataset hierarchy drags are represented by {doc}`DatasetsMimeData <../../data/datasets_mime_data>`.

```{doxygenclass} mv::gui::DropWidget
:members:
:protected-members:
```
