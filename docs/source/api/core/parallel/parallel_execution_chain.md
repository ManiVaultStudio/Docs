# Parallel execution chain

`ParallelExecutionChain` is a move-only, single-use builder that combines sequential `run()` stages and parallel `forEach()` stages before executing the resulting workflow plan.

```{doxygenclass} mv::ParallelExecutionChain
:members:
```
