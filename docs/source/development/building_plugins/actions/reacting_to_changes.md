# Reacting to action changes

Connect to the signal that represents the semantic change your plugin needs. Value actions expose typed signals such as `valueChanged`, `stringChanged`, `toggled`, or `currentIndexChanged`; trigger actions expose a trigger signal.

```cpp
connect(&_pointSizeAction, &mv::gui::DecimalAction::valueChanged,
        this, [this](float pointSize) {
            _renderer.setPointSize(pointSize);
            getWidget().update();
        });

connect(&_showLabelsAction, &mv::gui::ToggleAction::toggled,
        this, [this](bool showLabels) {
            _renderer.setLabelsVisible(showLabels);
        });
```

Supplying the plugin as the receiver context makes Qt disconnect the lambda when the plugin is destroyed.

## Establish the initial state

A connection reacts to future changes; it does not normally initialize dependent state. Put the update in one callable, invoke it once, and reuse it from the signal:

```cpp
const auto updateRenderer = [this]() {
    _renderer.setPointSize(_pointSizeAction.getValue());
    _renderer.setLabelsVisible(_showLabelsAction.isChecked());
};

updateRenderer();

connect(&_pointSizeAction, &mv::gui::DecimalAction::valueChanged,
        this, updateRenderer);
connect(&_showLabelsAction, &mv::gui::ToggleAction::toggled,
        this, updateRenderer);
```

Restoring action state may emit value signals. Make handlers safe to run both during initialization and later interaction, and avoid assuming that every signal originated from a user gesture.

## Keep the action authoritative

Read current settings from actions when performing an operation. Avoid maintaining a second unsynchronized copy in the plugin. If external state changes the parameter, update the action and allow the normal signal path to update consumers.

For expensive work, debounce rapid value changes or use a trigger action to make application explicit. A slider can emit many intermediate values; starting a large computation for every one is rarely desirable.
