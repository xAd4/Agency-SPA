from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView, FormView, DetailView, CreateView
from .forms import AppointmentForm, ContactForm
from .models import Gallery
from django import forms

# Create your views here.
#* IMPORTANT: VIEW HOME
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
    
#* IMPORTANT: VIEW DETAIL GALLERY
class PropertyGalleryView(DetailView):
    model = Gallery
    template_name = "app/idea-details.html"
    
#TODO: VIEW DETAIL CREATE: Exclusive use for staff
@method_decorator(staff_member_required, name="dispatch")
class PropertyGalleryCreateView(CreateView):
    model = Gallery
    template_name = "helpers/form_create_update.html"
    fields = ["squareFeet","garage","bedrooms","pool","build","image","title","content"]
    success_url = reverse_lazy("status-200")
    
    def get_form(self, form_class=None):
        form = super().get_form()
        form.fields["squareFeet"].widget = forms.TextInput(attrs={"class": "form-control", 'placeholder':"Square Feet"})
        form.fields["garage"].widget = forms.NumberInput(attrs={"class": "form-control", 'placeholder':"Garage"})
        form.fields["bedrooms"].widget = forms.NumberInput(attrs={"class": "form-control", 'placeholder':"Bedrooms"})
        form.fields["build"].widget = forms.TextInput(attrs={"class": "form-control", 'placeholder':"Build Year"})
        form.fields["image"].widget = forms.ClearableFileInput(attrs={"class": "form-control-file", 'placeholder':"Image"})
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control", 'placeholder':"Title"})
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control", 'placeholder':"Content"})
        return form