#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = u'cleanliness'

AUTHOR = u'Chris Miller'
SITENAME = u'randomlyunique'
SITEURL = u'http://www.randomlyunique.com'

TIMEZONE = u'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU = True

# Social widget
SOCIAL = (
    (u'github-square', u'https://github.com/chrisvmiller'),
)

DEFAULT_PAGINATION = 5

RELATIVE_URLS = True

PATH = u'content'
# ARTICLE_EXCLUDES = (('pages'))

PROFILE_IMAGE_URL = u''
STATIC_PATHS = [u'assets']

ARTICLE_URL = u'{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = u'{date:%Y}/{slug}/index.html'
