# Task

### Related
- Task {doc}`models <../models/tasks/index>`

## Types

The task classes below are derived from the {ref}`task <task>` base class.

```{toctree}
:maxdepth: 1

types/background_task
types/dataset_task
types/foreground_task
types/modal_task
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