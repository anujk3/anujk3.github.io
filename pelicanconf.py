#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

#################### SITE SETTINGS #######################

AUTHOR = 'Anuj Katiyal'
SITENAME = 'Solarized Mode ON'
SITEURL = 'http://localhost:8000'
HIDE_SITENAME = False

################### DEVELOPMENT SETTINGS #################

RELATIVE_URLS = False   # when deploying site
#RELATIVE_URLS = True    # developing site

# when changing settings set this to false
LOAD_CONTENT_CACHE = False

################## PELICAN SETTINGS #####################

DISPLAY_PAGES_ON_MENU = True
TAG_CLOUD_STEPS = 7
TAG_CLOUD_MAX_ITEMS = 15
DISPLAY_ARTICLE_INFO_ON_INDEX = True
PATH = 'content'
STATIC_PATHS = ['images', 'codes', 'figures', 'notebooks', 'extra/CNAME', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        'extra/robots.txt': {'path': 'robots.txt'},
}
#PAGE_PATHS = ['notebooks']
#ARTICLE_PATHS = ['notebooks']
NOTEBOOK_DIR = 'notebooks'
#ARTICLE_PATHS = ['content']
USE_FOLDER_AS_CATEGORY = False
THEME = "./pelican-bootstrap3" # 'notmyidea'
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# ipynb settings
IPYNB_USE_META_SUMMARY = True
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'i18n_subsites', 'liquid_tags.video', 'liquid_tags.img',
        'liquid_tags.youtube', 'liquid_tags.vimeo', 'liquid_tags.include_code',
        'tipue_search', 'tag_cloud']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
MARKDOWN = {
  'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.headerid': {},
  },
  'output_format': 'html5',
}

SUMMARY_MAX_LENGTH = 200

################# BOOTSTRAP SETTINGS ###########################
BANNER = 'images/datascience.jpg'
#SITELOGO = 'images/earth.png'
#SITELOGO_SIZE = 40
FAVICON = 'images/favicon.ico'

BANNER_SUBTITLE = 'Blog about my Data Science learnings, Python and Data Viz'
SHOW_ARTICLE_AUTHOR = True
SHOW_DATE_MODIFIED = True
BOOTSTRAP_FLUID = False   # set as false if you want a fixed width
BANNER_ALL_PAGES = False

DEFAULT_PAGINATION = 6   #10
DISPLAY_BREADCRUMBS = False
DISPLAY_TAGS_ON_SIDEBAR = True
HIDE_SIDEBAR  = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 5
PYGMENTS_STYLE = "solarizedlight"

BOOTSTRAP_THEME = 'journal' #'simplex'# 'cosmo' # 'readable'
BOOTSTRAP_NAVBAR_INVERSE = False

#AVATAR = 'images/me.png'
#ABOUT_ME = 'Here I am!'

GITHUB_USER = 'anujk3'
GITHUB_SKIP_FORK = True

TWITTER_USERNAME = "anujkatiyal"

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

EMAIL = 'anujk3@gmail.com'

TIMEZONE = 'America/New_York'
DATE_FORMATS = {'en': '%Y-%m-%d'}
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/anujkatiyal'),
          ('GitHub', 'https://github.com/anujk3'),
          ('Twitter', 'https://twitter.com/anujkatiyal'),
	  ('StackOverflow','http://stackoverflow.com/users/812950/anuj','stack-overflow'),)

# FB Open Graph and Twitter
USE_OPEN_GRAPH = True
OPEN_GRAPH_FB_APP_ID = '133931710670837'
OPEN_GRAPH_IMAGE = 'images/anujkatiyal.jpg'
TWITTER_CARDS = True

CC_LICENSE = "CC-BY-NC-SA"


DISQUS_SITENAME = 'anujkatiyal-com'
ADDTHIS_PROFILE = 'ra-59d18c8fa90b4cec'

