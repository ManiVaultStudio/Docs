Make your plugin even more useful by exposing remote tutorials directly from the **ManiVault Studio** start page.

<img src="https://github.com/user-attachments/assets/4f9b0de9-c927-41e6-b560-93268356addd" alt="TutorialTeaser" width="500">  

*A preview of what the user will experience when remote tutorials are configured correctly.*

---

## Purpose  
This guide explains how plugin developers can make their **ManiVault Studio** tutorials available remotely. These tutorials will show up on the **ManiVault Studio** start page, making them easily discoverable and instantly accessible by users. They will also be available from the corresponding plugin **learning center**, the **global learning center**, and from the main menu:
<img src="https://github.com/user-attachments/assets/538e485e-1f3b-4492-be1a-2d70819bfc96" alt="Tutorial Launch" width="500">  

---

## Step-by-Step Instructions

### 1. Host Projects Online (optional) 
If you plan to accompany tutorials with example projects, you must place one or more projects on a web server or any web-accessible location. **ManiVault Studio** will download these projects if tutorials come with projects. These projects could be uploaded to:
- an institutional server,
- a file hosting service,
- or any location **ManiVault Studio** can reach via **HTTP/HTTPS**.

### 2. Create a Tutorials JSON File  
The plugin developer must create a **JSON** file describing the tutorials they want to expose to **ManiVault Studio** users. This file must conform to the [tutorials JSON schema](https://github.com/ManiVaultStudio/core/blob/master/ManiVault/res/json/tutorials.schema.json). Each tutorial entry in the JSON can include information about the tutorial and optionally a project download link.

Each entry describes one project and should include:
- `title`, the tutorial title.
- `project`, link to optional project file.
- `summary`, tutorial description (**HTML** is allowed).
- `fullPost`, the tutorial **HTML** content.
- `plugins` list (if any plugin is not available on the user end, the tutorial project will not be able to load, see the [Caveats and notes](#Caveats--Notes) section for more info).
- `tags`, additional tags (add the `GettingStarted` for the tutorial to show on the start page).
- `date`, the date the tutorial was published.
- `minimum-version-major`, the major part of the minimum `ManiVault Studio` version.
- `minimum-version-minor`, the minor part of the minimum `ManiVault Studio` version.

For example:
```json
{
  "tutorials":
  [
    {
      "title":"Example tutorial",
      "tags":["ExampleA", "Example B"],
      "date":"2024-11-20 12:00:00 +0000",
      "icon":"plug",
      "summary":"Explains how to work with the examples.",
      "fullpost":"<p>This how remote tutorials work</p>",
      "url":"https://www.manivault.studio/tutorials/data-hierachy-plugin/",
      "project":"https://example.com/tutorial-project.mv",
      "minimum-version-major":1,
      "minimum-version-minor":2,
      "plugins":["Example Plugin"]
    }
  ]
}
```
*You can find other **ManiVault Studio** **JSON schemas** [here](https://github.com/ManiVaultStudio/core/blob/master/ManiVault/res/json/).*

### 3. Upload the JSON File  
   Once ready, upload the tutorials JSON file to a web server so ManiVault Studio can locate and download it.

### 4. Register the JSON URL in Your Plugin
In your plugin factory (either in `mv::PluginFactory::PluginFactory()` or `mv::PluginFactory::initialize()`), register the **JSON**'s URL with:

```cpp
mv::PluginFactory::getTutorialsDsnsAction().addString("https://example.com/my_plugin_tutorials.json");
```

## Summary: Registering Remote Tutorials in ManiVault Studio

| Step | Action                                                                          |
|------|----------------------------------------------------------------------------------|
| 1    | Upload your tutorial project file(s) somewhere downloadable (optional)                               |
| 2    | Create a **tutorials JSON** file conforming to the [tutorials](https://github.com/ManiVaultStudio/core/blob/master/ManiVault/res/json/tutorials.schema.json) schema                    |
| 3    | Host the **tutorials JSON** file online                                                       |
| 4    | Register the **tutorials JSON** file in your plugin via `mv::PluginFactory::getTutorialsDsnsAction().addString("https://example.com/tutorials.json")` |
| 5    | Users will see the tutorial(s) on the start page and can click to download + open   |

## What Happens in ManiVault Studio
When everything is set up:
- The remote tutorials you defined will appear under the **Tutorials** section of the start page, clearly labeled and searchable.
- Users can filter remote tutorials based on **name**, **version**, and **tags**.
- A single click on a listed tutorial:
  - Opens an empty project and adds a tutorial plugin with the content.
  - Or downloads the tutorial project **.mv** file.

*The user doesn’t need to know or care that the tutorial (and its project) was remote—it's seamless, see the teaser **GIF** at the top of this page for a preview of the experience.*

## Caveats & Notes
All downloadable files (**tutorials JSON** file and the project **.mv** files) must be a direct download link: The **URLs** must point directly to the raw file. Avoid links that:
- Require user login.
- Redirect to a download confirmation page; this is not guaranteed to work (e.g., **OSF**, **Google Drive**, and **Dropbox UI** pages).
- Use **HTTPS** whenever possible: This avoids security warnings or failed downloads in corporate/firewalled environments.
- Test everything: Always test your setup in a clean **ManiVault Studio** environment before sharing with users.
- Latency or failure fallback: If a tutorial and/or its associated project fails to download or is offline, it will not be shown. Ensure your hosting is reliable.

~~Make sure:~~
~~- To check the names of the plugins; the name should be the same as in the plugin **JSON** file. If they are not, the tutorial will not be listed on the start page tutorials section.~~
~~- That the **tutorials JSON** file adheres to the [tutorials JSON schema](https://github.com/ManiVaultStudio/core/blob/master/ManiVault/res/json/tutorials.schema.json). If your tutorials do not appear on the start page, check the **ManiVault Studio** console output; it will give hints where the problem is located~~

