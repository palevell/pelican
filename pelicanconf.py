#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Patrick'
SITENAME = 'Pelican'
SITEURL = 'https://palevell.github.io/pelican'
# THEME = '/home/patrick/src/pelican-themes/Just-Read'
# THEME = '/home/patrick/src/pelican-themes/pelican-cait'
# THEME = '/home/patrick/src/pelican-themes/bootstrap2-dark'
# THEME = 'notmyidea'

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