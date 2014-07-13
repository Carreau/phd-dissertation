# -*- coding: utf-8 -*-
#
# Human Control of a Bicycle documentation build configuration file, created by
# sphinx-quickstart on Wed Sep 28 12:51:59 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo',
              'sphinx.ext.mathjax',
              'sphinxcontrib.bibtex',
              'sphinx.ext.numfig',
              ]

# numfig:
numfig_number_figures = True
numfig_figure_caption_prefix = "Figure"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

author_first = u'Matthias'
author_last= u'Bussonnier'
author_full = u' '.join([author_first,author_last])


# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Actin gel dynamics'
copyright = u'2014, '+author_full

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''
latex_elements = { 'releasename': '' }

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt =  '%B %d, %Y at %X %Z'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'tables', 'data', 'figures', 'src', 'todo.rst',
    'README.rst', 'index-latex.rst', 'parts/cells.rst', 'parts/roleofactin.rst']
if tags.has('latex') or tags.has('latex-web') or tags.has('latex-print'):
    exclude_patterns.remove('index-latex.rst')
    exclude_patterns.append('index.rst')
    exclude_patterns.append('zreferences.rst')

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# Shows all todo listings
todo_include_todos = True


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'haiku'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project + ':'+author_full

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'actingeldynamics'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'A4paper'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '11pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index-latex', 'actingeldynamics.tex', u'Actin Gels dynamics',
   author_full, 'manual', False),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = 'figures/bear-6in.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = True

# If true, show URL addresses after external links.
if tags.has('latex-print'):
    latex_show_urls = 'inline'
else:
    latex_show_urls = False

# Additional stuff for the LaTeX build.
preamble = \
"""
\\usepackage{pdfpages}
\\setcounter{tocdepth}{2}
% \\makeatletter
% \\def\\cleardoublepage{
% \\clearpage\\if@twoside \\ifodd\\c@page\\else
% \\hbox{}
% \\vspace*{\\fill}
% \\vspace{\\fill}
% \\thispagestyle{empty}
% \\newpage
% \\if@twocolumn\\hbox{}\\newpage\\fi\\fi\\fi
% }
% \\makeatother
"""
#if tags.has('latex-print'):
#    preamble += \
#"""
#\\definecolor{TitleColor}{rgb}{0,0,0}
#\\definecolor{InnerLinkColor}{rgb}{0,0,0}
#\\definecolor{OuterLinkColor}{rgb}{0,0,0.}
#"""

import codecs
# texts = ['abstract', 'foreword']
# tex = []
# for text in texts:
#     with open(text + '.rst') as f:
#         full = f.read()
#     if text == 'abstract':
#         rst = full.replace('========\nAbstract\n========\n\n', '')
#     elif text == 'foreword':
#         rst = full.replace('========\nForeword\n========\n\n', '')
#     else:
#         rst = full
#     with open(text + '-temp.rst', 'w') as f:
#         f.write(rst)
#     os.system('pandoc -o ' + text + '.tex ' + text + '-temp.rst')
#     os.remove(text + '-temp.rst')
#     with open(text + '.tex') as f:
#         tex.append(f.read())
#     os.remove(text + '.tex')
#
# This creates thw raw latex for the acknowledgements
# with open('acknowledgements.rst') as f:
#     acknowledgements = f.read().replace('=' * 16 + '\nAcknowledgements\n'
#         + '=' * 16 + '\n\n', '').replace(':cite:`Lange2011`',
#                 '[DL11]')
# with open('acknowledgements-temp.rst', 'w') as f:
#     f.write(acknowledgements)
# del acknowledgements
# os.system('pandoc -o acknowledgements.tex acknowledgements-temp.rst')
# os.remove('acknowledgements-temp.rst')
# with codecs.open('acknowledgements.tex', encoding='utf-8') as f:
#     acknowledgements = f.read()
# os.remove('acknowledgements.tex')

toc = \
r"""
% \\pagestyle{frontmatter}
% \\chapter*{Abstract}
% \\thispagestyle{frontmatter}
% %s
% \\chapter*{Foreword}
% \\thispagestyle{frontmatter}
% %s
% \\chapter*{Acknowledgements}
% \\thispagestyle{frontmatter}
% --s
\tableofcontents
% \\cleardoublepage
% \\pagestyle{frontmatter}
% \\addtocontents{toc}{\\protect\\thispagestyle{frontmatter}}
% \\listoffigures
% \\addtocontents{lof}{\\protect\\thispagestyle{frontmatter}}
% \\listoftables
% \\addtocontents{lot}{\\protect\\thispagestyle{frontmatter}}
\cleardoublepage
\pagestyle{normal}
\pagenumbering{arabic}
 """# % (tex[0], tex[1])

latex_elements = {'preamble': preamble,
                  'tableofcontents': toc}

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

