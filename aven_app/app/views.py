from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import AppointmentForm, ContactForm

# Create your views here.

class HomeView(FormView):
    template_name = "app/index.html"
    form_class = AppointmentForm  # Usamos AppointmentForm como el formulario principal
    success_url = reverse_lazy('status-200')

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
            contact = contact_form.save(commit=False)  # No guardar aún en la base de datos
            contact.user_published = self.request.user  # Asignar el usuario logueado
            contact.save()  # Ahora guardar en la base de datos
            return redirect(self.success_url)
        else:
            return self.form_invalid(appointment_form)
    
class PropertyGalleryView(TemplateView):
    template_name = "app/idea-details.html"