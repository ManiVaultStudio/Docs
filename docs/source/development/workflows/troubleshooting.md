# Troubleshooting

## The workflow never completes

Check for a GUI-thread deadlock, a job waiting on another job in the same sequential stage, or manual completion that was never signalled. Also verify that an asynchronous callback retains the state it needs to publish completion.

## Progress stalls below completion

Look for a manual or nested-progress job that did not reach a terminal state, a child node added after weights were established, or a cancelled node that was not marked skipped. Inspect a `WorkflowProgressNode` snapshot with `WorkflowConsoleFormatter`.

## Cancellation appears ineffective

Cancellation cannot interrupt arbitrary blocking code. Add checks between bounded units, use cancellable APIs where available, and reduce the maximum duration of one unit. Confirm the child workflow shares the intended root execution state.

## A later stage sees missing output

Confirm the producer and consumer are separated by a stage barrier or otherwise have an explicit dependency. Check that the producer publishes under the same identifier and type the consumer expects, and do not consume success-dependent output after a failed result.

## Intermittent failures in parallel stages

Treat these as shared-state or lifetime bugs until proven otherwise. Check captures by reference, container mutation, Qt object affinity, non-thread-safe context members, and external libraries with hidden global state.

## Messages appear but the workflow succeeds

A diagnostic severity and execution status are related but separate. Ensure the failing job explicitly reports failure or throws; logging an error-shaped message alone may not apply failure control flow.

## Result details cannot be opened

If a notification links to a completed result, verify that `WorkflowResultRegistry` retains it for the required lifetime and that result-link handling is installed. The workflow result itself should remain usable even when presentation is unavailable.
