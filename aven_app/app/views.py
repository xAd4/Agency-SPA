from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import AppointmentForm, ContactForm

# Create your views here.

class HomeView(FormView):
    template_name = "app/index.html"
    form_class = AppointmentForm  # Usamos AppointmentForm como el formulario principal
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()  # Añadimos ContactForm al contexto
        return context

    def post(self, request, *args, **kwargs):
        appointment_form = AppointmentForm(self.request.POST)
        contact_form = ContactForm(self.request.POST)

        if appointment_form.is_valid():
            appointment_form.save()
            return self.form_valid(appointment_form)
        elif contact_form.is_valid():
            contact_form.save()
            return self.form_valid(contact_form)
        else:
            return self.form_invalid(appointment_form)
    
class PropertyGalleryView(TemplateView):
    template_name = "app/idea-details.html"