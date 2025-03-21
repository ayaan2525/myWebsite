import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project Information

project = 'Ayaan Ahmad Siddiqui'
author = 'Ayaan Ahmad Siddiqui'
release = '0.1'

extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon',
        'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'
html_static_path = ['_static']

html_theme_options = {
    "light_css_variables": {
        "color-band-primary": "#0A8FDC",
        "color-band-contant": "#0A8FDC",
    },
}
