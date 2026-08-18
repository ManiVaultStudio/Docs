# Failures in callbacks, tasks, and workflows

Asynchronous boundaries need an explicit owner for failures. An exception that escapes a Qt callback, detached worker, or unobserved future may not reach the initiating UI in a useful form.

## Qt callbacks

Catch failures at the callback boundary when no framework executor owns it. Add operation context and route the error once to the appropriate UI or result mechanism:

```cpp
connect(&_importAction, &QAction::triggered, this, [this]() {
    try {
        importSelectedFile();
    }
    catch (const std::exception& exception) {
        mv::util::exceptionMessageBox(
            tr("Unable to import the selected file"), exception, &getWidget());
    }
});
```

## Tasks and workflows

Prefer a workflow for substantial new asynchronous operations so progress, failure, results, and completion share one owner. A task by itself reports state but does not catch exceptions or preserve a structured outcome.

Workflow jobs may throw; the executor catches failures at the job boundary and records them in the result. Expected warnings and errors can be reported with `context->warning(...)` and `context->error(...)`, including location and detail fields.

An error message alone does not necessarily stop execution. Call `markFailed()` or use the job failure mechanism when the job must fail. Conversely, do not throw merely to report a warning.

Inspect the final workflow result status before consuming dependent output. Completion means execution ended, not that it succeeded. See {doc}`Tasks and workflows <../tasks/tasks_and_workflows>` and {doc}`Workflow results and error handling <../../workflows/results_and_error_handling>`.

Avoid adding a second notification or dialog if the workflow notifier already presents the result. Let one result own progress, cancellation, messages, and final presentation.
