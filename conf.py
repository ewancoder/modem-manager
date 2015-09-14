# -*- coding: utf-8 -*-
import sys
import os
import shlex

# -- Localization --
locale_dirs = ['locale/']
gettext_compact = False
language = 'en'

# -- DYNAMIC configuration --
project = 'Modem Manager'
copyright = '2015, Technikon'
author = 'ewancoder'
version = '0.8'
release = '0.8'

todo_include_todos = False
stageblocks = ('')

# -- General configuration ------------------------------------------------
extensions = [ 
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig'
]
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = 'sphinx'

def setup(app):
    app.add_config_value('stageblocks', 0, True)

# -- Options for HTML output ----------------------------------------------
html_theme = 'theme'
html_theme_path = ['.']
html_static_path = ['_static']
html_show_sphinx = False
#html_show_copyright = True
#html_title = None
#html_short_title = None
html_logo = 'icon.ico'
html_favicon = 'icon.ico'
#html_last_updated_fmt = '%b %d, %Y'

# -- Options for LaTeX output ---------------------------------------------
latex_elements = {
#'pointsize': '10pt',

'preamble': '''
\usepackage{cmap}
\usepackage[T2A]{fontenc}
\usepackage[utf8]{inputenc}
'''
}

latex_documents = [
  ('index', 'ModemManager.tex', 'Modem Manager Documentation',
   'Technikon', 'report')
]

#latex_logo = None
#latex_use_parts = False
#latex_show_pagerefs = False
#latex_show_urls = False

# -- Options for manual page output ---------------------------------------
man_pages = [
    ('index', 'modemmanager', 'Modem Manager Documentation',
     [author], 1)
]
#man_show_urls = False
