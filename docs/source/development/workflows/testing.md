# Testing workflows

Test the plan's observable contract rather than the concrete scheduler's internal task graph.

## Core cases

For each non-trivial workflow, cover:

- successful execution and expected outputs;
- a representative job failure and later-stage policy;
- cancellation before execution and during a long job;
- success, failure, and finalization branch behavior;
- progress reaching a terminal state without exceeding its bounds;
- warnings and errors appearing with the expected severity and location;
- nested result and progress propagation;
- GUI-affine work executing on the correct thread.

## Determinism

Parallel tests must not depend on job completion order. Use synchronization primitives or test hooks to reach a required state instead of sleeping for an assumed duration. Validate sets or keyed outputs when ordering is not part of the contract.

## Small plans

Prefer small purpose-built plans in unit tests. A single-stage plan can isolate progress or failure behavior; a two-stage plan can verify barriers. Reserve full application workflows for integration tests.

## Context and lifetime checks

Test that context values remain valid through asynchronous completion and that cancelled or failed paths release retained objects. Where callbacks use weak ownership, include a case in which the observed object disappears before completion.

## Headless diagnostics

The console formatter and progress snapshots are useful for asserting or logging execution state in tests without opening GUI dialogs. Avoid making tests depend on decorative formatting unless formatting itself is under test.
