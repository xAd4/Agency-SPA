from django import template
from app.forms import AppointmentForm

register = template.Library()

@register.inclusion_tag("app/forms/form_appointment.html", takes_context=True)
def form_appointment(context):
    request = context['request']
    if request.user.is_authenticated:
        form = AppointmentForm()
        return {"form": form}
    else:
        return {"form": None}