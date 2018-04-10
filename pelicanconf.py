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
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/index.html'
DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'
DRAFT_LANG_URL = 'drafts/{slug}-{lang}/'
DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}/'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
YEAR_ARCHIVE_URL = 'posts/{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_URL = 'posts/{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/'
DAY_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/index.html'
