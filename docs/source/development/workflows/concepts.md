# Core concepts

## Plan, stage, and job

A **plan** is the complete declarative description of a workflow. Its main stages execute in insertion order. Each stage contains one or more **jobs** and declares whether those jobs are sequential or parallel. A job is the smallest scheduled unit and carries its own identity, thread affinity, progress behavior, and relative weight.

Plans can also contain conditional lifecycle stages:

- success stages run after successful main-stage execution;
- failure stages run after a main-stage failure;
- finalization stages provide unconditional cleanup.

## Handles and identities

Plans, stages, and jobs use `WorkflowHandle` values to identify execution entities. Handles make it possible to associate planning-time entities with progress, reports, and outputs without relying on display names.

## Execution context

Every executing node receives a `WorkflowExecutionContext`. Contexts form a hierarchy matching the running plan. They provide access to the shared `WorkflowExecutionState` while retaining node-local report and progress positions. A separate `WorkflowContextBase` payload carries operation-specific data; `WorkflowContextVariantMap` is available when a typed context class would be excessive.

## Progress and reports

Progress and reporting are distinct trees:

- `WorkflowProgressNode` models completion state and weighted aggregation;
- `WorkflowReportNode` records lifecycle and diagnostic messages.

Keeping them separate lets a workflow report multiple messages without changing completion and lets progress update without producing log noise.

## State and result

`WorkflowExecutionState` is shared by all contexts in one root execution. It owns the root progress/report nodes, options, aggregate metrics, status, published values, and cancellation state. At completion, the executor snapshots the relevant information into `WorkflowResult`, with stage and job outcomes represented by `WorkflowStageResult` and `WorkflowJobResult` where needed.

## Root and child workflows

A root workflow establishes new execution state and may integrate with a ManiVault `Task`. A nested workflow executes under an existing context and contributes to the parent's hierarchy. This distinction affects option inheritance, progress composition, and result ownership.
