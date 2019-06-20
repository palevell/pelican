#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
# 2019-Jun-19 PAL - This is for testing pelican-themes
from random import choice
import os, sys
sys.path.append(os.curdir)
# 2019-Jun-19 PAL - Load pelican-themes list (for testing)
from themes import Themes

AUTHOR   = 'Patrick'
SITENAME = 'Pelican'
SITEURL  = ''  # 'https://palevell.github.io/pelican'
# 2019-Jun-19 PAL - Choose a random theme from pelican-themes, listed in Themes
TESTED_THEMES_FILENAME = 'tested_themes3.txt'
THEME = choice(Themes)
tested_themes = []
if os.path.exists(TESTED_THEMES_FILENAME):
    with open(TESTED_THEMES_FILENAME, 'rt') as f:
        for line in f.readlines():
            tested_themes.append(line.strip())
while THEME in tested_themes:
    THEME = choice(Themes)
with open(TESTED_THEMES_FILENAME, 'at') as f:
    f.write(THEME + os.linesep)
print("\n\tTheme: %s\n" % THEME)
# THEME ='pelican-themes/pelican-twitchy'
# BOOTSTRAP_THEME = ''  # 'united'
# PYGMENTS_STYLE = 'native'

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (("People's Party of Canada", 'https://peoplespartyofcanada.ca/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('@peoplespca', 'https://twitter.com/@peoplespca'),
          ('@MaximeBernier', 'https://twitter.com/@MaximeBernier'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Ref: https://pythonforundergradengineers.com/how-i-built-this-site-3.html
PLUGIN_PATHS = [ 'pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

## Theme-specific settings
## Pelican Twitchy
SITESUBTITLE = 'Site sub-title'
EXPAND_LATEST_ON_INDEX = True
SHARE = False
DISPLAY_TAGS_ON_MENU = False
COOKIE_CONSENT = True
TYPOGRIFY = True




