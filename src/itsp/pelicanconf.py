#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    from conf.env_conf import PROJECT_ENV
except ImportError:
    print(f"{bcolors.FAIL}ERROR: environment settings can not be found. Check readme.md file for set up process{bcolors.ENDC}")


if PROJECT_ENV == 'dev':
    try:
        from conf.dev_conf import *
        print(f"{bcolors.OKBLUE}INFO: running using dev settings{bcolors.ENDC}")
    except ImportError:
        print(f"{bcolors.FAIL}Environment settings for local development can not be found. Check readme.md file for set up process{bcolors.ENDC}")

elif PROJECT_ENV == 'test':
    try:
        from conf.test_conf import *
        print(f"{bcolors.OKBLUE}INFO: running using test settings{bcolors.ENDC}")
    except ImportError:
        print(f"{bcolors.FAIL}ERROR: Environment settings for production can not be found. Check readme.md file for set up process{bcolors.ENDC}")

elif PROJECT_ENV == 'prod':
    try:
        from conf.prod_conf import *
        print(f"{bcolors.OKBLUE}INFO: running using production settings{bcolors.ENDC}")
    except ImportError:
        print(f"{bcolors.FAIL}ERROR: Environment settings for production can not be found. Check readme.md file for set up process{bcolors.ENDC}")

from datetime import date
CURRENTYEAR = date.today().year
AUTHOR = 'itsp'
SITENAME = 'itsp'
PATH = 'content'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_LANG = 'ru'

LANGUAGES = {
    'ru': 'Русский',
    'en': 'English',
    'ro': 'Română'
}

PLUGIN_PATHS = ['./pelican-plugins']

PLUGINS = ['i18n_subsites']

I18N_SUBSITES = {

    'en': {
        'SITENAME': 'itsp',
    },
    'ro': {
        'SITENAME': 'itsp',
    }
}

JINJA_ENVIRONMENT = {
  'extensions': ['jinja2.ext.i18n']
}

def get_current_lang(gen):
    seq = list(gen)
    return DEFAULT_LANG if len(seq) == 0 else seq[0].lang

JINJA_FILTERS = {
    "get_current_lang": get_current_lang
}

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
