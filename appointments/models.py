from django.db import models


class appointment(models.Model):
    states=[("Approved","Approved"),("Pending","Pending")]
    appointment_date = models.DateTimeField()
    appointment_state = models.CharField(max_length=10, choices=states)
    patient = models.ForeignKey('patients.Patient',on_delete=models.SET_NULL, null=True)
    
    