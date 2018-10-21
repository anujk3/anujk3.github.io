#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *


SITEURL = 'http://anujkatiyal.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

SOCIAL = SOCIAL + (('rss', SITEURL + '/' + FEED_ALL_ATOM),)

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "anujkatiyal-com"
GOOGLE_ANALYTICS = "UA-107297585-1"
ADDTHIS_PROFILE = "ra-59d191ede9dfe49b"

SEARCH_URL = '/search'
