from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from taggit.models import Tag
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated_at


class TagSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        # Only include tags that are actually used by published posts
        return Tag.objects.filter(
            taggit_taggeditem_items__content_type__app_label='blog',
            taggit_taggeditem_items__content_type__model='post',
            taggit_taggeditem_items__object_id__in=Post.published.values_list('id', flat=True),
        ).distinct()

    def location(self, obj):
        return reverse('blog:post-list-by-tag', args=[obj.slug])

    def lastmod(self, obj):
        return Post.published.filter(tags=obj).latest('updated_at').updated_at
