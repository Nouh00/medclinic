from django import forms
from django.db import models
from django.forms import widgets
from .models import drug


class add_drug_form(forms.ModelForm):
    
    class Meta:
        model = drug
        fields = ("brand","name")
        widgets={
            'name': forms.TextInput(attrs={
                "class":"form-control form-control-lg",
                "placeholder": "Drug name .."
            }),
            'brand': forms.TextInput(attrs={
                "class":"form-control form-control-lg",
                "placeholder": "Drug brand .."
            })
        }