from django import template

from ..models import Catagory

register = template.Library()

@register.inclusion_tag('shared/Catagory_navbar.html')
def Catagory_navbar():
    return {
        'Catagory':Catagory.objects.filter(status=True)
    }