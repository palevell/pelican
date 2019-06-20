#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR   = 'Patrick'
SITENAME = 'Pelican'
SITEURL  = ''  # 'https://palevell.github.io/pelican'
# THEME ='random_theme'
THEME = 'pelican-themes/Flex'
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
LINKS = (("People's Party of Canada", 'https://www.peoplespartyofcanada.ca/'),
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




