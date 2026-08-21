# AbstractWorkflowMessagesModel

**Qualified name:** `mv::AbstractWorkflowMessagesModel`

`AbstractWorkflowMessagesModel` defines the common columns and item behavior used to present {doc}`WorkflowMessage <workflow_message>` instances. Its columns expose severity, text, emitter, location, details, timestamp, message ID, and parent-context ID.

Each row creates a shared copy of its workflow message, and every item in that row refers to the same copy. The specialized {doc}`list <workflow_messages_list_model>` and {doc}`tree <workflow_messages_tree_model>` models decide how rows are organized.

```{doxygenclass} mv::AbstractWorkflowMessagesModel
:members:
:protected-members:
```
