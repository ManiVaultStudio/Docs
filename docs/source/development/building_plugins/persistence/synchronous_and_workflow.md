# Synchronous and workflow serialization

`Serializable` exposes two layers. Choose based on the work performed, not the size of the class.

## Synchronous contract

Override `fromVariantMap()` and `toVariantMap()` when the operation completes immediately. These functions must finish before returning and must not launch background work, execute a workflow, or defer state changes.

The default `fromVariantMapWorkflow()` and `toVariantMapWorkflow()` implementations wrap the synchronous methods, so simple objects need no workflow override.

## Workflow contract

Override the workflow methods when persistence is expensive, staged, parallelizable, requires GUI-thread phases, or should report progress:

```cpp
mv::workflow::UniqueWorkflowPlan ExamplePlugin::toVariantMapWorkflow() const
{
    auto plan = std::make_unique<mv::workflow::WorkflowPlan>("Save example");

    plan->addSequentialStage("Collect settings",
        [this](const auto&, const auto& context) {
            context->setOutput(toVariantMap());
        },
        mv::workflow::WorkflowPlan::JobThreadAffinity::GuiThread);

    return plan;
}
```

Workflow methods construct plans; they do not execute them. Publish the serialized `QVariantMap` as workflow output and let project orchestration compose and execute the plan.

Parent-map and JSON convenience helpers call the synchronous methods directly. They do not discover or execute custom workflow serialization. For workflow composition, see {doc}`Nested workflows <../../workflows/nested_workflows>`.
