# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'pyranges'
copyright = '2020, Endre Bakken Stovner'
author = 'Endre Bakken Stovner'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.napoleon',
    "sphinx.ext.autodoc",
    "autoapi.extension",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest"
]

autoapi_dirs = ["../../pyranges/"]

autoapi_ignore = ["*flycheck*", "*#*", "*pyranges/methods/*py"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["pyranges/pyranges.py"]

autodoc_member_order = "alphabetical"

doctest_global_setup = """
import numpy as np
np.random.seed(0)
import pyranges as pr
import pandas as pd
"""

collect_ignore = ["pyranges/__init__.py"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# pip install git+https://github.com/pandas-dev/pandas-sphinx-theme.git@master
# html_theme = 'pandas_sphinx_theme'
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    'page_width': 'auto',
    'body_max_width': 'auto'
}
# page_width = 1200