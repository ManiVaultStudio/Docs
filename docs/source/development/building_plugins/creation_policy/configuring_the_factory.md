# Configuring the factory

Configure stable creation policy on the factory during factory construction or startup, before users can request instances.

```cpp
ExamplePluginFactory::ExamplePluginFactory()
{
    setMaximumNumberOfInstances(1);
    setAllowPluginCreationFromStandardGui(true);
}
```

The setter belongs to `PluginFactory`; there is no instance-level creation policy. Every instance of a kind shares the same factory and therefore the same limit.

## Maximum instances

`setMaximumNumberOfInstances()` sets the number of live instances that may coexist:

```cpp
setMaximumNumberOfInstances(1);  // singleton-like
setMaximumNumberOfInstances(4);  // finite pool
setMaximumNumberOfInstances(0);  // no instance may be created
```

Unlimited creation is the default. The internal value is an unsigned 32-bit integer initialized with `-1`, so code that needs to state the default explicitly can use:

```cpp
setMaximumNumberOfInstances(std::numeric_limits<std::uint32_t>::max());
```

Usually it is clearer simply not to call the setter for the unlimited case.

## Standard-GUI creation

Use the standard-GUI flag when instances should only be created by a controlled integration path:

```cpp
setAllowPluginCreationFromStandardGui(false);
```

Standard interfaces such as the data-hierarchy context menu inspect this flag before showing plugin trigger actions. Code may still call `mv::plugins().requestPlugin(...)`, and the normal maximum-instance check still applies.

## Counters are core-owned

Factories expose three related values:

- `getNumberOfInstances()` is the current live count.
- `getNumberOfInstancesProduced()` is the cumulative count produced in this application session.
- `getMaximumNumberOfInstances()` is the concurrent limit.

Do not call `setNumberOfInstances()` or `setNumberOfInstancesProduced()` from plugin code. The plugin manager increments them during managed creation, and plugin destruction updates the live count. Manual changes desynchronize trigger state and enforcement from actual ownership.

The cumulative produced count is useful for diagnostics or unique naming. It is not used to decide whether another instance may be created.

## Keep policy static after startup

Treat the maximum as startup configuration. `setMaximumNumberOfInstances()` changes the stored maximum but does not itself emit a policy-change signal or immediately recompute the standard trigger's enabled state. The standard trigger is recomputed when the live count changes.

If an application truly needs runtime policy changes, it must explicitly update the surrounding UI and define what happens when the new maximum is below the current live count. Existing instances are not automatically destroyed.
