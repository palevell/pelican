#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

RANDOM_THEME = False

AUTHOR   = 'Patrick'
SITENAME = "Patrick's Place"
SITEURL  = ''  # 'https://palevell.github.io/pelican'\
if not RANDOM_THEME:
    THEME = 'pelican-themes/pelican-twitchy'
else:
    THEME ='random_theme'
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

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Ref: https://matthewdevaney.com/posts/2019/03/04/build-a-blog-with-pelican-and-python-pt-1-installation-theme/
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
# SITESUBTITLE = 'Join us.'
EXPAND_LATEST_ON_INDEX = True
SHARE = False
DISPLAY_TAGS_ON_MENU = False
COOKIE_CONSENT = True
TYPOGRIFY = True

## Flex
SITELOGO = 'images/ppc-logo_180x.png'
SITELOGO_SIZE = 45

# uikit
"""DISPLAY_TAGS_ON_SIDEBAR_LIMIT = 10
DISPLAY_LINKS_ON_SIDEBAR_LIMIT = 10
LICENSE = ''"""

# BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'



