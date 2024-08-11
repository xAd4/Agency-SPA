from django import template
from app.forms import ContactForm

register = template.Library()

@register.inclusion_tag("app/forms/contact_appointment.html", takes_context=True)
def contact_appointment(context):
    request = context['request']
    if request.user.is_authenticated:
        form = ContactForm()
        return {"form": form}
    else:
        return {"form": None}