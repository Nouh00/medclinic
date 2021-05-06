from django.shortcuts import render, redirect
from .models import appointment
from patients.models import Patient
from .forms import add_appointment_form, add_patient_form
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    appointments = appointment.objects.all()
    return render(request, 'appointments/index.html', {"appointments": appointments})


def add_appointments(request):
    patients = Patient.objects.all("-added_date")
    patient_form = add_patient_form()
    appointment_form  = add_appointment_form()
    if request.method=='POST':
        patient_form = add_patient_form(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            appointment = appointment.objects.create()
            appointment_form = add_appointment_form(request.POST)
            if appointment_form.is_valid:
                appointment_form.save()
                return redirect('appointments:appointments')

    context = {'patient_form':patient_form,'appointment_form': appointment_form}
    return render(request, 'appointments/book_appointment/add-appointments.html', context)
