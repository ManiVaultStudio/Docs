# Examples and recipes

This page is a task-oriented index rather than a second API reference. Start with the smallest recipe that satisfies the operation. The first five recipes use the concise, blocking `mv::Parallel` interface. The remaining recipes use a workflow plan or a directly managed task because they need asynchronous lifetime, GUI integration, or execution control.

The snippets focus on the choice of execution mechanism. Production code must still define ownership, handle `WorkflowResult`, and keep shared state safe. See {doc}`Thread safety and data access <thread_safety>` for the concurrency rules.

## High-level blocking recipes

(recipe-run-one-operation)=
### Run one substantial operation on a worker and wait for its result

Use `Parallel::run()` for one coarse operation when the caller may wait until it finishes:

```cpp
const auto result = mv::Parallel::run("Build search index", [] {
    buildSearchIndex();
});
```

The work is scheduled through the workflow executor, but `run()` does not return until execution completes. Do not call it from a path that must keep the GUI responsive. Continue with {doc}`Running an operation <running_operations>`.

(recipe-process-items)=
### Process independent items concurrently

Use `Parallel::forEach()` when every item can be processed independently:

```cpp
const auto result = mv::Parallel::forEach(
    "Generate previews",
    images,
    [](Image& image) {
        generatePreview(image);
    });
```

The range is owned for the duration of execution. The callback must not concurrently mutate shared container state. Continue with {doc}`Processing collections <processing_collections>`.

(recipe-map-results)=
### Transform a collection and preserve input order

Use `Parallel::map()` when every input produces one output:

```cpp
const auto labels = mv::Parallel::map(
    "Format labels",
    values,
    [](const auto& value) {
        return formatLabel(value);
    });
```

The returned values follow input order even though individual transformations may finish out of order. Continue with {doc}`Mapping collections <mapping_collections>`.

(recipe-stage-pipeline)=
### Combine preparation, parallel work, and finalization

Use `ParallelExecutionChain` for a straightforward series of sequential and parallel phases:

```cpp
const auto result = mv::Parallel::stages("Rebuild cache")
    .run("Prepare cache", prepareCache)
    .forEach("Build cache entries", records, buildCacheEntry)
    .run("Commit cache", commitCache)
    .execute(options);
```

Each stage is a barrier: all cache entries finish before `commitCache()` starts. Continue with {doc}`Building execution chains <execution_chains>`.

(recipe-limit-workers)=
### Limit concurrency or force serial execution

Pass `WorkflowOptions` to the terminal operation when the workload or a dependency requires less concurrency:

```cpp
mv::workflow::WorkflowOptions options;
options.execution.maxWorkerThreadCount = 4;

const auto result = mv::Parallel::forEach(
    "Read sources", sources, readSource, options);
```

Set `options.execution.parallel = false` to keep the workflow structure and reporting while executing the parallel stages serially. See {doc}`Options and cancellation <options_and_cancellation>` for the full option groups.

## Interactive workflow recipes

(recipe-live-progress)=
### Keep the interface responsive and show live progress

Use asynchronous workflow execution when the GUI must remain responsive. Enabling progress reporting lets the executor associate a ManiVault task with the workflow:

```cpp
mv::workflow::WorkflowOptions options;
options.reporting.progress = true;

_workflowFuture = mv::Application::getWorkflowPlanExecutor().execute(
    std::move(plan), nullptr, options);

_workflowFuture.onFinished(this, [this](const auto& result) {
    handleResult(result);
});
```

Store the `WorkflowResultFuture` for the entire operation rather than creating an untracked temporary. The callback runs after completion; it is not necessary to call `get()` on the GUI thread. See {doc}`Results and error handling <../workflows/results_and_error_handling>` and {doc}`Tasks and workflows <../building_plugins/tasks/tasks_and_workflows>`.

(recipe-cancellation)=
### Make a long-running operation cancellable

Cancellation is an execution policy plus a cooperative implementation. Enable it for an asynchronous, task-backed workflow and check the associated task between meaningful units of work:

```cpp
mv::workflow::WorkflowOptions options;
options.reporting.progress   = true;
options.cancellation.enabled = true;

plan->addSequentialStage("Process records", [](const auto&, const auto& context) {
    for (const auto& record : records()) {
        const auto task = context->getTask();

        if (task && (task->isAboutToBeAborted() ||
                     task->isAborting() || task->isAborted())) {
            throw std::runtime_error("Processing was canceled");
        }

        process(record);
    }
});
```

