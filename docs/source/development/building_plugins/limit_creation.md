# Limiting Plugin Instance Creation

ManiVault supports limiting how many instances of a given plugin can be created. This is useful when:

- A plugin is **expensive** (GPU/CPU/memory heavy) and should not be instantiated many times.
- A plugin represents a **singleton-like resource** (e.g., a global service, exclusive device handle).
- An application designer wants a **curated workflow**, where only a controlled set of plugin instances can be added.

This page documents the API for **querying** instance counts and **configuring** the maximum number of allowed instances.

---

## Concepts

The API distinguishes between two counters and one limit:

- **Number of instances (loaded)**  
  The number of plugin instances that are currently alive/loaded in the application.

- **Number of instances produced (lifetime total)**  
  The total number of instances that have been created during the current application session (even if they were later closed/unloaded).

- **Maximum number of instances**  
  The upper bound on how many instances may exist at the same time. If the maximum is reached, additional instances are not created.

> **Unlimited instances**  
> If `maximumNumberOfInstances == -1`, there is no limit. Because the API uses `std::uint32_t`, this value is represented as:
>
> ```cpp
> static_cast<std::uint32_t>(-1)
> // or equivalently
> std::numeric_limits<std::uint32_t>::max()
> ```
>
> In other words: the “no limit” sentinel is the maximum representable `uint32_t` value.

---

## API

### Querying the current number of loaded instances

```cpp
std::uint32_t getNumberOfInstances() const;
```

Returns the number of plugin instances currently loaded.

### Setting the current number of loaded instances

```cpp
void setNumberOfInstances(std::uint32_t numberOfInstances);
```

Sets the number of plugin instances currently loaded.

> In normal usage you should not need to call this directly. The **core maintains these counters internally**.

### Querying the total number of instances produced

```cpp
std::uint32_t getNumberOfInstancesProduced() const;
```

Returns the total number of instances produced during the current application session.

### Setting the total number of instances produced

```cpp
void setNumberOfInstancesProduced(std::uint32_t numberOfInstancesProduced);
```

Sets the total number of produced instances.

> In normal usage you should not need to call this directly. The **core maintains these counters internally**.

### Querying the maximum number of allowed instances

```cpp
std::uint32_t getMaximumNumberOfInstances() const;
```

Returns the maximum number of instances allowed to exist simultaneously.

### Setting the maximum number of allowed instances

```cpp
void setMaximumNumberOfInstances(std::uint32_t maximumNumberOfInstances);
```

Sets the maximum number of instances allowed to exist simultaneously.

---

## Signals

The API provides signals that allow the UI (or other observers) to react to changes.

### Loaded instance count changed

```cpp
void numberOfInstancesChanged(std::uint32_t numberOfInstances);
```

Emitted when the number of currently loaded instances changes.

### Total produced instance count changed

```cpp
void numberOfInstancesProducedChanged(std::uint32_t numberOfInstancesProduced);
```

Emitted when the total number of produced instances changes.

---

## Recommended Usage

Typical usage is to set a maximum (or leave it unlimited) and let the **core** enforce and track the counters.

```cpp
// Allow at most one instance (singleton-style)
plugin->setMaximumNumberOfInstances(1);

// Allow unlimited instances (this is the default)
plugin->setMaximumNumberOfInstances(static_cast<std::uint32_t>(-1));
```

