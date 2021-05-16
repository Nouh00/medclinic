from django.db import models
from patients.models import Patient

# Create your models here.
class consultation(models.Model):
    reason = models.CharField( max_length=50)
    cons_type = models.CharField( max_length=50)
    examine =  models.CharField(max_length=50)
    conclusion = models.CharField(max_length=50)
    patient = models.ForeignKey('patients.Patient',on_delete=models.SET_NULL, null=True)
    