Execute the plan asynchronously as in the preceding recipe. A request cannot forcibly stop arbitrary C++ code; the operation must stop at safe boundaries and leave resources valid. Handle the resulting exception or failed result at the owning boundary. See {doc}`Progress and cancellation <../workflows/progress_and_cancellation>` for cleanup and skipped-work guidance.

(recipe-report-progress)=
### Report intermediate progress and diagnostics

For a long job, use its execution context to report bounded progress and messages:

```cpp
plan->addSequentialStage("Import records", [](const auto&, const auto& context) {
    const auto input = loadInput();

    for (std::size_t index = 0; index < input.size(); ++index) {
        importRecord(input[index]);
        context->setProgress(
            static_cast<double>(index + 1) / input.size());
    }

    context->info("Imported all records");
});
```

Report through the context rather than writing directly to the root task. That preserves the workflow's progress tree and diagnostics. See {doc}`Execution context <../workflows/execution_context>` and {doc}`Reporting and profiling <../workflows/reporting_and_profiling>`.

(recipe-gui-commit)=
### Prepare on workers and commit on the GUI thread

Keep expensive preparation on a worker, then use explicit GUI-thread affinity only for the phase that touches Qt GUI state:

```cpp
auto prepared = std::make_shared<PreparedState>();

plan->addSequentialStage("Prepare", [prepared] {
    *prepared = prepareState();
});

plan->addSequentialStage(
    "Update interface",
    [this, prepared] {
        applyToWidgets(*prepared);
    },
    mv::workflow::WorkflowPlan::JobThreadAffinity::GuiThread);
```

The stage boundary makes the prepared state complete before the GUI commit begins. Keep GUI-thread stages short. See {doc}`Threading and parallelism <../workflows/threading_and_parallelism>`.

(recipe-batched-work)=
### Process a very large collection in bounded batches

Use a workflow plan when a very large job set should be submitted in controlled batches:

```cpp
mv::workflow::WorkflowPlan::Jobs jobs;
jobs.reserve(blocks.size());

for (const auto& block : blocks) {
    jobs.emplace_back("Process block", [block] {
        processBlock(block);
    });
}

plan->addBatchedParallelStage(
    "Process blocks", std::move(jobs), 16);
```

Batching controls scheduling granularity; it is not a substitute for limiting the executor's worker count. See {doc}`Defining workflows <../workflows/defining_workflows>`.

(recipe-workflow-serialization)=
### Parallelize expensive or staged serialization

Ordinary action and object state should remain synchronous. Override the workflow serialization methods only when persistence is expensive, staged, parallelizable, or needs explicit thread affinity:

```cpp
mv::workflow::UniqueWorkflowPlan ExamplePlugin::toVariantMapWorkflow() const
{
    auto plan = std::make_unique<mv::workflow::WorkflowPlan>("Save example");

    plan->addSequentialStage(
        "Collect settings",
        [this](const auto&, const auto& context) {
            context->setOutput(toVariantMap());
        },
        mv::workflow::WorkflowPlan::JobThreadAffinity::GuiThread);

    return plan;
}
```

These methods construct plans; project orchestration executes them. Use nested workflows and parallel stages inside the plan when the serialized components justify it. See {doc}`Synchronous and workflow serialization <../building_plugins/persistence/synchronous_and_workflow>`.

## Work owned by another executor

(recipe-external-task)=
### Show progress for work scheduled by another executor

When a library, service, process wrapper, or established worker already owns execution, attach a long-lived task rather than duplicating scheduling with a workflow:

```cpp
_task = new mv::BackgroundTask(this, "Download data");
_task->setRunning();

downloader.onProgress([this](float progress) {
    _task->setProgress(progress);
});

downloader.onFinished([this] {
    _task->setFinished();
});
```

Treat the callback names as placeholders for the external executor's API. Marshal task updates to the task's thread when callbacks arrive elsewhere, keep the task alive until completion, and preserve failures separately because task status is only a progress presentation. See {doc}`Choosing an execution model <../building_plugins/tasks/choosing_an_execution_model>` and {doc}`Threading and integration <../building_plugins/tasks/threading_and_integration>`.

## When none of these recipes fits

Use the {doc}`advanced workflow framework <../workflows/index>` for conditional success, failure, and finalization stages; nested workflows; custom weights; explicit outputs and metrics; or other execution graphs that do not fit the high-level utilities. If the operation is a tight numerical loop or already parallelizes internally, the workflow engine can orchestrate it as one coarse job while OpenMP, oneTBB, a GPU API, or the library's own implementation performs the fine-grained work. See {doc}`Intended scope and granularity <scope_and_granularity>`.
