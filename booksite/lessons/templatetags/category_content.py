from django import template
from ..models import Category
register = template.Library()
@register.inclusion_tag('lessons/category.html')
def show_category(menu_class = 'category'):
    categories = Category.objects.all()
    return {"categories": categories, "menu_class": menu_class}