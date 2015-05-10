#/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jeremy Fried'
SITENAME = u'Music'
SITEURL = 'http://localhost:8000'
SITESUBTITLE = 'A musical journey'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME='pelican-themes/crowsfoot'
#BOOTSTRAP_THEME='flatly'
#BOOTSTRAP_NAVBAR_INVERSE = True
#PROFILE_IMAGE_URL='images/header.jpg'

PLUGIN_PATHS = ['pelican-plugins',]
PLUGINS = ['liquid_tags.youtube','pelican_youtube',]

#DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Francis (Band)', 'http://www.francisseattle.com'),)

# Social widget
TWITTER_ADDRESS = 'http://twitter.com/jcgerm'

GITHUB_ADDRESS = 'http://github.com/jcgerm'

EMAIL_ADDRESS = 'jcgerm@gmail.com'

SOUNDCLOUD = 'http://soundcloud.com/jcgerm'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
