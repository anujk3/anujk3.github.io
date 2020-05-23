#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

AUTHOR = "Anuj Katiyal"
SITENAME = "Essentials Blog"
SITESUBTITLE = "learnings along the journey called life, grateful everyday..."
SITEURL = ""

PATH = "content"

# Regional Settings
TIMEZONE = "America/New_York"
DATE_FORMATS = {"en": "%b %d, %Y"}


DEFAULT_LANG = "en"
DEFAULT_CATEGORY = "blog"
CLAIM_GOOGLE = "hx-CqBDqKh1MGFBW_c2UdmrFPisQq0_Qxqzxadi5hKY"
CLAIM_BING = "B0509443E2B44E9E8C4B4CED376C665F"

LANDING_PAGE_TITLE = "Data is all we need..."

PROJECTS_TITLE = "Essentials I write about..."
PROJECTS = [
    {
        "name": "Fitness Journey",
        "url": "http://localhost:8000/categories.html#python-ref",
        "description": "Garmin Analysis of fitness data",
    },
]

# Blogroll
LINKS = (
    ("Discord", "https://anujkatiyal.com"),
    ("Patreon", "https://anujkatiyal.com"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/anujkatiyal"),
    ("GitHub", "https://github.com/anujk3"),
    ("Twitter", "https://twitter.com/anujkatiyal"),
    ("StackOverflow", "http://stackoverflow.com/users/812950/anuj", "stack-overflow"),
)

TWITTER_USERNAME = "anujkatiyal"

# Update if you use amazon links
# AMAZON_ONELINK = ""

# GOOGLE_ANALYTICS tracking ID
GOOGLE_ANALYTICS = "UA-107297585-1"

## Configure if you use Disqus for comments
DISQUS_SITENAME = "anujkatiyal-com"
DISQUS_DISPLAY_COUNTS = True

# Extra files customization
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/robots.txt": {"path": "robots.txt"},
    "pdfs/AnujKatiyal_Resume.pdf": {"path": "AnujKatiyal_Resume.pdf"},
}
STATIC_PATHS = [
    "images",
    "codes",
    "figures",
    "notebooks",
    "extra/CNAME",
    "extra/robots.txt",
    "pdfs",
]

# Photo Gallery plugin
PHOTO_LIBRARY = "gallery-source/"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_SQUARE_THUMB = False
PHOTO_RESIZE_JOBS = 5
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = "© Anuj Katiyal (https://anujkatiyal.com)"
PHOTO_WATERMARK_IMG = ""
PHOTO_EXIF_KEEP = False
PHOTO_EXIF_REMOVE_GPS = True
PHOTO_EXIF_COPYRIGHT = "COPYRIGHT"
# PHOTO_EXIF_COPYRIGHT_AUTHOR = 'Your Name Here' (Defaults to Author)


# Put as draft content in the future
WITH_FUTURE_DATES = True

# Put full text in RSS feed
RSS_FEED_SUMMARY_ONLY = False

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = "feeds/all.atom.xml"
# FEED_ALL_RSS = "feeds/all.rss"
# CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
# CATEGORY_FEED_RSS = "feeds/{slug}.rss"
# TRANSLATION_FEED_ATOM = "feeds/{lang}.atom.xml"
# TRANSLATION_FEED_RSS = "feeds/{lang}.rss"
# AUTHOR_FEED_ATOM = "feeds/{slug}.atom.xml"
# AUTHOR_FEED_RSS = "feeds/{slug}.rss"
# TAG_FEED_ATOM = "feeds/tag_{slug}.atom.xml"
# TAG_FEED_RSS = "feeds/tag_{slug}.rss"

DISPLAY_PAGES_ON_MENU = True

# CACHE_CONTENT = False
# CACHE_PATH = ".cache"
# LOAD_CONTENT_CACHE = False

# Plugins
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "sitemap",
    "extract_toc",
    "tipue_search",
    "liquid_tags.img",
    "neighbors",
    "render_math",
    "related_posts",
    "share_post",
    "series",
    "assets",
    "post_stats",
    "photos",
    "liquid_tags.youtube",
    "liquid_tags.notebook",
    "liquid_tags.include_code",
]

THEME = "pelican-themes/elegant"

# elegant
TYPOGRIFY = True
RESPONSIVE_IMAGES = True

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight", "linenums": True},
        "markdown.extensions.extra": {},
        "markdown.extensions.toc": {"permalink": "true"},
        "markdown.extensions.meta": {},
        "markdown.extensions.admonition": {},
    },
    "output_format": "html5",
}

# for Tique Search Plugin
DIRECT_TEMPLATES = (
    "index",
    "tags",
    "categories",
    "authors",
    "archives",
    "search",
    "404",
)

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
SHARE_POST_INTRO = "Like this post? Share on:"
SHARE_LINKS = [("twitter", "Twitter"), ("facebook", "Facebook"), ("email", "Email")]
COMMENTS_INTRO = ""

FILENAME_METADATA = "(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)"
USE_FOLDER_AS_CATEGORY = False

SEARCH_BOX = False

# URL Settings to be compatible with octopress
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

ARTICLE_LANG_URL = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/"
ARTICLE_LANG_SAVE_AS = "blog/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/index.html"

YEAR_ARCHIVE_URL = "blog/archive/{date:%Y}/"
YEAR_ARCHIVE_SAVE_AS = "blog/archive/{date:%Y}/index.html"

MONTH_ARCHIVE_URL = "blog/archive/{date:%Y}/{date:%m}/"
MONTH_ARCHIVE_SAVE_AS = "blog/archive/{date:%Y}/{date:%m}/index.html"

CATEGORY_URL = "blog/category/{slug}/"
CATEGORY_SAVE_AS = "blog/category/{slug}/index.html"

TAG_URL = "blog/tag/{slug}/"
TAG_SAVE_AS = "blog/tag/{slug}/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

ARCHIVES_URL = "blog/archives/"
ARCHIVES_SAVE_AS = "blog/archives/index.html"

CATEGORIES_URL = "blog/categories/"
CATEGORIES_SAVE_AS = "blog/categories/index.html"

TAGS_URL = "blog/tags/"
TAGS_SAVE_AS = "blog/tags/index.html"

TAGS_URL = "tags"
TAGS_SAVE_AS = "tags/index.html"
AUTHORS_URL = "authors"
AUTHORS_SAVE_AS = "authors/index.html"
CATEGORIES_URL = "categories"
CATEGORIES_SAVE_AS = "categories/index.html"
ARCHIVES_URL = "archives"
ARCHIVES_SAVE_AS = "archives/index.html"

DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 0

PAGINATION_PATTERNS = (
    (1, "{base_name}/", "{base_name}/index.html"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

SITE_UPDATED = datetime.date.today()

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ("Tags", TAGS_URL, TAGS_SAVE_AS),
    ("Archives", ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

AUTHORS = {
    "Anuj Katiyal": {
        "url": "https://anujkatiyal.com/",
        "blurb": "Python, PySpark, SQL and everything big data...",
        "avatar": "/images/anujkatiyal.jpg",
    },
}
AUTHOR = "Anuj Katiyal"
