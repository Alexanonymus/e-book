from django import template
from ..models import SubCategory
register = template.Library()
@register.inclusion_tag('lessons/subcategory.html')

def show_subcategory(subcategory_class='subcategory'):
    subcategory = SubCategory.objects.all()
    return {"subcategory":subcategory, "subcategory_class":subcategory_class}