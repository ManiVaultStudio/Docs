# MessageCardAction

`mv::gui::MessageCardAction` is a `WidgetAction` that presents an inline, severity-coded message with a category, description, and optional buttons. The action keeps its message state independently of generated widgets, so widgets created later show the current message and existing widgets update when `setMessage()` is called.

Construct the action with an optional owning `QObject` parent, then set its message:

```cpp
mv::gui::MessageCardAction messageAction(this);
messageAction.setMessage(
    mv::util::SeverityLevel::Warning,
    "Input unavailable",
    "Select a points dataset to continue.");
```

The optional `ButtonActions` argument is an ordered list of button labels and callbacks. Callbacks are retained until the message is replaced or the action is destroyed; they must not throw and must not capture objects that may be destroyed first. The parent owns the action when provided; otherwise, the creator is responsible for its lifetime.

**Qualified name:** `mv::gui::MessageCardAction`

See the [implementation header](https://github.com/ManiVaultStudio/core/blob/master/src/lib/actions/MessageCardAction.h) for the complete declaration and callback contract.
