from django import template
import shop_app.views as views
from shop_app.models import Category

register = template.Library()


@register.inclusion_tag('catalog.html')
def list_category(category_selected=0):
    categories = Category.objects.all()
    return {'category': categories, 'category_selected': category_selected}