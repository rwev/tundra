#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# PELICAN VARIABLES REFERENCED BY TEMPLATE

OWNER = ""
AUTHOR = ""

SITENAME = ""
SITEURL = "localhost:8000"

USER_LOGO_URL = ""
TAGLINE = ""

DISPLAY_LINKS_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_SOCIAL_ON_MENU = False

LINK_ITEMS = (
    # ("<TEXT>", "<URL>"),
)
SOCIAL = ()

# CONFIGURATIONS FOR PELICAN BUILD PROCESS

THEME = "tundra"
RELATIVE_URLS = True

# PLUGINS

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "autopages",
    "similar_posts",
    "neighbors",
    "more_categories",
    "photos",
    "summary",
    "clean_summary",
]

# autopages
AUTOPAGES_PATH = ""

AUTHOR_PAGE_PATH = ""
CATEGORY_PAGE_PATH = ""
TAG_PAGE_PATH = ""

# similar_posts
SIMILAR_POSTS_MAX_COUNT = 3

# photos
PHOTO_LIBRARY = ""

PHOTO_THUMB = (550, 550, 75)
PHOTO_SQUARE_THUMB = False

PHOTO_WATERMARK = False

PHOTO_EXIF_KEEP = False
PHOTO_EXIF_REMOVE_GPS = True
PHOTO_EXIF_COPYRIGHT = "CC-BY-NC-ND"
PHOTO_EXIF_COPYRIGHT_AUTHOR = ""

# summary
SUMMARY_MAX_LENGTH = 1000  # use whole summary
SUMMARY_USE_FIRST_PARAGRAPH = True

CLEAR_SUMMARY_MAXIMUM = 0
CLEAN_SUMMARY_MINIMUM_ONE = False

# CONFIGURATIONS FOR TUNDRA STATIC APPEARANCE (NOT USED BY PELICAN)

TUNDRA_SEPARATION_STR = " // "

TUNDRA_BLOG = "blog"
TUNDRA_LINKS = "links"
TUNDRA_SOCIAL = "social"

TUNDRA_HOME = "home"
TUNDRA_ARCHIVES = "archives"
TUNDRA_SIMILAR_ARTICLES = "similar articles"

TUNDRA_PAGES = "pages"

TUNDRA_AUTHOR = "author"
TUNDRA_AUTHORS = "authors"
TUNDRA_AUTHOR_S = "author(s)"

TUNDRA_CATEGORY = "category"
TUNDRA_CATEGORIES = "categories"

TUNDRA_ARTICLES = "articles"

TUNDRA_GALLERY = "gallery"

TUNDRA_TAG = "tag"
TUNDRA_TAGS = "tags"

TUNDRA_PREVIOUS = "prev"
TUNDRA_NEXT = "next"

TUNDRA_NEWER = "newer"
TUNDRA_OLDER = "older"

TUNDRA_POSTED = "posted"
TUNDRA_MODIFIED = "modified"

TUNDRA_ATOM = "atom"
TUNDRA_RSS = "rss"

# FORMATTING / FEED GENERATION

DEFAULT_DATE_FORMAT = "%Y.%m.%d %H:%M"  # big

TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

AUTHOR_FEED_ATOM = "feeds/author.{slug}.atom.xml"
AUTHOR_FEED_RSS = "feeds/author.{slug}.rss.xml"

TAG_FEED_ATOM = "feeds/tag.{slug}.atom.xml"
TAG_FEED_RSS = "feeds/tag.{slug}.rss.xml"

CATEGORY_FEED_ATOM = "feeds/category.{slug}.atom.xml"
CATEGORY_FEED_RSS = "feeds/category.{slug}.rss.xml"

DISPLAY_SUB_FEEDS = False # whether to display author, tag, and category feeds

FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS =  "feeds/all.rss.xml"
