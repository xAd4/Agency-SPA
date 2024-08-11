from django import template
from app.models import Contact

register = template.Library()

@register.simple_tag
def contact_clients():
    contacts = Contact.objects.all()
    return contacts