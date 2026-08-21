# Workflow message

A structured diagnostic message associated with a workflow execution context. It carries severity, text, emitter and location information, optional details, a timestamp, and identifiers that preserve the reporting hierarchy.

Jobs normally create messages through their execution context rather than constructing presentation models. A completed workflow result owns the collected messages; the {doc}`workflow-message models <abstract_workflow_messages_model>` turn them into flat or hierarchical Qt model data.

Workflow messages should describe execution-specific milestones, warnings, and errors that belong with the result. Use the general {doc}`logging API <../../util/logging/index>` for process-wide developer evidence, and a user notification when the user needs a brief outcome independent of a result view.

```{doxygenenum} mv::workflow::MessageKind
```

```{doxygenstruct} mv::workflow::WorkflowMessage
:members:
```
