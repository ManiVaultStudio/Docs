# WorkflowMessagesFilterModel

**Qualified name:** `mv::WorkflowMessagesFilterModel`

`WorkflowMessagesFilterModel` is the sorting and filtering proxy for an {doc}`AbstractWorkflowMessagesModel <abstract_workflow_messages_model>`. Its `OptionsAction` selects the visible severity levels, while the inherited regular-expression filter can constrain the configured filter column.

Sorting respects the structured values of severity, emitter, location, text, timestamp, and details instead of relying solely on their display strings. `WorkflowResultDialog` places this proxy in front of a {doc}`WorkflowMessagesTreeModel <workflow_messages_tree_model>`.

```{doxygenclass} mv::WorkflowMessagesFilterModel
:members:
:protected-members:
```
