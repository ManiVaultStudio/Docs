# Nested workflows

Nested workflows let a job expand into another plan while preserving one execution hierarchy. They are useful when a reusable operation already has meaningful stages, progress, diagnostics, and cleanup of its own.

## Execution under a parent

A child plan runs with a parent `WorkflowExecutionContext`. It shares cancellation and root execution state while creating child report and progress nodes. Messages and metrics can therefore be collected with the root result without losing their nested location.

## Progress modes

Nested progress can be represented in two ways:

- **atomic** treats the child as a single weighted unit at the parent level;
- **nested** exposes the child's fine-grained progress beneath the parent job.

Use atomic progress when internal detail is distracting or unstable. Use nested progress when the child is long-running and its phases are meaningful to users.

## Error and cancellation propagation

A failed nested workflow fails its owning job unless the surrounding plan explicitly handles that outcome. Cancellation should be checked within the child just as in a root workflow; both observe the shared cancellation state.

## Avoid unnecessary nesting

Do not create a nested plan merely to call a helper function. Nesting is valuable when the child needs its own scheduling, progress hierarchy, lifecycle stages, or reusable result contract. Plain functions keep simple code easier to follow.
