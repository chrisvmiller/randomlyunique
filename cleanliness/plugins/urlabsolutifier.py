"""URL Absolutifier Pelican Plugin

This uses monkey patching to make feedgenerator writing out absolute URLs in
anchor and image tags.

"""

from pelican import signals
import re
import urlparse

def monkey_patch_feedgenerator(sender):
    def add_item(self, title, link, description, *args, **kwargs):
        for regexp in regexps:
            description = regexp.sub(replace_url, description)
        return old_func(self, title, link, description, *args, **kwargs)

    def replace_url(match):
        url = match.group(2)
        if not urlparse.urlparse(url).scheme:
            url = urlparse.urljoin(site_url, url)
            return '<{}="{}"'.format(match.group(1), url)
        return match.group(0)

    import feedgenerator
    site_url = sender.settings.get('SITEURL')
    if site_url:
        regexps = [
            re.compile(r'<(a [^>]*href)=[\'"](.*?)[\'"]'),
            re.compile(r'<(img [^>]*src)=[\'"](.*?)[\'"]'),
        ]
        old_func = feedgenerator.SyndicationFeed.add_item
        feedgenerator.SyndicationFeed.add_item = add_item


def register():
    signals.initialized.connect(monkey_patch_feedgenerator)
