# Building applications

A ManiVault-based application combines the core, a deliberate plugin set, application identity and branding, and optionally curated projects or tutorials. Building the executable is only the first stage: a complete application also defines what users can do, how they enter the workflow, and which content is supported.

Start with {doc}`creating_an_application`. It connects the complete lifecycle:

```text
define the product
        ↓
compose core and plugins with DevBundle
        ↓
build and verify the integrated application
        ↓
configure identity, branding, and start page
        ↓
publish and expose projects or tutorials
        ↓
validate the end-user experience
```

## Application workflow

| Stage | Guide | Outcome |
|---|---|---|
| Plan and compose | {doc}`creating_an_application` | Reproducible DevBundle definition and integrated build |
| Customize | {doc}`app_customization` | Stable identity, branding, and start-page configuration |
| Customize startup | {doc}`splash_screen_customization` | Branded HTML splash screen with progress feedback |
| Curate a workflow | {doc}`publishing_a_project` | Controlled, read-only project experience |
| Distribute projects | {doc}`hosting_projects` | Discoverable local or remote project catalog |
| Teach workflows | {doc}`hosting_tutorials` | Tutorials available from the start page and Learning Center |

The application build must contain every plugin needed by its projects and tutorials. Configuration controls presentation and discovery; it does not add missing compiled capabilities.

```{toctree}
:maxdepth: 2

creating_an_application
app_customization
splash_screen_customization
publishing_a_project
hosting_projects
hosting_tutorials
```
