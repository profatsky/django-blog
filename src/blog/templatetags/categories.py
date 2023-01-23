from django import template

from ..models import Category

register = template.Library()


@register.inclusion_tag('blog/category_list.html')
def show_categories(current_category=None):
    categories = Category.objects.all()
    return {'category_list': categories, 'current_category': current_category}
