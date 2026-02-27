# QObject Lifetime & Ownership Guidelines

## Overview

Qt's object model is built around **heap allocation + parent--child
ownership**. However, ManiVault's codebase deliberately uses a different
pattern in many places:

> Most `QObject`-derived helper objects are stored as **stack/member
> subobjects**, while only top-level components are dynamically
> allocated.

This document explains: - When this pattern is safe - When it is
unsafe - Why ManiVault uses it - The constraints developers must follow

------------------------------------------------------------------------

## Qt's Default Ownership Model

In standard Qt practice:

``` cpp
auto *child = new QObject(parent);
```

-   Parent owns the child.
-   Parent deletes child in `QObject::~QObject()`.
-   This model assumes heap allocation.

This is the most common and safest approach when: - Objects are
reparented - Ownership is transferred - Objects are shared across
components - Objects are passed to Qt containers (menus, widgets,
toolbars, etc.)

------------------------------------------------------------------------

## ManiVault's Allocation Strategy

### Design Principle

In ManiVault:

-   **Top-level components** are heap allocated.
-   **Internal helper QObjects** are often stack/member objects.
-   Parent is typically set to `this`.
-   Ownership is strictly hierarchical and local.

Example:

``` cpp
class StandardItemModel : public QStandardItemModel {
    Q_OBJECT
private:
    gui::NumberOfRowsAction _numberOfRowsAction{this};
};
```

### Why We Do This

The reasons are architectural and deliberate:

1.  **Deterministic lifetime**
    -   Member subobjects are destroyed automatically.
    -   No raw `new/delete` management.
2.  **No scattered heap allocations**
    -   Improves locality.
    -   Reduces pointer chasing.
    -   Easier reasoning about ownership.
3.  **Strict containment**
    -   Helpers never outlive their owner.
    -   Ownership boundaries are explicit in class structure.
4.  **Architectural clarity**
    -   Object graph mirrors class composition.
    -   No hidden ownership transfers.

This approach works because the majority of these objects: - Are not
reparented - Are not handed to ownership-taking APIs - Do not cross
thread boundaries - Are fully contained within their owning component

------------------------------------------------------------------------

## When Stack-Allocated QObjects Are Safe

A `QObject`-derived member object is safe **only if all of the following
are true**:

✔ Parent is either: - `this` (the enclosing owner), OR - `nullptr`
permanently
✔ It is never reparented
✔ It is never passed to APIs that assume ownership
Examples of risky APIs: - `QWidget::addAction()` -
`QMenu::addAction()` - `QToolBar::addAction()` - Any API that may call
`setParent()`
✔ It is never deleted via `deleteLater()`
✔ It does not receive queued signals after derived destruction begins

------------------------------------------------------------------------

## Common Failure Mode (Linux-only Crashes)

Typical assertion:

    ASSERT failure in qobjectdefs_impl.h:
    "Called object is not of the correct type
    (class destructor may have already run)"

This usually indicates:

> A queued signal is invoking a slot in a derived class after that
> derived destructor has already executed.

This is not inherently a stack-allocation issue.\
It is usually caused by:

-   `Qt::QueuedConnection`
-   Cross-thread `AutoConnection`
-   Timers still running during teardown
-   Signals emitted during destruction

Linux timing makes these more visible than Windows.

------------------------------------------------------------------------

## Required Teardown Discipline

When using stack/member QObjects:

### Always stop active emitters in destructor

``` cpp
~ActionsHierarchyModel() override
{
    _timer.stop();
    QObject::disconnect(&_numberOfRowsAction, nullptr, this, nullptr);
}
```

### Avoid queued connections into derived classes during teardown

If necessary, disconnect in the derived destructor.

------------------------------------------------------------------------

## When Heap Allocation Is Required

Use heap allocation (`new` + parent) if any of the following apply:

-   Object may be reparented
-   Object may outlive the owning component
-   Object participates in UI container ownership
-   Object crosses thread boundaries
-   Object may receive queued events late in destruction
-   Object is part of a plugin boundary
-   Ownership is not strictly hierarchical

Example:

``` cpp
_numberOfRowsAction = new gui::NumberOfRowsAction(this);
```

This eliminates: - Accidental ownership transfer - Undefined delete
behavior - Destructor ordering hazards

------------------------------------------------------------------------

## Project Policy

### We do NOT mandate heap allocation for all QObjects.

Instead:

-   Stack/member QObjects are allowed and widely used.
-   They must follow the safety constraints defined above.
-   High-risk categories should prefer heap allocation.

### High-risk categories

Prefer heap allocation for:

-   `QAction`
-   `QTimer`
-   UI-related QObjects
-   Cross-thread workers
-   Plugin-boundary objects

------------------------------------------------------------------------

## Decision Rule for Developers

Before adding a stack-allocated QObject member, ask:

> "Could any other object ever delete or reparent this QObject?"

If the answer is **yes or maybe**, allocate it on the heap.

If the answer is **definitively no**, stack allocation is acceptable.

------------------------------------------------------------------------

## Summary

ManiVault's stack-allocation pattern:

-   Is intentional.
-   Improves architectural clarity and determinism.
-   Works reliably under strict constraints.
-   Requires disciplined ownership and teardown management.

We do not refactor the entire codebase to heap allocation.

Instead, we:
- Maintain strict containment rules.
- Convert only high-risk objects to heap allocation.
- Ensure teardown is safe against queued delivery.
