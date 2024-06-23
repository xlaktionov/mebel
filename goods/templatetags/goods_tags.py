from django import template

from goods.models import Categories

register = template.Library()

@register.simple_tag()
def categories__tag():
    return Categories.objects.all()