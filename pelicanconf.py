THEME = u'cleanliness'

SITENAME = u'randomlyunique'
SITEURL = u'http://www.randomlyunique.com'

TIMEZONE = u'US/Pacific'
DEFAULT_LANG = u'en'

RELATIVE_URLS = True
FEED_MAX_ITEMS = 10

PATH = u'content'
STATIC_PATHS = [u'assets']

ARTICLE_URL = u'{category}/{date:%Y}/{slug}/index.html'
ARTICLE_SAVE_AS = u'{category}/{date:%Y}/{slug}/index.html'

DEFAULT_PAGINATION = False
AUTHOR_SAVE_AS = False
TAG_SAVE_AS = False

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DIRECT_TEMPLATES = ['index']

PLUGIN_PATHS = ['cleanliness/plugins']
PLUGINS = ['thumbnailer']

IMAGE_PATH = 'assets/'
THUMBNAIL_DIR = 'category/thumbnails'
