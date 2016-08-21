THEME = u'cleanliness'

AUTHOR = u'Chris Miller'
SITENAME = u'randomlyunique'
SITEURL = u'http://www.randomlyunique.com'

TIMEZONE = u'US/Pacific'

DEFAULT_LANG = u'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU = True

DEFAULT_PAGINATION = 5

RELATIVE_URLS = True

PATH = u'content'

STATIC_PATHS = [u'assets']

ARTICLE_URL = u'{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = u'{date:%Y}/{slug}/index.html'

PLUGIN_PATHS = ['cleanliness/plugins']
PLUGINS = []
