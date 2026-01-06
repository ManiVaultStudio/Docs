# Adding Actions

Actions can be integrated into the GUI in two primary ways:

1. By creating an action widget directly and adding it to a layout.
2. By adding an action to a container (group) action and embedding the group in the layout.

---

## Creating an Action Widget

In the simplest case, an action is instantiated and its widget representation is added directly to a layout.

```cpp
// Create a decimal action
auto decimalAction = new DecimalAction(this, "Decimal action");

// Create the widget for the action and add it to the layout
layout->addWidget(decimalAction->createWidget(this));
```

*This example shows how to create a single decimal action and add its widget directly to the GUI.*

---

## Adding an Action to a Container Action

Actions can also be grouped using a container action, such as a horizontal group. This is useful when multiple related actions should be presented together.

```cpp
// Create a container (group) action
auto decimalActions = new HorizontalGroupAction(this, "Decimal actions");

// Create individual decimal actions
auto decimalActionA = new DecimalAction(this, "Decimal action A");
auto decimalActionB = new DecimalAction(this, "Decimal action B");

// Add actions to the group
decimalActions->addAction(decimalActionA);
decimalActions->addAction(
    decimalActionB,
    DecimalAction::WidgetFlag::LineEdit // Override widget flags
);

// Create the group widget and add it to the layout
layout->addWidget(decimalActions->createWidget(this));
```

*This example demonstrates how multiple decimal actions can be grouped and added to the GUI via a container action.*
