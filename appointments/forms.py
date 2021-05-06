from django import forms
from patients.models import Patient
from .models import appointment


class add_patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('fname', 'lname', 'birth', 'phone', 'email', 'adresse')
        widgets = {
            'fname': forms.TextInput(attrs={
                "class":"form-control form-control-lg",
                "placeholder": "First name .."
                }),
            'lname': forms.TextInput(attrs={
                "class":"form-control form-control-lg",
                "placeholder": "Last name .."
                }), 
            'birth': forms.TextInput(attrs={
                "class":"form-control form-control-lg",
                "placeholder": "Birth date ..",
                "onfocus": "(this.type='date')"
                }), 
            'phone': forms.NumberInput(attrs={
                "class":"form-control form-control-lg",
                "id":"numberinput",
                "placeholder":"Phone number .."
                }), 
            'email': forms.TextInput(attrs={
                "class":"form-control form-control-lg",
                "placeholder":"example@mail.com"
                }), 
            'adresse': forms.TextInput(attrs={
                "class":"form-control form-control-lg",
                "placeholder":"Adresse .."
                }),
        }


class add_appointment_form(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ('appointment_date', 'appointment_state',)
        widgets = {
            'appointment_date': forms.TextInput(attrs={
                "class":"form-control form-control-lg",
                "placeholder": "Appointment date ..", 
                "onfocus": "(this.type='date')"
                }),
            'appointment_state': forms.HiddenInput(attrs={
                "value":"Pending",
                }),
        }