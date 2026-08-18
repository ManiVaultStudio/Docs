# Task hierarchies

A parent task can summarize several child operations. Calling `child.setParentTask(&parent)` registers the relationship and changes the parent to `Aggregate` progress mode. The parent's progress is the weighted average of its enabled children.

```cpp
mv::ForegroundTask overall{this, "Preparing visualization"};
mv::Task load{this, "Loading", {mv::Task::GuiScope::None}};
mv::Task compute{this, "Computing", {mv::Task::GuiScope::None}};

load.setWeight(1.0f);
compute.setWeight(4.0f);

load.setParentTask(&overall);
compute.setParentTask(&overall);
```

Here, loading contributes one fifth and computation four fifths of the aggregate progress. Choose weights from expected work, not merely the number of child tasks.

The parent automatically becomes running when a child runs and finished when all enabled children are finished. It becomes aborted only when all enabled children are aborted. If application semantics require a different parent status, set `ConfigurationFlag::OverrideAggregateStatus` and manage the parent explicitly.

## Task hierarchy versus QObject ownership

Task parenting and `QObject` ownership are independent:

- the constructor's `QObject* parent` controls memory ownership;
- `setParentTask()` controls progress and status aggregation.

Set both deliberately. The task parent must not outlive pointers to its children, and all tasks in one hierarchy should have the same Qt thread affinity.

## Disabled and hidden tasks

Disabled child tasks are excluded from aggregation. Visibility controls whether a task is shown, while its GUI scopes control where it can be presented. Do not disable a child merely to hide it; that also changes the aggregate calculation.

Use hierarchies when child operations have independently meaningful state or cancellation. For a fixed list of simple steps, `Subtasks` mode is lighter and usually clearer.

