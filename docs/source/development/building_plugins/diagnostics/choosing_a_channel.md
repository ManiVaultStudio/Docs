# Choosing a reporting channel

Use the channel according to what the recipient must do next.

| Situation | Prefer |
| --- | --- |
| Brief outcome the user should notice | Plugin notification |
| New long-running or cancellable operation | Workflow-backed execution with task progress where needed |
| Existing externally managed operation needs GUI progress | Directly managed task |
| Persistent lightweight plugin state | Status action or plugin status-bar action |
| Developer-oriented execution evidence | Qt log message |
| Operation cannot fulfill its contract | Exception or failed workflow job |
| Failure must be acknowledged immediately | Exception dialog at the UI boundary |

A warning is not automatically an exception. If the operation can complete with a documented fallback, report the fallback and continue. If continuing would produce invalid or misleading state, fail the operation.

Do not send the same failure through every channel. A lower layer should return or throw rich failure information; the layer that owns the user interaction decides whether to show a notification or dialog. Logging the technical details once is enough.

## User text and diagnostic evidence

User-facing text should say what failed, the effect, and any useful next step. Developer diagnostics should add operation names, stable IDs, paths where appropriate, relevant types, and the original cause. Avoid exposing secrets, credentials, full sensitive datasets, or unbounded payloads in either channel.
