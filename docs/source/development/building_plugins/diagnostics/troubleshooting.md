# Diagnostic checklist

When a failure is difficult to diagnose, verify the following in order:

1. Identify the operation boundary and whether it completed, failed, or was cancelled.
2. Record stable plugin, dataset, action, workflow, or diagnostic IDs.
3. Preserve the original exception cause before adding higher-level context.
4. Check object and dataset validity at the time the callback actually ran.
5. Confirm the code ran on the required thread.
6. Inspect workflow status and structured messages, not only future completion.
7. Reproduce with non-default state and after a save/reload round trip when persistence is involved.
8. Ensure the failure was presented once and was not swallowed by an empty catch block.

## Common anti-patterns

- Catching `...` and continuing with partially initialized state.
- Showing a notification but forgetting to return or mark the operation failed.
- Displaying modal dialogs inside reusable utilities or worker jobs.
- Logging only “failed” without the operation, object identity, and cause.
- Logging sensitive or extremely large values.
- Treating cancellation as an error.
- Emitting an error workflow message while allowing dependent jobs to consume missing output.
- Retaining raw object pointers in queued diagnostic callbacks.

Tests should assert both behavior and reporting: the operation fails or falls back as intended, the result status is correct, and the diagnostic contains enough context to act on without creating duplicate UI messages.
