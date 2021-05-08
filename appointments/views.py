from django.shortcuts import render, redirect
from .models import appointment
from patients.models import Patient
from .forms import add_appointment_form, add_patient_form
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users 

# Create your views here.
@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def index(request):
    pending_appointments = appointment.objects.filter(appointment_state='Pending', patient__isnull=False)
    Approved_appointments = appointment.objects.filter(appointment_state='Approved', patient__isnull=False)

    appointments = {
        "pending_appointments":pending_appointments,
        "approved_appointments":Approved_appointments
    }
    return render(request, 'appointments/index.html', appointments)



def add_appointments(request):
    patients = Patient.objects.order_by("-added_date")
    patient_form = add_patient_form()
    if request.method=='POST':
        appointment_date = request.POST['appointment_date']
        patient_form = add_patient_form(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            patient_id = Patient.objects.latest('patient_id')
            add_appointment = appointment.objects.create(appointment_date=appointment_date, appointment_state='Pending', patient=patient_id)
            return redirect('appointments:book_success')

    context = {'patient_form':patient_form}
    return render(request, 'appointments/book_appointment/add-appointments.html', context)


def book_success(request):
    return render(request, 'appointments/book_appointment/booking_success.html')



@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary'])
def delete_appointment(request, patient_id):
    appointment.objects.get(patient_id=patient_id).delete()
    return redirect('appointments:appointments')



@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def change_state(request, patient_id):
    appointments = appointment.objects.get(patient_id=patient_id)
    if appointments.appointment_state == 'Pending':
        appointments.appointment_state = 'Approved'
        appointments.save()

    return redirect('appointments:appointments')