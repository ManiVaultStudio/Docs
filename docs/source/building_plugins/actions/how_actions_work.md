# How actions work

Each action object holds a piece of state (a value or trigger) and automatically generates the appropriate GUI controls to manipulate that state. For example, a **StringAction** stores a text string and creates a labeled text box widget for users to view or edit that string [1](https://ieeexplore.ieee.org/document/10290921). A **DecimalAction** holds a numeric value and might create a slider + textbox combo to adjust that number. Developers do not directly create Qt widgets for plugin settings; instead, they instantiate actions (like new `StringAction(this, "Label", defaultValue)`) and **ManiVault** takes care of rendering the GUI elements and keeping them in sync with the underlying value
[2](https://www.manivault.studio/apireference/classhdps_1_1gui_1_1_string_action.html#a881b46415ef708147f61e48cba775224acc8fbdf588f8cda64966ea5a6053fe5f#:~:text=Q_INVOKABLE%C2%A0StringAction%20%28QObject%20,title%2C%20const%20QString%20%26string). This abstraction makes actions building blocks that can be added to a plugin’s interface with minimal effort while ensuring consistency across the whole application.

## Key characteristics

Actions aren’t just static UI controls – they carry metadata and integration hooks:

Each action has a title (used as its label in the UI) and an internal ID. The title is displayed next to the widget (and is interactive for linking/sharing as discussed later).

Actions know whether they are public or private in scope. A public action’s value can be shared with other plugins, whereas a private action is local to the plugin. By default, most plugin settings actions are private until the user or developer marks them public.

Actions emit signals when their value changes or when other state toggles happen (enabled/disabled, visibility changes, etc.), allowing the plugin logic to react to user input without manual GUI wiring.

All actions are part of a hierarchy within a plugin (often reflecting grouping in the UI). ManiVault’s core can traverse this hierarchy for tasks like saving state or building dynamic dialogs.