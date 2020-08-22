from django.contrib.sitemaps import Sitemap
from .models import Post
from django.shortcuts import reverse


class PostSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8

    def items(self):
        return Post.objects.filter(active=True)

    def lastmod(self, obj):
        return obj.post_update




class StaticViewSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8
    def items(self):
        return ['about','home','most-rated','most-watched','newest']
    def location(self, item):
        return reverse(item)