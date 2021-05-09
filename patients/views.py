from django.shortcuts import render, redirect
from .models import Patient
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users
from appointments.forms import add_patient_form
# Create your views here.

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def index(request):
    patients = Patient.objects.all().order_by('lname')
    return render(request, 'patients/index.html', {'patients': patients})


@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def add_patient(request):
    patient_form = add_patient_form()
    if request.method=='POST':
        patient_form = add_patient_form(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('patients:add_success')

    context = {'patient_form':patient_form}
    return render(request, 'patients/add_patient/add_patient.html', context)


def add_success(request):
    return render(request, 'patients/add_patient/add_success.html')

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def delete_patient(request, patient_id):
    Patient.objects.get(patient_id=patient_id).delete()
    return redirect('patients:patients')


@login_required
def patient_profile(request, patient_id):
    patient = Patient.objects.get(patient_id=patient_id)
    patient_data = {
        'fname': patient.fname,
        'lname': patient.lname,
        'birth': patient.birth,   
        'phone': patient.phone,
        'email': patient.email,   
        'adresse': patient.adresse
    }

    return render(request, 'patients/profile/patient.html', patient_data)
