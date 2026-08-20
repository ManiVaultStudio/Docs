# Qt plugin considerations

ManiVault plugins are Qt components loaded into a long-running GUI application. Correct plugin code must account for both C++ object lifetime and Qt's additional contracts: QObject parentage, thread affinity, queued delivery, meta-object generation, widget ownership, and event-loop-driven destruction.

This section incorporates the former **QObject Lifetime & Ownership Guidelines** and places those rules alongside the related threading, connection, build, UI, and teardown guidance.

```{toctree}
:maxdepth: 2

qobject_ownership
connections_and_callbacks
threads_and_event_loop
meta_object_and_build
widgets_models_and_presentation
teardown_and_testing
```

Domain-specific pages still describe their own contracts. In particular, see {doc}`Action ownership <../actions/lifecycle>`, {doc}`Dataset removal <../data/events/removal_and_lifetime>`, {doc}`Plugin lifecycle <../fundamentals/lifecycle>`, and {doc}`Workflow threading <../../workflows/threading_and_parallelism>`.
