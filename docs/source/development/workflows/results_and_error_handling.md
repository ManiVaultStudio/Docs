# Results and error handling

## Result hierarchy

`WorkflowResultBase` supplies common identity and status behavior. `WorkflowResult` represents the root outcome, while `WorkflowStageResult` and `WorkflowJobResult` represent lower-level outcomes. The root result also carries collected messages and metrics.

Always inspect status before consuming outputs whose production depends on successful completion. A completed future means execution ended; it does not imply success.

## Reporting a failure

Jobs can fail explicitly through the job/context facilities or by throwing. Prefer an explicit, actionable message when the failure is expected and can be explained. Exceptions remain appropriate for violated contracts or failures naturally expressed by a called API. The executor catches failures at the job boundary and incorporates them into workflow status and diagnostics.

Avoid using a fatal message as a substitute for control flow unless the associated job is also marked failed. Likewise, do not throw solely to report a warning.

## Structured messages

`WorkflowMessage` combines severity, text, location, and optional detail fields. Put the concise user-facing explanation in the text and machine- or developer-oriented evidence in details. This allows the result dialog, filters, and console formatter to present the same event appropriately.

## Futures

`WorkflowResultFuture` holds shared completion state and provides access to the final result. Use it to observe asynchronous execution without exposing executor internals. Arrange callbacks and captured state so they remain valid until completion.

## Result registry and dialog

`WorkflowResultRegistry` retains results that need to be opened from notifications. `WorkflowResultDialog` presents filtered messages and details. These are presentation facilities; core workflow correctness must not depend on a dialog being shown.
