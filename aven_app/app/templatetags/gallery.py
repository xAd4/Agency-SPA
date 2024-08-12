from django import template
from app.models import Gallery

register = template.Library()

@register.simple_tag
def galleries():
    galleries = Gallery.objects.all()
    return galleries