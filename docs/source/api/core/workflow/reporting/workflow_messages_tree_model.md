# WorkflowMessagesTreeModel

**Qualified name:** `mv::WorkflowMessagesTreeModel`

`WorkflowMessagesTreeModel` organizes the messages collected by a workflow result according to their context identifiers. When a message's parent-context ID matches an existing message ID, its row is attached beneath that parent; otherwise it remains at the root.

This is the source model used by {doc}`WorkflowResultDialog <workflow_result_dialog>` because it preserves the relationship between parent and nested workflow reporting. Use {doc}`WorkflowMessagesListModel <workflow_messages_list_model>` when a flat view is more appropriate.

```{doxygenclass} mv::WorkflowMessagesTreeModel
:members:
:protected-members:
```
