# PointRenderer

**Qualified name:** `mv::gui::PointRenderer`

## Z ordering

`PointZOrderMode` controls how overlapping points receive depth:

- `InsertionOrder` assigns equal depth to every point, so draw and insertion order determine visibility. This is the default.
- `Dimension` derives depth from a scalar supplied for each point with `setZOrderChannelScalars()`. The renderer computes the scalar range and normalizes values for depth assignment.
- `Randomized` derives a deterministic pseudo-random depth from the point index. It can reduce systematic insertion-order bias without requiring a data dimension.

Configure dimension-controlled ordering by supplying one scalar per rendered point before selecting the mode:

```cpp
renderer.setZOrderChannelScalars(zOrderValues);
renderer.setZOrderMode(mv::gui::PointZOrderMode::Dimension);
```

If dimension mode has no Z-order scalar buffer, points retain equal depth. Keep the scalar vector aligned with the position vector whenever point data changes.

`getRandomizedDepthEnabled()` and `setRandomizedDepthEnabled()` remain compatibility conveniences. Enabling randomized depth selects `Randomized`; disabling it selects `InsertionOrder`. Use `getZOrderMode()` and `setZOrderMode()` when code must distinguish all three modes.

```{doxygenenum} mv::gui::PointZOrderMode
```

```{doxygenclass} mv::gui::PointRenderer
:members:
:protected-members:
```
