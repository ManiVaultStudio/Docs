# ManiVault Documentation

This repository contains the official documentation for **ManiVault** and related tooling. The documentation is published via [Read the Docs](https://about.readthedocs.com/) and built directly from the content in this repository.

The [Read the Docs](https://about.readthedocs.com/) documentation contains the following sections:
- **User Guide**  
  Contains onboarding information and tutorials  
  *Primarily written for end users*
- **Development**  
  Documents how to extend ManiVault with new plugins and how to create bespoke applications built on ManiVault  
  *This section is geared towards Plugin developers and application designers*
- **Reference**  
  Contains a curated doxygen reference (for plugin and core developers)
  List of all release notes (intended for all users)

---

## Documentation Structure

The documentation is written primarily in **Markdown** and organized by topic. The directory structure mirrors what is rendered on Read the Docs.

Typical layout:
```
Docs/
├── docs/
│   ├── source/          # Published documentation content
│   │   ├── index.md     # Root documentation entry point
│   │   ├── user_guide/
│   │   ├── development/
│   │   ├── api/
│   │   └── release_notes/
│   ├── Doxyfile         # Doxygen configuration for the API XML
│   ├── Makefile
│   ├── make.bat
│   └── requirements.txt
├── external/core/       # Pinned ManiVault Core submodule
├── .readthedocs.yaml    # Read the Docs build configuration
└── README.md
```

> **Note:** The Sphinx source directory is `docs/source/`. Other files under `docs/` support the build but are not documentation pages.

---

<details>

<summary><strong>Modifying the Documentation (Read the Docs)</strong></summary>

### 1. Edit or add Markdown files

All published documentation content lives under the `docs/source/` directory.

- Modify existing pages by editing their **.md** files
- Add new pages by creating new **.md** files in the appropriate subdirectory

Example:
```
docs/source/user_guide/tutorials/my-new-tutorial.md
```

---

### 2. Register new pages in the table of contents

Read the Docs uses [Sphinx](https://www.sphinx-doc.org/en/master/) to build the site. For a page to appear in navigation, it must be referenced in a **toctree**.

Edit the relevant index file, for example:
    
    ```{toctree}
    :maxdepth: 2

    installation
    tutorials/my-new-tutorial
    reference/api
    ```

If a page is not listed in a **toctree**, it will **not appear** in the rendered documentation.

---

### 3. Preview the documentation locally (recommended)

Before submitting a pull request, contributors are encouraged to build the documentation locally.

#### Install dependencies

Read the Docs builds with Python 3.11. From the repository root, install the same Python dependencies locally:

```bash
python -m pip install -r docs/requirements.txt
```

#### Prepare the API reference

Sphinx requires pre-built Doxygen XML in `docs/_doxygen/xml`. Download the same archive used by Read the Docs:

```bash
mkdir -p docs/_doxygen
curl -L -o doxygen-xml.tar.gz https://github.com/ManiVaultStudio/Docs/releases/download/doxygen-xml-latest/doxygen-xml.tar.gz
tar -xzf doxygen-xml.tar.gz -C docs/_doxygen
rm doxygen-xml.tar.gz
```

Alternatively, initialize the pinned Core submodule and generate the XML locally (requires Doxygen):

```bash
git submodule update --init external/core
doxygen docs/Doxyfile
```

Both methods must produce `docs/_doxygen/xml/index.xml` before Sphinx is run.

#### Build the documentation
From the repository root:

```bash
sphinx-build -b html docs/source docs/build/html
```

Alternatively, run `make html` from `docs/` on Linux or macOS, or `docs\make.bat html` from the repository root on Windows.

Open the generated documentation:
```
docs/build/html/index.html
```

This preview closely matches what the [ManiVault Read the Docs](https://manivault.readthedocs.io/en/latest/) will look like.
  
---

### 4. Read the Docs build configuration

The Read the Docs build is configured in:
```
.readthedocs.yaml
```

Important notes:
- Builds are triggered automatically on pushes and pull requests
- The default branch is used for the published documentation
- The hosted build downloads the latest published Doxygen XML archive before running Sphinx

</details>

---

## Doxygen
Our curated API documentation is based on Doxygen. During the Read the Docs build process, pre-built Doxygen XML is downloaded from [releases](https://github.com/ManiVaultStudio/Docs/releases/tag/doxygen-xml-latest) to expedite the process. The latest development artifact is generated daily with [this](https://github.com/ManiVaultStudio/Docs/blob/main/.github/workflows/update-doxygen-xml.yml) GitHub action. A versioned Docs tag also publishes a matching, immutable `doxygen-xml-<version>` artifact from its pinned Core submodule so that released documentation does not drift with Core development.

## Release notes
A curated list of release notes is generated daily using [this](https://github.com/ManiVaultStudio/Docs/blob/main/.github/workflows/synchronize-release-notes.yml) GitHub action.

## Code Blocks and Examples

This documentation contains code snippets and example code intended for reuse.

- **All code snippets are licensed under the MIT License**
- Snippets may be copied into open-source or commercial projects without restriction

Larger examples may include an explicit SPDX identifier:
```cpp
// SPDX-License-Identifier: MIT
```

<details>

<summary><strong>Contributing</strong></summary>  

#### Content
Contributions are welcome and appreciated, including:
- Fixing typos or inaccuracies
- Improving clarity and explanations
- Adding tutorials, guides, or reference material

#### Contribution workflow
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Build the documentation locally to verify correctness
5. Submit a pull request

</details>

<details>

<summary><strong>License</strong></summary>  

#### Documentation text
All documentation text is dual-licensed under **either**:
- **Creative Commons Attribution 4.0 International (CC BY 4.0)**, or
- **MIT License**

You may choose either license.

#### Code snippets
All code snippets and example code are licensed under the **MIT License** only.

#### Contributions
By contributing to this repository, you agree that your contributions are licensed under:
- **CC BY 4.0 OR MIT** (documentation text)
- **MIT License** (code snippets)

See the **LICENSE** file for full license texts and details.
</details>

## Links

- Documentation (Read the Docs): https://manivault.readthedocs.io/en/latest/
- ManiVault main repository: https://github.com/ManiVaultStudio/core
