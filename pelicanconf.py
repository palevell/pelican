#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

RANDOM_THEME = False

AUTHOR   = 'Patrick'
SITENAME = "Patrick's Place"
SITEURL  = '/'  # 'https://palevell.github.io/pelican'\
# SITESUBTITLE = 'Join us.'
SITELOGO = 'images/ppc-logo_180x.png'
SITELOGO_SIZE = 125
HIDE_SITENAME = True
FAVICON='extra/favicon.ico'
if not RANDOM_THEME:
    THEME = 'theme'  # 'pelican-themes/pelican-twitchy'
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
         ('Frank Vaughan III', 'http://frankvauhan.ca'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('@palevell', 'https://twitter.com/@palevell'),
          ('@PPC_Retweets', 'https://twitter.com/@PPC_Retweets'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Ref: https://pythonforundergradengineers.com/how-i-built-this-site-3.html
PLUGIN_PATHS = [ 'pelican-plugins', ]
PLUGINS = ['i18n_subsites', 'share_post', ]
"""PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img',
           'neighbors', 'render_math', 'related_posts', 'assets', 'share_post',
           'series']"""
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
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
EXPAND_LATEST_ON_INDEX = True
SHARE = True
DISPLAY_TAGS_ON_MENU = False
COOKIE_CONSENT = True
TYPOGRIFY = True
DISPLAY_RECENT_POSTS_ON_MENU = True
RECENT_POST_COUNT = 5




