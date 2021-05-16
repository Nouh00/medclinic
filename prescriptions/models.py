from django.db import models

# Create your models here.
class Document(models.Model):
    document_types=[(1,"prescription"),(2,"bill")]
    doc_date = models.DateTimeField(auto_now_add=True)
    doc_type = models.CharField(max_length=50, choices=document_types)
    consultation = models.ForeignKey('consultation.consultation',on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey('patients.doctor', on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey('patients.Patient',on_delete=models.SET_NULL, null=True)
    secretary = models.ForeignKey('patients.secretary', on_delete=models.SET_NULL, null=True)

    class Meta:
            abstract = True
    
    def __str__(self):
        return self.doc_type

class prescription(Document):
    prescription_id = models.AutoField(primary_key=True)
