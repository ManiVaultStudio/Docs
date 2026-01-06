# App customization

## Customizing a ManiVault-based Application

A ManiVault “application” (or *viewer*) consists of:

- the **ManiVault core**, plus  
- one or more **additional plugins**.

Additionally, the application designer can customize specific aspects of the app to better suit their use case or organization.

Customization can be done in two ways:

1. **From within the UI** (recommended for most users), or  
2. **By editing JSON files** in the customization directory.

This section focuses on customizing the application **from the UI**. The JSON files written by the UI are described along the way and can also be edited manually.

---

## Customization directory

All app-specific customization lives in the **customization directory**. By default, this is:

```text
<app_dir>/Customization
```

From C++ code, you can query this location via [mv::util::StandardPaths](ManiVault/src/util/StandardPaths.h).

The directory layout is:

- `app.json`  
  Stores the customization settings generated from the UI (branding, start page, etc.).

- `projects.json` (optional)  
  Lists **Project Data Source Names (DSNs)** that should be exposed in the app. If present, these projects will be available on the start page and in the projects main menu.

- `assets/`  
  Holds app-specific assets, for example:
  - `SplashScreen.html` to override the default splash screen.
  - (Future) additional images or HTML fragments for branding.

You can safely commit this directory into your app repo, or ship it alongside the application as part of your distribution.

---

## Opening the customization UI

To customize the app from within the running application:

1. Start your ManiVault-based application.
2. Press **`Ctrl + F8`** to open the **Customization** panel.

<img width="640" height="509" alt="image" src="https://github.com/user-attachments/assets/db86679a-7d6b-48e5-9932-eba4a2c88c24" />

The customization UI is divided into three categories:

1. **Branding**
2. **Start page**
3. **Projects**

All changes made here are written to `app.json` (and `projects.json` when you edit DSNs).

---

## Branding

The **Branding** category controls where settings are stored and how the application presents itself visually.

### Identity and settings storage

These three fields are **mandatory** and together determine where application settings are stored:

- **Organization name**  
  The human-readable name of your organization (`qApp->setOrganizationName(<organization_name>)`).

- **Organization domain**  
  Typically a DNS-style domain (e.g. `example.org`).  
  Used (together with the organization name) to build a stable settings path (`qApp->setOrganizationDomain(<organization_domain>)`).

- **Full name**  
  The full application name that is used for the application identity.  
  Internally, this is used as the application name when storing settings (for example via `qApp->setApplicationName(<full_name>)`).

```{note}
These three properties are crucial. Changes here will affect the location where ManiVault stores user and application settings. You generally want to set them once when designing the app and not change them afterwards.

### Display name and version

- **Base name**  
  A short internal name of the application (e.g. `MyViewer`).  
  This can be used as a concise identifier and is also used as the basis for auto-generating the full name.

- **Full name**  
  By default, the full name is automatically generated from the base name and the app version, e.g. `MyViewer 1.2.0`.  
  This value is mandatory (see above) and can either follow the automatic scheme or be overridden manually.

- **Override full name** (toggle)  
  When enabled, you can manually edit the full name field.  
  This is useful if you want a more descriptive marketing name, or if you don’t want the version in the window title.

### Visual branding

- **Logo**  
  Lets you select an image used as the app logo.  
  Currently, the logo is used on the **start page**, but this may be extended in future versions.

- **App icon editor**  
  Lets you load a PNG image that is converted into an application icon.  
  - You can **preview** the icon live in different sizes.  
  - This **does not** change the executable’s icon on disk; it affects the icon used within the ManiVault UI (e.g. start page tiles, windows, etc.).

- **Convert logo to icon** (button)  
  Convenience button to convert the current logo directly into an icon, so you don’t have to provide the same asset twice.

### Splash screen

- **Enable custom splash screen** (toggle)  
  When enabled, the app uses a custom splash screen from the customization directory.

- **Preview splash screen**  
  Allows you to preview the current splash screen directly from the UI.

The splash screen is typically defined by `assets/SplashScreen.html` in the customization directory. A splash screen customization tutorial will follow soon.

### About dialog text

- **Custom “About” text**  
  Lets you override the default text shown when users go to **Help → About**.

You can use this to:

- Describe the purpose of your application,
- Add licensing or attribution information,
- Provide links to documentation or support.

The text is stored in `app.json` and can be plain text or (depending on implementation) a subset of rich text/HTML.

---

## Start page

The **Start page** category gives app designers control over which sections appear on the start page and how dense it looks.

### Layout

- **Compact** (toggle)  
  Switches between:
  - A **high-density** layout (compact) with tighter spacing, and  
  - A **low-density** layout with more whitespace and larger items.

Use this to match the style of your app: compact for expert tools, more spacious for visually guided workflows.

### Sections

Each toggle shows or hides a section on the start page:

- **Open & Create**  
  Controls the visibility of actions related to opening existing projects and creating new ones.

- **Project databases**  
  Enables or disables the section that lists projects from configured **project DSNs**.  
  (See the **Projects** category below for DSN configuration.)

- **Recent projects**  
  Shows or hides the list of previously opened projects, making it quick to resume recent work.

- **Project from data**  
  Toggles the section that allows users to create a new project and load data of a selected type.

- **Project from workspace**  
  Toggles the section for creating a new project from a **workspace template**  
  (Note: not operational at the moment; the UI is present, but functionality may be incomplete).

- **Tutorials**  
  Controls the section listing available tutorials (and optionally related projects).  
  This is useful for onboarding new users or guiding them through typical workflows.

All these settings are stored in `app.json`. Toggling them in the UI is the recommended way to configure the start page, but you can also edit them directly in JSON if you need to automate or script app setups.

---

## Projects

The **Projects** category is where app designers configure **Project Data Source Names (DSNs)**.

When DSNs are configured correctly:

- Projects from those DSNs become available on the **start page**, and  
- They also appear in the **Projects** main menu inside the application.

The DSN configuration is stored in `projects.json` in the customization directory. Each DSN describes how to reach a projects repository (local or remote). For full details on remote projects and DSN formats, see the {doc}`Hosting projects <hosting_projects>` guide for details.

In short:

- Use the **Projects** UI category to add/edit DSNs.
- Verify that the DSN settings are valid (URL, authentication, etc.).
- Once saved, the configured project databases become available on the start page when the **Project databases** toggle (in the Start page category) is enabled.

---

## Summary

- The **customization directory** (`<app_dir>/Customization`) holds all app-specific settings and assets (`app.json`, `projects.json`, `assets/…`).
- Press **`Ctrl + F8`** in the running application to open the **Customization UI**.
- Use:
  - **Branding** to define identity, settings storage, logo/icon, splash screen, and About text.
  - **Start page** to control which sections the user sees and how dense the layout is.
  - **Projects** to configure project DSNs that feed into the start page and project menus.

You can either:

- Use this UI to configure your app and commit the resulting customization files, or  
- Treat `app.json` / `projects.json` as configuration files that you manage alongside your app builds (e.g., for different branded distributions).
