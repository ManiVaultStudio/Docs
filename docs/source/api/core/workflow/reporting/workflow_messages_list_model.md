# WorkflowMessagesListModel

**Qualified name:** `mv::WorkflowMessagesListModel`

`WorkflowMessagesListModel` presents all messages collected by a workflow result as a flat sequence. Use it when chronological or sortable inspection matters more than execution-context nesting.

Call `setWorkflowResult()` with the completed or otherwise inspectable result whose messages should populate the model. For a context hierarchy, use {doc}`WorkflowMessagesTreeModel <workflow_messages_tree_model>` instead.

```{doxygenclass} mv::WorkflowMessagesListModel
:members:
:protected-members:
```
