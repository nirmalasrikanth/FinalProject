from django.contrib.sitemaps import Sitemap
from .models import ItemBase
class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return ItemBase
    def lastmod(self, obj):
        return obj.updated