# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "C.C.K's Practice repository"
copyright = '2023, Kallen Ceryeei Celeste'
author = 'Kallen Ceryeei Celeste'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'myst_parser',
]

root_doc = 'README'
templates_path = ['_templates']
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.venv', '**/doc', '**/doc',]
include_patterns = ['**README.*', '**readme.*']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for TO-DO extension ---------------------------------------------
todo_include_todos = True
