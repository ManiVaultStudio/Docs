# Hosting projects

Make your plugin even more useful by exposing remote projects directly from the **ManiVault Studio** start page.

<img src="https://github.com/user-attachments/assets/22c51124-ec89-45a0-8efc-2d620e10682f" alt="Project Teaser" width="500">  

*A preview of what the user will experience when remote projects are configured correctly.*

---

## Purpose  
This guide explains how plugin developers can make their **ManiVault Studio** projects available remotely. These projects will show up on the **ManiVault Studio** start page, making them easily discoverable and instantly accessible by users.

---

## Step-by-Step Instructions

### 1. Upload Your Project(s)
Host your **.mv** project files on a publicly accessible web server. These could be on:
- an institutional server,
- a file hosting service,
- or any location **ManiVault Studio** can reach via **HTTPS**.

### 2. Create a Project Metadata JSON
Prepare a **JSON** file describing the projects you uploaded. This file must conform to the rules of the [projects JSON schema](https://github.com/ManiVaultStudio/core/blob/master/ManiVault/res/json/projects.schema.json).  

Each entry describes one project:
| Name | Required | Notes |
|-------------------|-----|------|
| `title`           | ✅ | |
| `uuid` | ✅ | This is neceassary to reference the project unambiguously, you should generate one yourself with a [UUID generator](https://www.uuidgenerator.net/). 
| `ignore`           |  | Do not list the project when this option is `true` |
| `group`           |   | The group to which this project belongs (the project will be accessible by expanding this group in the GUI). |
| `startup` | | Flags the project as a startup project (for future use)
| `url`             | ✅ | Provide a (direct download link) |
| `summary`         | ✅ | HTML formatting is allowed. |
| `requiredPlugins` | ✅ | If any plugin is not available on the user end, the project will not be listed, see the [Caveats and notes](#Caveats--Notes) section for more info. |
| `coreVersion`     | ✅ | For more info, see the example. |
| `tags`     | ✅ | |
| `date`     | ✅ | |
| `downloadSize` | | Set this value if the download size cannot be established automatically by ManiVault (in case of URLs with redirects). |
| `hardwareRequirements` | | Minimum and recommended hardware requirements for loading the project. |

For example:

```json
[
  {
    "title": "Example Project",
    "uuid": "b730760f-b494-4d99-b584-419a64ccb2d5",
    "url": "https://example.com/myproject.zip",
    "summary": "<p>Demo for my plugin</p>",
    "requiredPlugins": [
      { "name": "MyPlugin", "repoName": "MyPluginRepo", "version": "1.0" }
    ],
    "coreVersion": { "major": 1, "minor": 0, "patch": 0, "suffix": "" },
    "tags": ["Demo", "MyPlugin"],
    "date": "2025-06-16 13:00:00"
  }
]
```
*You can find **ManiVault Studio** **JSON schemas** [here](https://github.com/ManiVaultStudio/core/blob/master/ManiVault/res/json/).*

### 3. Upload the JSON File
Once your **JSON** is ready:
- Upload it to the same (or another) accessible web location.
- Ensure it's reachable via a direct **HTTP/HTTPS** URL.

### 4. Register the JSON URL in Your Plugin
In your plugin factory (either in `mv::PluginFactory::PluginFactory()` or `mv::PluginFactory::initialize()`), register the **JSON**'s URL with:

```cpp
mv::PluginFactory::getProjectsDsnsAction().addString("https://example.com/my_plugin_projects.json");
```

## Summary: Registering Remote Projects in ManiVault Studio

| Step | Action                                                                          |
|------|----------------------------------------------------------------------------------|
| 1    | Upload your project files somewhere downloadable                                |
| 2    | Create a **projects JSON** metadata file conforming to the [projects](https://github.com/ManiVaultStudio/core/blob/master/ManiVault/res/json/projects.schema.json) schema                    |
| 3    | Host the **projects JSON** file online                                                       |
| 4    | Register the **projects JSON** file in your plugin via `mv::PluginFactory::getProjectsDsnsAction().addString("https://example.com/projects.json")` |
| 5    | Users will see the project(s) on the start page and can click to download + open   |
## What Happens in ManiVault Studio
When everything is set up:
- The remote projects you defined will appear under the **Projects** section of the start page, clearly labeled and searchable.
- Users can filter remote projects based on **name**, **version**, and **tags**.
- A single click on a listed project:
  - Downloads the **.mv** file from the URL (if already downloaded, the user decides whether to open the downloaded file or download again).
  - Opens the project in **ManiVault Studio** automatically.

*The user doesn’t need to know or care that the project was remote—it's seamless, see the teaser **GIF** at the top of this page for a preview of the experience.*

## Caveats & Notes
All downloadable files (**projects JSON** file and the project **.mv** files) must be a direct download link: The **URLs** must point directly to the raw file. Avoid links that:
- Require user login.
- Redirect to a download confirmation page; this is not guaranteed to work (e.g. **OSF**, **Google Drive**, and **Dropbox UI** pages).
- Ensure **HTTPS** download is enabled (HTTP is not allowed).
- Test everything: Always test your setup in a clean **ManiVault Studio** environment before sharing with users.
- Latency or failure fallback: If a project fails to download or is offline, it will not be shown. Ensure your hosting is reliable.

Make sure:
- To check the name of the required plugins; the name should be the same as the plugin **JSON** file. If they are not, the project will not be listed on the start page projects section.
- That the **projects JSON** file adheres to the [projects JSON schema](https://github.com/ManiVaultStudio/core/blob/master/ManiVault/res/json/projects.schema.json). If your projects do not appear on the start page, check the **ManiVault Studio** console output; it will give hints where the problem is located

