from django.shortcuts import render
from .models import Patient
# Create your views here.


def index(request):
    patients = Patient.objects.all().order_by('lname')
    return render(request, 'patients/index.html', {'patients': patients})


def add_patient(request):
    
    create_pat= Patient.objects.create(
        fname = "Ali",
        lname =  "hadamakan",
        birth =  "2000-5-12",
        phone = "+213564875632",
        email = "ali@gmail.com",
        adresse = "no where"
    )
    return render(request, 'patients/index.html', {'patients': "patient created"})

def delete_patient(request, patient_id):
    Patient.objects.get(patient_id=patient_id).delete()
    return render(request, 'patients/index.html', {'patients': "patient deleted"})
