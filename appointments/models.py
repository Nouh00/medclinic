from django.db import models


class appointment(models.Model):
    states=[(1,"Approved"),(2,"Waiting")]
    appointment_date = models.DateField()
    appointment_state = models.CharField(max_length=10, choices=states)
    patient = models.ForeignKey('patients.Patient',on_delete=models.CASCADE)
    def __str__(self):
        return self.patient
    