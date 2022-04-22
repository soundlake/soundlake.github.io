#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'soundlake'
SITENAME = u'soundlake'
SITEURL = 'https://soundlake.xyz'

PATH = 'content'

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
MENUITEMS = (('Blog', SITEURL),)
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com'),
         ('Python.org', 'http://python.org'),
         ('Jinja2', 'http://jinja.pocoo.org'),
         ('Markdown', 'https://daringfireball.net/projects/markdown'),
         ('Python-Markdown', 'https://python-markdown.github.io'),
         ('pelican-blue', 'https://github.com/Parbhat/pelican-blue'),
         ('source code', 'https://github.com/soundlake/soundlake.net'),)

# Social widget
SOCIAL = (('github', 'https://github.com/soundlake'),
          ('bitbucket', 'https://bitbucket.org/soundlake'),
          ('gitlab', 'https://gitlab.com/soundlake'),
          ('stack-overflow', 'https://stackoverflow.com/users/4276533/soundlake'),
          ('twitter', 'https://twitter.com/sound_lake'),
          ('tumblr', 'https://sound-lake.tumblr.com'),
          ('telegram', 'https://t.me/soundlake'),
          ('soundcloud', 'https://soundcloud.com/soundlake'),)

DEFAULT_PAGINATION = 5

STATIC_PATHS = [
    'static',
    'images',
]

EXTRA_PATH_METADATA = {
    'static/favicon.png': {'path': 'favicon.png'},
    'static/CNAME': {'path': 'CNAME'},
}

TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme - pelican-blue
THEME = 'themes/pelican-blue'

SIDEBAR_DIGEST = 'Developer / Programmer / Musician'
FAVICON = 'favicon.png'
TWITTER_USERNAME = 'sound_lake'

# URLs
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{lang}/{slug}.html'
ARTICLE_LANG_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{lang}/{slug}.html'
DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_LANG_URL = 'drafts/{lang}/{slug}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{lang}/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{lang}/{slug}.html'
PAGE_LANG_SAVE_AS = 'pages/{lang}/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}.html'
YEAR_ARCHIVE_URL = 'posts/{date:%Y}.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}.html'
MONTH_ARCHIVE_URL = 'posts/{date:%Y}/{date:%m}.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}.html'
DAY_ARCHIVE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}.html'
DAY_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}.html'
