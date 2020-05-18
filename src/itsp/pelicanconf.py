#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'itsp'
SITENAME = 'itsp'
SITEURL = 'https://kirill-tsurkan.github.io/itsp/'

PATH = 'content'
OUTPUT_PATH = 'docs/'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

DISPLAY_CATEGORIES_ON_MENU = False

TIMEZONE = "Europe/Chisinau"

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Disable modules
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},}

DEFAULT_PAGINATION = False

LOAD_CONTENT_CACHE = False

THEME = 'themes/itsp'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
