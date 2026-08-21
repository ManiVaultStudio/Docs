# Workflow result dialog

A dialog for inspecting the summary and structured messages collected by a workflow result. It presents a {doc}`WorkflowMessagesTreeModel <workflow_messages_tree_model>` through a {doc}`WorkflowMessagesFilterModel <workflow_messages_filter_model>`, allowing the user to preserve context hierarchy, sort columns, and choose visible severity levels.

The diagnostics area initially expands when the result contains warnings or errors. Result-detail options supply the surrounding title and message; the dialog does not create or own workflow execution.

```{doxygenclass} mv::workflow::WorkflowResultDialog
:members:
```
