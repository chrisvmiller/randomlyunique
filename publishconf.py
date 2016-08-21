import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = u'http://www.randomlyunique.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_MAX_ITEMS = 1

DELETE_OUTPUT_DIRECTORY = True