# Publishing a Project

In ManiVault-based applications, a **published project** is a special, “baked” variant of a normal project. Published projects are typically used in **tailor-made applications** and viewer distributions, where you want a controlled experience for end users.

An application or viewer will often contain one or more published projects. While publishing is not mandatory, it can be very useful in scenarios where you want to ship a fixed layout and a restricted set of tools.

---

### What is a published project?

Conceptually, you can think of a published project as a **read-only, baked project**:

- The **view layout is fixed**  
  Users cannot freely rearrange or add/remove views (unless explicitly allowed by the viewer).

- The **locations of view plugins are fixed**  
  Which views are present, and where they appear in the layout, is defined by the publisher.

- The set of **plugins that users can add later from the UI can be limited**  
  You can restrict which additional plugins can be created from the UI *after* the published project is loaded.  
  This does **not** remove plugins that are already part of the published layout; it only affects what users can add themselves at runtime.

In the **Publish project** dialog, these and other options are configured through a combination of main fields and an advanced **settings panel** (opened via the gear icon). The settings panel groups together more detailed controls for how the published project behaves and what users are allowed to do (for example, which plugins they can add from the UI).

In other words: a published project wraps up your data + layout + plugin configuration into a controlled package that can be embedded into an application.

> **Note**  
> In future versions we plan to add more fine-grained control over how the published project is presented to the user (for example, which parts of the UI are visible, which interactions are allowed, etc.).

---

### When should you publish a project?

Publishing is especially useful when:

- You are building a **tailor-made viewer** for a specific workflow or audience.
- You want to distribute a **demo or showcase** with a curated layout and limited controls.
- You need to **lock down the analysis environment**, so users can explore but not change the core setup.
- You want to ensure **reproducible layouts** across installations (everyone sees the same views in the same places).

If you are working on an exploratory analysis for yourself, a normal (unpublished) project is usually sufficient. When that analysis turns into something you want to ship to others as a stable product, it’s a good candidate for publishing.

---

### Preparing a project for publishing

Before you publish, it helps to:

1. **Finalize the view layout**
   - Open the project in your ManiVault-based application.
   - Arrange views (scatter plots, embeddings, tables, etc.) exactly as you want end users to see them.
   - Remove temporary or experimental views that shouldn’t be part of the shipped experience.

2. **Select and configure plugins**
   - Load only the plugins you want to appear in the final layout.
   - Configure their options (color schemes, selections, filters, etc.) as needed.

3. **Save the project**
   - Save the project in its final state so the publisher has a clean, consistent starting point.

---

### Publishing a project
<img width="811" height="645" alt="image" src="https://github.com/user-attachments/assets/46b12982-f156-4cd2-9d3d-49578d0de545" />

*Example of the “Publish project” dialog.*

<img width="431" height="544" alt="image" src="https://github.com/user-attachments/assets/fcf75778-e147-41f9-97c7-1e527773c085" />

*The advanced settings panel is opened by clicking the gear icon.*

1. **Open the project you want to publish**
   - Start ManiVault Studio.
   - Load the project that you prepared in the previous section.

2. **Open the publish command**
   - In the main window, go to:
     ```text
     Main menu → Publish project…
     ```
   - This opens the publish dialog that contains:
     - Compression settings,
     - Entry for the project title,
     - And an advanced **settings panel**, accessible via the gear icon for more detailed configuration (including plugin-related options)
5. **Use the settings panel to refine behavior (optional but recommended)**
   - Click the **gear icon** in the publish dialog to open the settings panel.
   - In this panel, you can configure several advanced options, including which plugins users are allowed to **add from the UI** once the published project is loaded.
   - For plugin limits in particular:
     - Enable only the plugins that users should be able to add from the UI.
     - Disable plugins that are experimental, irrelevant, or internal-only.
   - This restriction only affects plugins that users can **create from the UI**; any plugins already present in the published layout remain available.

6. **Choose the output location**
   - Select where the published project should be saved (for example, a projects directory that will later be packaged with your application).
   - Confirm the file name and location.

7. **Publish**
   - Start the publishing process.
   - Once it completes, you will have a **published project artifact** that can be included in your ManiVault-based application or distributed to users as part of a viewer.

---

### Using a published project in an application

After publishing, the resulting project is typically:

- **Bundled with an application/viewer**, so that:
  - The viewer opens directly into the published project at startup, or
  - The project appears in a list of available projects on the start page.

- **Treated as read-only**:
  - Users can explore, filter, zoom, and interact, but they cannot overwrite or fundamentally change the underlying published configuration.

- **Optionally restricted in terms of new plugins**:
  - Users may be prevented from adding new plugin instances from the UI, depending on how you configured plugin limits during publishing.
  - Plugins that are already part of the published layout continue to function as normal.

How exactly a published project is discovered and presented (start page entries, menu items, etc.) is determined by your application’s configuration (for example, via project DSNs or app-specific configuration files).

---

### Summary

- A **published project** is a **read-only, baked** variant of a regular project, primarily used in **tailor-made applications**.
- Publishing lets you fix:
  - The **view layout**,
  - The **positions of view plugins**,
  - And **which additional plugins users can add later from the UI**, configured via the publish dialog’s settings panel.
- This creates a controlled, reproducible viewing experience for end users.
- In future versions, more fine-grained control will be added to further customize how a published project is presented in the UI.
