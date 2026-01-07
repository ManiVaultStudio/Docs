# Customizing actions

When an action creates its GUI representation, **widget flags** determine which UI elements are shown and how they are arranged. These flags allow application and plugin developers to adapt the look and behavior of actions to different contexts.

There are three supported ways to customize widget flags, plus an advanced option for post-processing the created widget.

---

## 1. Default widget flags

Default widget flags define the *standard* appearance of an action whenever its widget is created without additional overrides.

For example, the default widget flags of `mv::gui::DecimalAction` (derived from `mv::gui::NumericalAction`) produce a widget that includes both a spin box and a slider.

### Examples

**Default widget flags**

![Decimal action with default widget flags](../../assets/decimal_action_default_widget_flags.png)

*The default widget flags (`DecimalAction::WidgetFlag::Default`) show both a spin box and a slider.*

**Spin box only**

![Decimal action with spinbox widget flag only](../../assets/decimal_action_spinbox.png)

*Using only `DecimalAction::WidgetFlag::SpinBox`.*

**Slider only**

![Decimal action with slider widget flag only](../../assets/decimal_action_slider.png)

*Using only `DecimalAction::WidgetFlag::Slider`.*

### Example: customizing default widget flags

```cpp
// Create the decimal actions
auto decimalActionDefault = new DecimalAction(this, "Decimal action (default flags)");
auto decimalActionSpinbox = new DecimalAction(this, "Decimal action (spinbox only)");
auto decimalActionSlider  = new DecimalAction(this, "Decimal action (slider only)");

// Override default widget flags
decimalActionSpinbox->setDefaultWidgetFlags(DecimalAction::WidgetFlag::SpinBox);
decimalActionSlider->setDefaultWidgetFlags(DecimalAction::WidgetFlag::Slider);

// Add the action widgets to the layout
layout->addWidget(decimalActionDefault->createWidget(this));
layout->addWidget(decimalActionSpinbox->createWidget(this));
layout->addWidget(decimalActionSlider->createWidget(this));
```

---

## 2. Overriding widget flags at widget creation time

Widget flags can also be specified **when creating the widget itself**. This allows the same action instance to appear differently in multiple places.

```cpp
// Create a single decimal action
auto decimalAction = new DecimalAction(this, "Decimal action");

// Add decimal action widget with spin box and slider
layout->addWidget(decimalAction->createWidget(
    this,
    DecimalAction::WidgetFlag::Default
));

// Add decimal action widget with spin box only
layout->addWidget(decimalAction->createWidget(
    this,
    DecimalAction::WidgetFlag::SpinBox
));

// Add decimal action widget with slider only
layout->addWidget(decimalAction->createWidget(
    this,
    DecimalAction::WidgetFlag::Slider
));
```

This approach does **not** modify the action’s default flags; it only affects the specific widget instance being created.

---

## 3. Overriding widget flags in group-based actions

When an action is added to a group-based action (for example, a `GroupAction` or `HorizontalGroupAction`), widget flags can be specified per action entry. These flags override the action’s default widget flags within the group.

```cpp
// Create the group and decimal actions
auto decimalActions = new HorizontalGroupAction(this, "Decimal actions");
auto decimalActionA = new DecimalAction(this, "Decimal action A");
auto decimalActionB = new DecimalAction(this, "Decimal action B");

// Add decimal actions to the group
decimalActions->addAction(decimalActionA);
decimalActions->addAction(
    decimalActionB,
    DecimalAction::WidgetFlag::LineEdit // Override widget flags
);

// Add the group action widget to the layout
layout->addWidget(decimalActions->createWidget(this));
```

This is useful when related actions should share a container but require different visual representations.

---

## Advanced: widget post-processing

If widget flags are not sufficient, the created widget can be customized **after creation** using a widget configuration function.

This is done via `WidgetAction::WidgetConfigurationFunction`, which is invoked immediately after the widget is constructed.

```cpp
// Create the decimal action
auto decimalAction = new DecimalAction(this, "My decimal");

// Define a widget configuration function
auto widgetEdit = [this](WidgetAction* action, QWidget* widget) -> void {
    auto spinBoxWidget = widget->findChild<QSpinBox*>("SpinBox");

    Q_ASSERT(spinBoxWidget);
    if (!spinBoxWidget)
        return;

    // Apply custom widget changes
    spinBoxWidget->setStyleSheet("color: red;");
};

// Create the widget with post-processing
decimalAction->createWidget(this, widgetEdit);
```

This mechanism allows fine-grained customization of the underlying Qt widgets when necessary, while still using the standard action infrastructure.
