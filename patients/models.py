from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    birth = models.DateTimeField()
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    adresse = models.CharField(max_length=100)

    class Meta:
        abstract = True


class Patient(Profile):
    patient_id = models.AutoField(primary_key=True)

    


