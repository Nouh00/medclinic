from django.shortcuts import render
from .models import Patient
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users
# Create your views here.

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary'])
def index(request):
    patients = Patient.objects.all().order_by('lname')
    return render(request, 'patients/index.html', {'patients': patients})


@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary'])
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


@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary'])
def delete_patient(request, patient_id):
    Patient.objects.get(patient_id=patient_id).delete()
    return render(request, 'patients/index.html', {'patients': "patient deleted"})
