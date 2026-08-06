# Execution context and shared state

`WorkflowExecutionContext` is the runtime interface passed to workflow jobs. It binds the current plan, stage, or job to its node-local progress and report nodes and to the shared root `WorkflowExecutionState`.

## Operation data

Derive a context payload from `WorkflowContextBase` when the operation has a stable domain model. A typed context makes ownership, synchronization, and required inputs explicit. Use `WorkflowContextVariantMap` for small or extensible key-value payloads, particularly where values must be published or retrieved by identifier.

The context payload and execution context serve different purposes:

- the payload contains operation-specific inputs and intermediate data;
- the execution context contains framework runtime facilities.

## Hierarchy

Child contexts share root state but have their own handles and report/progress positions. This enables recursive collection while retaining the exact source of a message or progress update.

## Outputs

Jobs can publish values through execution state using stable output identifiers. Treat published values as a hand-off contract: document the expected type and ensure a consumer cannot run before its producer. Prefer direct typed context members for tightly coupled stages and published values for loosely coupled or dynamically addressed results.

## Thread safety

Shared execution state protects its framework-owned aggregates, but that does not automatically make user payloads thread-safe. If parallel jobs access a custom context, the context implementation must provide synchronization or divide data so each job owns a disjoint part.

## Lifetime

Contexts are shared pointers because nested and asynchronous work can retain them. Avoid cycles from context-owned callbacks that capture the same context strongly. Use weak pointers when a callback should not extend the execution lifetime.
