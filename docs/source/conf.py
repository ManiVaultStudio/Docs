# Configuration file for the Sphinx documentation builder.

# -- Project information

import os


project = 'ManiVault'
copyright = '2026, BioVault'
author = 'BioVault'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
    'breathe',
    'exhale'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = [
    'colon_fence',   # useful for admonitions in Markdown
    'deflist',       # definition lists
    'linkify',       # auto-links plain URLs
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

HERE = os.path.dirname(__file__)                 # .../docs/source
DOCS_DIR = os.path.abspath(os.path.join(HERE, ".."))  # .../docs
DOXYGEN_XML_DIR = os.path.join(DOCS_DIR, "_doxygen", "xml")

breathe_projects = {"ManiVault": DOXYGEN_XML_DIR}
breathe_default_project = "ManiVault"

exhale_args = {
    "containmentFolder": "./api",
    "rootFileName": "library_root.rst",
    "rootFileTitle": "API Reference",
    "doxygenXmlDirectory": DOXYGEN_XML_DIR,
    "exhaleExecutesDoxygen": False,
}