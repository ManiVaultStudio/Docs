# Workflow utilities

The workflow directory contains supporting types that keep planning and job code focused on domain work.

## Configuration value types

`WorkflowOptions` collects cancellation, parallelization, profiling, and reporting policies. `WorkflowBatchingOptions` supplies conservative batch calculations. `WorkflowResultDetailsOptions` supplies presentation text and result-dialog detail behavior.

Prefer passing an options object at the execution boundary. Avoid reading global configuration from individual jobs because it makes plans harder to test and reuse.

## RAII scopes

`WorkflowExecutionLifecycleScope` reports lifecycle completion on scope exit, and `WorkflowConsoleDashboardScope` starts and stops console observation. These utilities make early returns and exceptions less likely to leave reporting state incomplete.

## Nested runtime access

`WorkflowRuntimeScoped` is the access point for synchronously executing a plan beneath an existing parent context. It preserves the active workflow hierarchy while keeping callers independent of the concrete executor.

## Identity and type conversion

`WorkflowHandle` provides stable entity identity. `WorkflowExecutionNodeType` describes the kind of node, with conversion helpers for display and serialization. Use handles for identity and names for presentation.

## Formatting and presentation

`WorkflowConsoleFormatter`, `WorkflowConsoleDashboard`, `WorkflowResultDialog`, and `WorkflowMessageDetailsDelegate` present existing workflow state. They should not own operation logic.

## Registry and dispatch

`WorkflowResultRegistry` makes completed results addressable from UI notifications. `WorkflowGuiThreadDispatcher` centralizes execution of GUI-affine jobs. Callers normally use both indirectly through the executor.

## Context utility

`WorkflowContextVariantMap` is a general-purpose payload with synchronized access to named values. Prefer a domain-specific `WorkflowContextBase` subclass when field names and types are known at compile time.

See the {doc}`workflow API reference <../../api/core/workflow/index>` for the complete type list and member documentation.
