from django import forms
from .models import Appointment, Contact

#* IMPORTANT: APPOINTMENT FORM
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["firstName", "lastName", "email", "phoneNumber", "selectTimeList", "budget"]
        widgets = {
            "firstName": forms.TextInput(attrs={
                "class": "form-control", 
                "placeholder": "First Name",
                "style": "text-transform:none;",
            }),
            "lastName": forms.TextInput(attrs={
                "class": "form-control", 
                "placeholder": "Last Name",
                "style": "text-transform:none;",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control", 
                "placeholder": "Your Email",
                "style": "text-transform:none;",
            }),
            "phoneNumber": forms.TextInput(attrs={
                "class": "form-control", 
                "placeholder": "Your Phone",
                "style": "text-transform:none;",
            }),
            "selectTimeList": forms.Select(attrs={
                "class": "selectpicker form-control", 
                "data-style": "btn-white",
            }),
            "budget": forms.Select(attrs={
                "class": "selectpicker form-control", 
                "data-style": "btn-white",
            }),
        }
        
#* IMPORTANT: CONTACT FORM
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["firstName","lastName","email","phoneNumber","content"]
        widgets = {
            "firstName": forms.TextInput(attrs={
                "class": "form-control", 
                "placeholder": "First Name",
                "style": "text-transform:none;",
            }),
            "lastName": forms.TextInput(attrs={
                "class": "form-control", 
                "placeholder": "Last Name",
                "style": "text-transform:none;",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control", 
                "placeholder": "Your Email",
                "style": "text-transform:none;",
            }),
            "phoneNumber": forms.TextInput(attrs={
                "class": "form-control", 
                "placeholder": "Your Phone",
                "style": "text-transform:none;",
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Give us more details..",
                "rows": 6,
                "style": "text-transform:none;",
            }),
        }
