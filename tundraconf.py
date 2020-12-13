#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# PELICAN VARIABLES REFERENCED BY TEMPLATE

OWNER = ""
AUTHOR = ""

SITENAME = ""
SITEURL = "localhost:8000"

SOURCE_CODE_URL = ""

USER_LOGO_URL = ""
TAGLINE = ""

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

LINK_ITEMS = (
    # ("<LABEL>", "<LINK_TEXT>", "<URL>"),
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
    "summary"
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

PHOTO_SQUARE_THUMB = True
PHOTO_RESIZE_JOBS = 5
PHOTO_WATERMARK = False

PHOTO_EXIF_KEEP = False
PHOTO_EXIF_REMOVE_GPS = True

PHOTO_EXIF_COPYRIGHT = "CC-BY-NC-ND"
PHOTO_EXIF_COPYRIGHT_AUTHOR = ""

# summary
SUMMARY_USE_FIRST_PARAGRAPH = True

# scripts
# GOATCOUNTER_URL = 'https://rwev.goatcounter.com/count'
GOATCOUNTER_URL = ''

# CONFIGURATIONS FOR TUNDRA STATIC APPEARANCE (NOT USED BY PELICAN)

TUNDRA_SEPARATION_STR = " // "

TUNDRA_SOCIAL = "social"

TUNDRA_HOME = "home"

TUNDRA_BLOG = "blog"
TUNDRA_PAGES = "pages"
TUNDRA_LINKS = "links"

TUNDRA_ARCHIVES = "archives"
TUNDRA_SIMILAR_ARTICLES = "similar articles"

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
