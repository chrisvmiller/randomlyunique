THEME = u'cleanliness'

SITENAME = u'randomlyunique'
SITEURL = u'http://www.randomlyunique.com'

TIMEZONE = u'US/Pacific'
DEFAULT_LANG = u'en'

RELATIVE_URLS = True

PATH = u'content'

STATIC_PATHS = [u'assets']

ARTICLE_URL = u'{category}/{slug}/'
ARTICLE_SAVE_AS = u'{category}/{slug}/index.html'

DEFAULT_PAGINATION = False
AUTHOR_SAVE_AS = False
TAG_SAVE_AS = False

DIRECT_TEMPLATES = ['index']

PLUGIN_PATHS = ['cleanliness/plugins']
PLUGINS = []
