# Reporting and metrics

Reporting types capture lifecycle events, structured diagnostics, aggregate metrics, and stage summaries. Presentation types render this information for result dialogs and detailed message inspection without owning workflow control flow.

For reporting conventions, see {doc}`Reporting, metrics, and profiling <../../../../development/workflows/reporting_and_profiling>`.

Workflow messages are part of a particular execution result. They are distinct from the process-wide {doc}`Qt logging pipeline <../../util/logging/index>`: messages preserve workflow context and can be shown with the result, while Qt logs provide general developer diagnostics.

```{toctree}
:maxdepth: 1

workflow_message
abstract_workflow_messages_model
workflow_messages_list_model
workflow_messages_tree_model
workflow_messages_filter_model
workflow_report_node
workflow_metric
workflow_execution_metrics
workflow_stage_summary
workflow_result_details_options
workflow_result_dialog
```
