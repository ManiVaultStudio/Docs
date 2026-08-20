# Choosing status-bar content

Use the status bar only when information remains useful across many interactions and can be understood in little space.

| Need | Preferred mechanism |
| --- | --- |
| Persistent, lightweight plugin-kind state | Plugin status-bar action |
| Progress for long or cancellable work | Workflow-backed execution and its task projection |
| Brief outcome the user should notice | Plugin notification |
| Failure that prevents an operation from completing | Workflow result or exception at the owning boundary |
| Detailed or developer-oriented history | Logging |
| Controls or state for one plugin instance | The instance's own actions or view UI |

See {doc}`Choosing a reporting channel <../diagnostics/choosing_a_channel>` for the complete comparison.

## Good status-bar content

Suitable examples include:

- an aggregate connection or synchronization state;
- a short count or badge relevant across all instances;
- a compact mode toggle with application-wide meaning;
- a concise last-known state with details available in a popup;
- a quick route to a frequently used plugin-wide action.

Keep inline content short and stable. Move tables, histories, filters, and explanatory text into the popup or the plugin's main interface.

## Avoid duplicate progress and errors

The core already presents background tasks in a dedicated status-bar item. New substantial operations should normally use the workflow engine, which owns scheduling, results, cancellation, and progress; its task projection supplies the GUI progress. Do not mirror the same percentage in a second plugin-specific status item unless it conveys distinct aggregate state.

Likewise, do not keep a completed error in the status bar after already presenting it as a notification or failed workflow result. The status bar is state, not an event log.

## Decide the scope

One registered action belongs to one plugin kind. If only one plugin instance can exist, it may directly summarize that instance. Otherwise define an aggregation rule, for example:

- **3 views active**;
- the most severe state across instances;
- combined cache or queue size;
- state of the currently focused instance, clearly labelled as such;
- a popup listing every instance separately.

The rule should remain deterministic when instances are created, restored, renamed, or removed.
