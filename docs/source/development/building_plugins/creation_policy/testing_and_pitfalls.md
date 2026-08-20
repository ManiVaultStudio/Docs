# Testing and pitfalls

Test creation policy as lifecycle behavior, not just as a disabled menu action.

## Minimum test matrix

- Create instances up to the maximum and verify that the next manager request fails cleanly.
- Confirm the standard trigger becomes disabled at the maximum.
- Destroy one instance and verify that another can be created and the trigger becomes enabled again.
- Verify hidden-from-standard-GUI plugins are absent from standard surfaces but remain requestable through the intended controlled path.
- Exercise every supported contextual dataset selection and confirm unsupported selections offer no trigger.
- Save and reopen a project containing the maximum supported number of instances.
- Open older projects containing the number of instances allowed by earlier releases.
- Exercise production, `init()`, loading, and teardown failures without leaving visible partial state.
- Close the application or project with instances still alive and check shutdown ordering.

## Common mistakes

### Setting the limit on an instance

Creation policy belongs to the factory. Configure it in the factory constructor or startup path, before the first request.

### Updating the counters manually

The current and cumulative counters reflect core-managed ownership. Setting them from plugin code can allow too many instances, permanently disable a trigger, or corrupt later destruction accounting.

### Calling `produce()` directly

The returned object has not followed the managed creation path. Use `mv::plugins().requestPlugin(...)` instead.

### Treating the GUI flag as enforcement

The flag controls standard presentation only. Programmatic requests and restoration still reach the manager and are governed by the instance limit.

### Using only a preflight check

`mayProduce()` does not reserve capacity. Handle the manager request's failure path.

### Changing the maximum at runtime

The setter does not evict existing instances or immediately refresh every UI representation. Prefer stable startup policy. If dynamic changes are required, define saturation, UI refresh, and persistence behavior explicitly.

### Ignoring saved projects

A limit that is correct for new sessions may reject instances recorded in existing projects. Include restoration fixtures whenever changing the policy.

## Review checklist

- Is the limit justified by correctness or a measured resource constraint?
- Is the policy configured on the factory before creation becomes available?
- Do all pathways request through the plugin manager?
- Are contextual input rules represented by triggers rather than global counts?
- Is failure surfaced through an appropriate diagnostics channel?
- Are project compatibility and teardown covered by tests?
