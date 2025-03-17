# docs/conf.py

import os
import sys

# -- Project information -----------------------------------------------------
project = "My Resume"
author = "Your Name"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"  # or "sphinx_rtd_theme"
html_static_path = ["_static"]
# docs/conf.py
html_static_path = ["_static"]

def setup(app):
    app.add_css_file("custom.css")
