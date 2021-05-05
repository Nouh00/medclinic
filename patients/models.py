from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    birth = models.DateField()
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    adresse = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True
    def __str__(self):
        return self.fname
    

class Patient(Profile):
    patient_id = models.AutoField(primary_key=True)

    


