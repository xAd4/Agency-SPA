from django.shortcuts import render
from django.urls import reverse_lazy
from django import forms
from django.views.generic import CreateView
from .forms import FormSignUpWithEmail

# Create your views here.

class SignUpView(CreateView):
    form_class = FormSignUpWithEmail
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def get_form(self, form_class = None):
        form = super(SignUpView, self).get_form()
        form.fields["username"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder':"Username"})
        form.fields["email"].widget = forms.EmailInput(attrs={"class": "form-control mb-2", 'placeholder':"Email"})
        form.fields["password1"].widget = forms.PasswordInput(attrs={"class": "form-control mb-2", 'placeholder':"Password"})
        form.fields["password2"].widget = forms.PasswordInput(attrs={"class": "form-control mb-2", 'placeholder':"Password confirmation"})
        return form