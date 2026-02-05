# Graphics

The graphics module provides low-level rendering infrastructure used throughout the application for efficient and reusable GPU-based visualization. It defines a generic renderer abstraction alongside a set of helper classes that encapsulate common rendering patterns and graphics resources.

Renderers focus on orchestrating draw calls and rendering logic, while helper classes provide thin, explicit wrappers around graphics primitives such as buffers, shaders, textures, framebuffers, and mathematical types. Together, these components form a minimal and flexible foundation for building higher-level visualizations without imposing a specific rendering strategy.

## Renderer class

Below are renderer classes often used in **ManiVault**, for instance in the [scatterplot plugin](https://github.com/ManiVaultStudio/scatterplot).

```{toctree}
:maxdepth: 2

renderers/renderer
helpers/renderer_2d
helpers/point_renderer
helpers/density_renderer
```

## Helper classes

The helper classes below are used to expedite the renderer development. 

```{toctree}
:maxdepth: 2

helpers/bounds
helpers/buffer_object
helpers/frame_buffer
helpers/matrix_3f
helpers/off_screen_buffer
helpers/selection
helpers/shader
helpers/texture
helpers/vector_2f
helpers/vector_3f
```