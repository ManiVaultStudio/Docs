# Recipes and testing

## Replace or add

If a loaded plugin can either replace its primary input or add a secondary input, make those consequences separate regions. Avoid a generic **Load** region whose behavior changes invisibly with current state.

## Accept compatible derived datasets

When a plugin accepts both full and derived datasets of the same data type, test the real requirements rather than rejecting all derived data. Conversely, validate row counts, dimensions, source relationships, or mutability when the operation depends on them. Type compatibility alone does not guarantee semantic compatibility.

## Start long-running work

Treat a drop callback like any other plugin command. Update lightweight state directly, but run substantial operations through the {doc}`workflow engine or task facilities <../tasks/tasks_and_workflows>`. Recheck captured handles when execution begins and report failures through the normal workflow or diagnostic channels.

## Testing checklist

Exercise drag and drop with:

- no datasets, one dataset, and a hierarchy multi-selection;
- the expected type and at least one unrelated data type;
- full, derived, and subset datasets where relevant;
- a dataset removed or replaced shortly after the drop;
- every region when several operations are offered;
- leaving the target without dropping;
- resizing the target before and during interaction;
- an empty state and a populated state;
- light and dark themes, long dataset names, and a narrow target;
- project restore followed by a new drop;
- long-running work, cancellation, and plugin destruction.

## Common pitfalls

### Nothing happens on drag enter

Confirm that the target, rather than only one of its children, has `setAcceptDrops(true)`, and that `initialize()` was called before the widget became interactive. Returning no regions deliberately rejects the drag.

### File drags appear to be ignored

`DatasetsMimeData` represents datasets dragged inside ManiVault. Operating-system file drags use different MIME data and should be implemented as a separate import interaction.

### The wrong item is loaded from a multi-selection

Do not call `first()` until the dataset count has been validated. Either require exactly one input or define and communicate group behavior.

### An unavailable region still performs work

The visual `dropAllowed` flag is not an authorization check. Do not attach an active callback to an unavailable region, and validate important preconditions again inside enabled callbacks.

### A callback uses stale data

Capture `Dataset<T>` handles instead of raw dataset pointers, and check `isValid()` at the time of use. For asynchronous work, follow the dataset access and cancellation rules described in {doc}`Working with data and datasets <../data/index>` and {doc}`Tasks and workflows <../tasks/index>`.
