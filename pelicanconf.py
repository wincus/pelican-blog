#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'wincus'
SITENAME = u'Wincus Random Notes'
THEME='themes/pelican-sober'
DISPLAY_PAGES_ON_MENU = True
PELICAN_SOBER_STICKY_SIDEBAR = True

PATH = 'content'
TIMEZONE = 'America/Mendoza'
DEFAULT_LANG = u'en'
SITEURL = 'http://blog.wincus.com.ar'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('@jonwincus', 'https://twitter.com/jonwincus'),
          ('wincus', 'https://github.com/wincus'),
          ('jonwincus', 'https://ar.linkedin.com/in/jonwincus'),)

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

GOOGLE_ANALYTICS = 'UA-57105532-1'
