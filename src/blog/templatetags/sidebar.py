from django import template

from ..models import Post

register = template.Library()


@register.inclusion_tag('inc/sidebar.html')
def show_sidebar():
    posts = Post.objects.filter(status='published').order_by('-views')[:3]
    return {'popular_posts': posts}
