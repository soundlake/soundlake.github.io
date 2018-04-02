#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'soundlake'
SITENAME = u'soundlake'
SITEURL = ''

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
         ('Python-Markdown', 'https://python-markdown.github.io'),
         ('pelican-blue', 'https://github.com/Parbhat/pelican-blue'),)

# Social widget
SOCIAL = (('github', 'https://github.com/soundlake'),
          ('bitbucket', 'https://bitbucket.org/soundlake'),
          ('gitlab', 'https://gitlab.com/soundlake'),
          ('stack-overflow', 'https://stackoverflow.com/users/4276533/soundlake'),
          ('twitter', 'https://twitter.com/sound_lake'),
          ('soundcloud', 'https://soundcloud.com/soundlake'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
    'static',
]

EXTRA_PATH_METADATA = {
    'static/favicon.png': {'path': 'favicon.png'},
    'static/CNAME': {'path': 'CNAME'},
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme - pelican-blue
THEME = 'themes/pelican-blue'

SIDEBAR_DIGEST = 'Developer / Programmer / Musician'
FAVICON = 'favicon.png'
DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = 'sound_lake'
MENUITEMS = (('Blog', SITEURL),)
