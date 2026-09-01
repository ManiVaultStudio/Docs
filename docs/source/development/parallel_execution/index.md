# Parallel execution

Parallel execution is an optional API for scheduling work and running independent operations concurrently. You do not have to use it to build a ManiVault plugin or application. Ordinary synchronous functions, standard action serialization, and other existing Core APIs continue to work without calling `mv::Parallel` or defining a custom workflow.

Use these pages when an operation is substantial enough that moving work to worker threads, processing independent items concurrently, reporting progress, supporting cancellation, or preserving a structured result would improve the implementation or user experience.

## Choose by goal

- **Save and restore a few action values:** use {doc}`Saving and restoring action state <../building_plugins/actions/serialization>`. No parallel API is needed.
- **Optimize expensive, staged, or parallelizable plugin serialization:** start with {doc}`Synchronous and workflow serialization <../building_plugins/persistence/synchronous_and_workflow>`.
- **Schedule one coarse operation and inspect its result while the caller can wait:** use {doc}`Running an operation <running_operations>`.
- **Apply independent work to files, datasets, images, or blocks:** use {doc}`Processing collections <processing_collections>`.
- **Transform a collection and return results in input order:** use {doc}`Mapping collections <mapping_collections>`.
- **Combine preparation, parallel processing, and finalization phases:** use {doc}`Building execution chains <execution_chains>`.
- **Run a long operation on workers with interactive progress and cancellation:** start with the {doc}`Advanced workflow framework <../workflows/index>`, then continue with {doc}`Progress and cancellation <../workflows/progress_and_cancellation>`.
- **Show progress for work already scheduled by another library or service:** see {doc}`Choosing an execution model <../building_plugins/tasks/choosing_an_execution_model>`.
- **Speed up a tight numerical loop or internally threaded kernel:** read {doc}`Intended scope and granularity <scope_and_granularity>` before choosing a facility.

## Choose the smallest suitable level

- **Direct synchronous code:** use it when the work is short, bounded, and does not need execution progress or cancellation.
- **High-level `mv::Parallel` utilities:** use them when the caller may wait and the work fits one operation, a collection, a mapping, or a straightforward sequence of stages.
- **Advanced workflow framework:** use it when the operation needs asynchronous lifetime, task-backed progress, cancellation, GUI-thread phases, nesting, custom weights, or detailed reporting.

`mv::Parallel` is the concise entry point when the middle level fits. It builds on the workflow engine without requiring developers to construct workflow plans themselves. Its terminal calls are blocking: the work can run on workflow workers, but the call returns only after the operation finishes. Do not use a blocking helper from a context that must remain responsive.

## Start using the high-level API

Begin with {doc}`Getting started <getting_started>`, then continue with the guide matching the shape of the operation.

```{toctree}
:maxdepth: 1

getting_started
running_operations
processing_collections
mapping_collections
execution_chains
examples
```

## Advanced decisions and controls

The following pages explain configuration, safety, granularity, and the point at which a custom workflow becomes appropriate. They are important when the basic utilities fit only partially, but they are not prerequisites for understanding what the API is for.

```{toctree}
:maxdepth: 1

options_and_cancellation
thread_safety
scope_and_granularity
../workflows/index
```

## API reference

For exact signatures, see the {doc}`parallel API reference <../../api/core/parallel/index>`. The underlying types are documented in the {doc}`workflow API reference <../../api/core/workflow/index>`.
