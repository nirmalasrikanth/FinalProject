from django.contrib.sitemaps import Sitemap
from .models import Course
class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return Course
    def lastmod(self, obj):
        return obj.updated