# Splash screen customization

The ManiVault Studio splash screen is implemented as **HTML**, which makes it easy to change the look and feel of your application without recompiling.

By default, most applications use a standard splash screen template provided by the core:

```text
ManiVault/res/html/SplashScreenTemplate.html
```

You can use this file as a reference when designing your own splash screen.

> **Note**  
> The **customization directory** location can differ per platform or application bundle layout.  
> If you are unsure where it is, query it from C++ using From C++ code, you can query this location via [mv::util::StandardPaths::getCustomizationDirectory()](https://github.com/ManiVaultStudio/core/blob/master/ManiVault/src/util/StandardPaths.h).

---

## Predefined variables

Inside the splash screen HTML, you can use special placeholders in **double curly braces**. These are predefined by the core and substituted at runtime:

- `{{BACKGROUND_IMAGE}}`  
  Replaced by a Qt resource URL for the background image.

- `{{LOGO}}`  
  Replaced by the application logo image.

- `{{TITLE}}`  
  The application title.

- `{{VERSION}}`  
  The application version.

- `{{SUBTITLE}}`  
  The application subtitle.

- `{{DESCRIPTION}}`  
  The application description.

- `{{ALERTS}}`  
  Replaced with loading/system errors and warnings.

- `{{COPYRIGHT}}`  
  The copyright notice.

You can place these variables anywhere in your HTML where text or images would normally go (e.g., titles, subtitles, hero area, footer).

In addition, you can load **images and other static resources** (such as background images, icons, or custom CSS/JS files) from the application’s `assets` folder inside the customization directory.

---

## Base HTML template

A minimal splash screen template that works with ManiVault looks like this:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Splash Screen</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="Content-Security-Policy"
          content="default-src 'self' qrc:;
                   script-src  'self' 'unsafe-inline' qrc:;
                   style-src   'self' 'unsafe-inline';
                   font-src    'self' data: qrc:;
                   img-src     'self' data: custom-assets:;">
    <link rel="preload" href="qrc:/webfonts/fa-solid-900.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="qrc:/webfonts/fa-regular-400.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="qrc:/webfonts/fa-brands-400.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="qrc:/webfonts/all.min.css">
    <style>
      html, body { height: 100%; margin: 0; }

      body {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        font-family: system-ui, sans-serif;
      }

      #progress {
        position: fixed;
        left: 0; right: 0; bottom: 0;
        display: flex;
        align-items: center;
        padding: 4px 8px;
        padding-right: 20px;
        gap: 8px;
        height: 24px;
        background: rgb(70, 70, 70);
        font-size: 12px;
        z-index: 99999;
      }

      #progress #description {
        flex: 1;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        color: rgb(220, 220, 220);
        padding-left: 5px;
      }

      #progress #bar-container {
        flex: 0 0 150px;
        height: 4px;
        background: #ddd;
        border-radius: 2px;
        overflow: hidden;
      }

      #progress #bar-container #bar {
        width: 0px;
        height: 100%;
        background: #3b82f6;
        transition: width .2s linear, transform .2s linear;
        will-change: transform;
      }
    </style>
  </head>
  <body>
    <div class="content">
      <!--
        Place your custom layout here, for example:

        <div class="hero" style="background-image: url('{{BACKGROUND_IMAGE}}')">
          <img src="{{LOGO}}" alt="Logo">
          <h1>{{TITLE}}</h1>
          <p class="subtitle">{{SUBTITLE}}</p>
          <p class="description">{{DESCRIPTION}}</p>
          <div class="alerts">{{ALERTS}}</div>
          <footer>{{COPYRIGHT}}</footer>
        </div>
      -->
      <div id="progress">
        <div id="description"></div>
        <div id="bar-container">
          <div id="bar"></div>
        </div>
      </div>
    </div>

    <script src="qrc:/qtwebchannel/qwebchannel.js"></script>
    <script>
      function setProgress(p) {
        document.getElementById('bar').style.width = ((p / 100.0) * 150) + 'px';
      }

      function setProgressDescription(progressDescription) {
        document.getElementById('description').textContent = progressDescription;
      }

      new QWebChannel(qt.webChannelTransport, function (channel) {
        const bridge = channel.objects.bridge;

        bridge.progressChanged.connect(setProgress);
        bridge.progressDescriptionChanged.connect(setProgressDescription);

        if (bridge.requestInitial)
          bridge.requestInitial();
      });
    </script>
  </body>
</html>
```

You are free to change the HTML and CSS inside `<body>` (and add your own styles), as long as:

- The **Content-Security-Policy** remains compatible with what you want to load.
- The `qwebchannel.js` script and the progress bar wiring are kept if you still want to show loading progress.

---

## Creating a custom splash screen

To create your own splash screen:

1. **Enable custom splash screen in the app**
   - In the customization UI (opened with `Ctrl + F8`), go to **Branding**.
   - Enable the **custom splash screen** toggle.

2. **Locate the customization directory**
   - By default, many apps use:
     ```text
     <app_dir>/Customization
     ```
   - The exact location, however, may differ between platforms and application bundles.
   - If you are unsure, query the path in C++ using:
     ```cpp
     mv::util::StandardPaths::getCustomizationDirectory()
     ```

3. **Create the HTML file**
   - Inside the customization directory, create (or open) the `assets` folder:
     ```text
     <customization_dir>/assets
     ```
   - Create a file named:
     ```text
     SplashScreen.html
     ```

4. **Copy the base template**
   - Copy the base HTML shown above into `SplashScreen.html`.
   - Or, copy the built-in template from  
     `ManiVault/res/html/SplashScreenTemplate.html`  
     and adapt it to your needs.

5. **Add images and other resources**
   - Place any custom images, icons, or other static resources in:
     ```text
     <customization_dir>/assets
     ```
   - From your `SplashScreen.html`, you can reference these resources using the mechanisms supported by your application (for example, via the `custom-assets:` URL scheme, or other paths configured by the core).

6. **Customize the content**
   - Add your own layout, branding, and styling.
   - Insert the predefined variables wherever needed, for example:
     ```html
     <h1>{{TITLE}}</h1>
     <p class="subtitle">{{SUBTITLE}}</p>
     <p class="version">{{VERSION}}</p>
     <div class="alerts">{{ALERTS}}</div>
     <footer>{{COPYRIGHT}}</footer>
     ```
   - Use `{{BACKGROUND_IMAGE}}` and `{{LOGO}}` for images supplied by the application.
   - Combine those with additional images from the `assets` directory for fully customized branding.

7. **Save and restart**
   - Save `SplashScreen.html`.
   - Restart the application.
   - The app will now load your custom splash screen from the customization directory instead of the built-in one.

---

With this setup, you can fully control the splash screen’s layout and styling, while still benefiting from dynamic information (title, version, alerts, etc.) supplied by the ManiVault core, and from custom images and other resources stored in your `assets` folder.
