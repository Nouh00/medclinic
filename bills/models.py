from django.db import models
from prescriptions.models import Document
# Create your models here.


class Bill(Document):
    bill_id = models.AutoField(primary_key=True)
    total = models.IntegerField()
