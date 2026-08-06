# Examples and recipes

The following patterns emphasize structure. Exact callable signatures are available in the {doc}`WorkflowPlan API reference <../../api/core/workflow/planning/workflow_plan>`.

## Pipeline with a parallel middle phase

Structure an import pipeline as three stages:

1. A sequential validation stage reads metadata and prepares shared context.
2. A parallel stage processes independent data blocks into disjoint output slots.
3. A sequential commit stage combines outputs and updates application state.

This makes the validation and commit operations explicit barriers around safe parallel work.

## GUI hand-off

Perform expensive preparation on worker threads, then add a short GUI-affine job that applies the prepared value to a widget or model. Never perform the expensive preparation inside the GUI job merely because the final consumer lives on that thread.

## Reusable child operation

Represent a reusable save, load, or archive operation as its own plan when it has several observable phases. Add it as a nested workflow job and choose nested progress if users benefit from seeing those phases.

## Failure cleanup

Put compensating behavior that is meaningful only after failure in a failure stage. Put resource release and temporary-file cleanup in finalization or, preferably, local RAII objects. Keep success-only publication in a success stage so partial outputs are not exposed after failure.

## Large homogeneous collections

Generate one job per item, then use a batched parallel stage. Select the batch size from memory use and external resource limits. Check cancellation between items and publish aggregate metrics such as processed count and bytes only after each item commits successfully.
