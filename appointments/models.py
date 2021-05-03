from django.db import models


class appointment(models.Model):
    states=[('pined','approved')]
    appointment_date = models.DateField()
    appointment_state = models.CharField(max_length=10, choices=states)
    patient = models.ForeignKey('patients.Patient',on_delete=models.CASCADE)
