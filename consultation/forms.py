from django import forms
from django.db import models
from django.forms import fields
from .models import consultation



class consul_form(forms.ModelForm):
    class Meta:
        model = consultation
        fields = ('reason','cons_type','examine','conclusion')