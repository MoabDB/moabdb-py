# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MoabDB'
copyright = '2022, MoabDB'
author = 'MoabDB'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon', 'm2r', 'sphinxawesome_theme', 'sphinx_favicon', 'sphinx_rtd_theme', 'pydata_sphinx_theme']
source_suffix = ['.rst']

templates_path = ['_templates']
exclude_patterns = []
highlight_language = 'python3'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_baseurl = 'https://docs.moabdb.com/'
html_static_path = ['_static']
html_css_files = ["custom.css"]
#html_logo = "_static/images/MoabDB.jpg"

# html_theme_options = {
#     "navbar_start": ["navbar-logo"],
#     "navbar_center": ["navbar-nav"],
#     "navbar_end": ["navbar-icon-links"],
#     "navbar_persistent": ["search-button"]
# }

# favicons = [
#     {
#         "rel": "icon",
#         "static-file": "favicons/favicon-32x32.png",
#         "type": "image/png",
#     },
#     {
#         "rel": "icon",
#         "sizes": "16x16",
#         'static-file': "favicons/favicon-16x16.png",
#         "type": "image/png",
#     },
#     {
#         "rel": "icon",
#         "sizes": "32x32",
#         "static-file": "favicons/favicon-32x32.png",
#         "type": "image/png",
#     },
#     {
#         "rel": "apple-touch-icon",
#         "sizes": "180x180",
#         "static-file": "favicons/apple-touch-icon.png",
#         "type": "image/png",
#     },
#     {
#         "rel": "android-chrome",
#         "sizes": "192x192",
#         "static-file": "favicons/android-chrome-192x192.png",
#         "type": "image/png",
#     },
#     {
#         "rel": "android-chrome",
#         "sizes": "512x512",
#         "static-file": "favicons/android-chrome-512x512.png",
#         "type": "image/png",
#     },
# ]
