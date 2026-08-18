# Task

Tasks report the progress and state of long-running operations to the user. They do not schedule or execute those operations. For substantial new work, prefer the workflow-backed execution facilities and use a task as their GUI progress projection; manage a task directly when execution is owned elsewhere.

In the current design, tasks focus on progress reporting rather than execution itself. Future versions will extend this concept to optionally manage and run worker logic directly, allowing tasks to encapsulate both execution and reporting.

Tasks are closely integrated with the task models, which manage their lifecycle and visibility within the application.

For guidance on choosing between high-level parallel execution, custom workflows, and direct task management, see {doc}`Long-running operations and task progress <../../../development/building_plugins/tasks/index>`.

## Related

- Task {doc}`models <../models/tasks/index>`

## Base type

```{toctree}
:maxdepth: 1

task
```

## Types

The task classes below are derived from the {doc}`task <task>` base class.

```{toctree}
:maxdepth: 1

types/background_task
types/dataset_task
types/foreground_task
types/modal_task
types/application_startup_task
```

## Handlers

Task handlers are responsible for presenting task-related information to the user. For example, they may display progress using a modal dialog, a progress bar in the status bar, or similar UI elements.

```{toctree}
:maxdepth: 1

handlers/abstract_task_handler
handlers/background_task_handler
handlers/dataset_task_handler
handlers/foreground_task_handler
handlers/modal_task_handler
```

## Testing

Below are some auxilliary classes for testing various task types
```{toctree}
:maxdepth: 1

testing/abstract_task_tester
testing/background_task_tester
testing/foreground_task_tester
testing/modal_task_tester
testing/task_tester_runner
```
