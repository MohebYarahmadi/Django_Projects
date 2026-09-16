from django import template
from djanog.db.models import Count

from blog.models import Post


register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest-posts.html')
def show_latest_posts(arg=5):
    latest_posts = Post.published.order_by('-published_at')[:arg]
    return {'latest_posts': latest_posts}
