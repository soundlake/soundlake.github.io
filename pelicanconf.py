#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'soundlake'
SITENAME = u'soundlake'
SITEURL = 'https://soundlake.net'

PATH = 'content'

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com'),
         ('Python.org', 'http://python.org'),
         ('Jinja2', 'http://jinja.pocoo.org'),
         ('Markdown', 'https://daringfireball.net/projects/markdown'),
         ('Python-Markdown', 'https://python-markdown.github.io'),)

# Social widget
SOCIAL = (('github', 'https://github.com/soundlake'),
          ('stackoverflow', 'https://stackoverflow.com/users/4276533/soundlake'),
          ('soundcloud', 'https://soundcloud.com/soundlake'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
    'static',
]

EXTRA_PATH_METADATA = {
    'static/favicon.png': {'path': 'favicon.png'},
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
